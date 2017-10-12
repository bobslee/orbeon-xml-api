from lxml import etree

import xmltodict

from controls import StringControl, DateControl, TimeControl, DateTimeControl, \
    BooleanControl, AnyUriControl, EmailControl, DecimalControl, \
    Select1Control, OpenSelect1Control, SelectControl, ImageAnnotationControl
from utils import generate_xml_root

XF_TYPE_CONTROL = {
    'xf:string': StringControl,
    'xs:string': StringControl,
    'xforms:string': StringControl,

    'xf:date': DateControl,
    'xs:date': DateControl,
    'xforms:date': DateControl,

    'xf:time': TimeControl,
    'xs:time': TimeControl,
    'xforms:time': TimeControl,

    'xf:dateTime': DateTimeControl,
    'xs:dateTime': DateTimeControl,
    'xforms:dateTime': DateTimeControl,

    'xf:boolean': BooleanControl,
    'xs:boolean': BooleanControl,
    'xforms:boolean': BooleanControl,

    'xf:anyURI': AnyUriControl,
    'xs:anyURI': AnyUriControl,
    'xforms:anyURI': AnyUriControl,

    'xf:email': EmailControl,
    'xs:email': EmailControl,
    'xforms:email': EmailControl,

    'xf:decimal': DecimalControl,
    'xs:decimal': DecimalControl,
    'xforms:decimal': DecimalControl,

    'xf:integer': DecimalControl,
    'xs:integer': DecimalControl,
    'xforms:integer': DecimalControl,

    'xf:double': DecimalControl,
    'xs:double': DecimalControl,
    'xforms:double': DecimalControl,
}


class Builder:

    def __init__(self, xml, lang='en', **kwargs):
        self.xml = xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        self._control_objects = {}
        if kwargs.get('controls', False):
            self.set_control_objects(kwargs['controls'])

        self.context = None
        if kwargs.get('context', False):
            self.set_context(kwargs['context'])

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
            raise Exception("[orbeon-xml-api] Found %s elements for: %s" % (len(resource), query))

        parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
        resource_root = etree.XML(etree.tostring(resource[0]).encode('utf-8'), parser)
        resource_xml = etree.tostring(resource_root)
        res_dict = xmltodict.parse(resource_xml)

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
            if name is None:
                continue

            k = name
            k = k.replace('-', '')
            k = k.replace('.', '_')
            self.sanitized_control_names[k] = name

    def set_control_objects(self, control_objects):
        for k, v in control_objects.items():
            self.add_control_object(k, v)

    def set_context(self, context):
        self.context = context

    def add_control_object(self, name, control_obj):
        supported = False
        for klass in XF_TYPE_CONTROL.values():
            if name == klass.__name__:
                supported = True

        if not supported:
            for parent in control_obj.__bases__:
                if parent.__name__ == 'ImageAnnotationControl':
                    supported = True

        # If still not supported
        # TODO refactor to nicer code
        if not supported:
            raise Exception("Unsupported Control Object: %s" % name)

        self._control_objects[name] = control_obj

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

        self.name = None
        self.set_name()

        self.xf_type = element.get('type', 'xf:string')

        self.parent = None
        self.set_parent()

    def set_name(self):
        # XXX Maybe also add a `ref` property set_ref()
        if self.element.get('name'):
            self.name = self.element.get('name')
        elif self.element.get('ref'):
            self.name = self.element.get('ref')

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
            if self.builder._control_objects.get('Select1Control', False):
                return self.builder._control_objects.get('Select1Control')(self.builder, self, element)
            else:
                return Select1Control(self.builder, self, element)

        if fr_control_tag == 'open-select1':
            if self.builder._control_objects.get('OpenSelect1Control', False):
                return self.builder._control_objects.get('OpenSelect1Control')(self.builder, self, element)
            else:
                return OpenSelect1Control(self.builder, self, element)

        elif fr_control_tag == 'select':
            if self.builder._control_objects.get('SelectControl', False):
                return self.builder._control_objects.get('SelectControl')(self.builder, self, element)
            else:
                return SelectControl(self.builder, self, element)

        elif fr_control_tag == 'wpaint':
            if self.builder._control_objects.get('ImageAnnotationControl', False):
                return self.builder._control_objects.get('ImageAnnotationControl')(self.builder, self, element)
            else:
                return ImageAnnotationControl(self.builder, self, element)

        else:
            control_class_name = XF_TYPE_CONTROL[self.xf_type].__name__

            if self.builder._control_objects.get(control_class_name, False):
                return self.builder._control_objects.get(control_class_name)(self.builder, self, element)
            else:
                return XF_TYPE_CONTROL[self.xf_type](self.builder, self, element)


class Resource:

    def __init__(self, builder, element):
        self.builder = builder
        self.element = element
