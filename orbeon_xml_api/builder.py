from lxml import etree

import xmltodict

from controls import StringControl, DateControl, TimeControl, DateTimeControl, \
    BooleanControl, AnyUriControl, EmailControl, DecimalControl, \
    Select1Control, OpenSelect1Control, SelectControl, ImageAnnotationControl
from utils import generate_xml_root

XF_TYPE_CONTROL = {
    'xf:string': StringControl,
    'xs:string': StringControl,
    'xf:date': DateControl,
    'xf:time': TimeControl,
    'xf:dateTime': DateTimeControl,
    'xf:boolean': BooleanControl,
    'xf:anyURI': AnyUriControl,
    'xf:email': EmailControl,
    'xf:decimal': DecimalControl
}

CONTROL_DECODERS = ['string', 'date', 'any_uri', 'image_annotation']


class Builder:

    def __init__(self, xml, lang='en', **kwargs):
        self.xml = xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        self.control_decoders = {}
        if kwargs.get('control_decoders', False):
            self.set_control_decoders(kwargs['control_decoders'])

        self.binds = {}
        self.set_binds()

        self.fr_body_elements = []
        self.set_fr_body_elements()

        self.resource = {}
        self.set_resource()

        self.controls = {}
        self.set_controls()

        self.sanitized_control_names = {}
        self.set_sanitized_control_names()

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_binds(self):
        # TODO
        # Fix/handle duplicates, due to iteration control(s)
        # Consider whether a self.binds pair, should assign a value as a list, with duplicates.
        # Refactor other code.
        q_left = "//*[@id='fr-form-binds']//*[name()='xforms:bind']"
        q_right = "//*[@id='fr-form-binds']//*[name()='xf:bind']"

        query = "%s|%s" % (q_left, q_right)

        for e in self.xml_root.xpath(query):
            self.binds[e.get('id')] = Bind(self, e)

    def set_resource(self):
        query = "//*[@id='fr-form-resources']/resources//resource[@xml:lang='%s']" % self.lang

        resource = self.xml_root.xpath(query)

        if len(resource) != 1:
            raise Exception("[orbeon-xml-api] Found %s for: %s" % query)

        res_dict = xmltodict.parse(etree.tostring(resource[0]))

        for tag, v in res_dict.get('resource', {}).items():
            self.resource[tag] = Resource(self, v)

    def set_fr_body_elements(self):
        query = "//*[name()='fr:body']//*[@bind]"
        self.fr_body_elements = self.xml_root.xpath(query)

    def set_controls(self):
        for el in self.fr_body_elements:
            bind = self.binds[el.get('bind')]
            control = bind.get_fr_control_object(el)

            if control is not None:
                self.controls[bind.name] = control

    def set_sanitized_control_names(self):
        for name in self.controls.keys():
            k = name
            k = k.replace('-', '')
            k = k.replace('.', '_')
            self.sanitized_control_names[k] = name

    def set_control_decoders(self, control_decoders):
        for k, v in control_decoders.items():
            self.add_control_decoder(k, v)

    def add_control_decoder(self, name, decoder_obj):
        if name not in CONTROL_DECODERS:
            raise Exception("Unsupported Control Decoder: %s" % name)

        if not callable(getattr(decoder_obj, 'decode', None)):
            raise Exception("Method `decode()` is missing in Control Decoder for: %s" % name)

        self.control_decoders[name] = decoder_obj

    # TODO
    def get_structure(self):
        """
        {
            CONTROL_NAME: {
                'xf_type': XF_TYPE,
                'bind': Bind,
                'control': Control,
                'parent': {
                    CONTROL_NAME: {
                        'xf_type': XF_TYPE,
                        'bind': Bind,
                        'control': Control,
                        'parent': None,
                    }
                }
            },
            ...
        }
        """


class Bind:

    def __init__(self, builder, element):
        self.builder = builder
        self.element = element
        self.id = element.get('id')
        self.name = element.get('name')
        self.xf_type = element.get('type', 'xf:string')

        self.parent = None
        self.set_parent()

    def set_parent(self):
        parent_element = self.element.getparent()

        if etree.QName(parent_element).localname == 'bind' and \
           parent_element.get('id') != 'fr-form-binds':
            self.parent = Bind(self.builder, parent_element)
        else:
            self.parent = None

    def get_fr_control_object(self, element):
        fr_control_tag = etree.QName(element).localname

        if fr_control_tag == 'select1':
            return Select1Control(self.builder, self, element)
        if fr_control_tag == 'open-select1':
            return OpenSelect1Control(self.builder, self, element)
        elif fr_control_tag == 'select':
            return SelectControl(self.builder, self, element)
        elif fr_control_tag == 'wpaint':
            return ImageAnnotationControl(self.builder, self, element)
        else:
            return XF_TYPE_CONTROL[self.xf_type](self.builder, self, element)


class Resource:

    def __init__(self, builder, element):
        self.builder = builder
        self.element = element
