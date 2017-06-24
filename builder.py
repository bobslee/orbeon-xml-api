from lxml import etree

from utils import generate_xml_root, sanitize_xml


class Builder:

    def __init__(self, xml, lang='en'):
        self.xml = xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        self.binds = {}
        self.set_binds()

        self.controls = {}
        self.set_controls()

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_binds(self):
        q_left = "//*[@id='fr-form-binds']//*[name()='xforms:bind']"
        q_right = "//*[@id='fr-form-binds']//*[name()='xf:bind']"

        query = "%s|%s" % (q_left, q_right)

        for e in self.xml_root.xpath(query):
            self.binds[e.get('id')] = Bind(self, e)

    def set_controls(self):
        query = "//*[name()='fr:body']//*[@bind]"

        for e in self.xml_root.xpath(query):
            bind = self.binds[e.get('bind')]
            self.controls[bind.name] = XS_TYPE_CONTROL[bind.xs_type](self, bind, e)

    # TODO
    def get_structure(self):
        """
        {
            CONTROL_NAME: {
                'xs_type': XS_TYPE,
                'bind': Bind,
                'control': Control,
                'parent': {
                    CONTROL_NAME: {
                        'xs_type': XS_TYPE,
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
        self.xs_type = element.get('xs:type', 'xf:string')

        self.parent = None
        self.set_parent()

    def set_parent(self):
        parent_element = self.element.getparent()

        if etree.QName(parent_element).localname == 'bind' and \
           parent_element.get('id') != 'fr-form-binds':
            self.parent = Bind(self.builder, parent_element)
        else:
            self.parent = None


class Element:
    """
    The Element of a Control
    """

    def __init__(self, control):
        self.control = control

    def __getattr__(self, name):
        """
        Get Element attr/property via refs.
        For example, a 'label', 'hint', 'alert'
        """
        if name in self.control.refs:
            query = "//resources/resource[@xml:lang='%s']/%s" % (
                self.control.builder.lang,
                self.control.refs[name]
            )
            res = self.control.builder.xml_root.xpath(query)
            if len(res) > 0:
                return res[0].text
            else:
                return None


class Control:

    def __init__(self, builder, bind, element):
        self.builder = builder
        self.bind = bind
        self._element = element

        self.parent = None
        self.set_parent()

        self.refs = {}
        self.set_refs()

        # model_instance is like raw default_value.
        # Still called model_instance, because of FB terminology.
        self.model_instance = None
        self.set_model_instance()

        self.default_value = None
        self.set_default_value()

        self.element = Element(self)

    def set_parent(self):
        if self.bind.parent and self.bind.parent.name in self.builder.controls:
            self.parent = self.builder.controls[self.bind.parent.name]

    def set_model_instance(self):
        if not self.bind.parent:
            return

        # TODO namespace prefix Error
        # query = "//xf:model/xf:instance/form/%s/%s" % (
        query = "//form/%s/%s" % (
            self.bind.parent.name,
            self.bind.name
        )

        res = self.builder.xml_root.xpath(query)

        if len(res) > 0:
            self.model_instance = res[0]

    def set_refs(self):
        """
        EXAMPLES:

        ref = '$form-resources/section-1/label'
        ref_name = 'label'
        ref_value = 'section-1/label'
        """
        for child in self._element.iterchildren():
            if child.get('ref'):
                ref = child.get('ref')
                ref_items = ref.split('/')

                if ref_items[0] == '$form-resources':
                    ref_name = ref_items[-1]
                    ref_value = '/'.join(ref_items[1:])
                    self.refs[ref_name] = ref_value

    def set_default_value(self):
        raise NotImplementedError

    def encode(self, value):
        """
        By the self.datatype (handler):
        >> self.datetype.encode(value)
        """
        raise NotImplementedError

    def decode(self, value):
        """
        By the self.datatype (handler):
        >> self.datetype.decode(value)
        """
        raise NotImplementedError


class StringControl(Control):

    def set_default_value(self):
        self.default_value = self.decode(getattr(self.model_instance, 'text', None))

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class DateControl(Control):

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class TimeControl(Control):
    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class DateTimeControl(Control):
    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class BooleanControl(Control):
    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        if value == 'true':
            return True
        elif value == 'false':
            return False

    def encode(self, value):
        # TODO isinstance(value, bool) validate?
        if value:
            return 'true'
        else:
            return 'false'


class AnyURIControl(Control):
    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class EmailControl(StringControl):
    pass


class DecimalControl(StringControl):
    pass


XS_TYPE_CONTROL = {
    'xf:string': StringControl,
    'xs:string': StringControl,
    'xf:date': DateControl,
    'xf:time': TimeControl,
    'xf:dateTime': DateTimeControl,
    'xf:boolean': BooleanControl,
    'xf:anyURI': AnyURIControl,
    'xf:email': EmailControl,
    'xf:decimal': DecimalControl
}
