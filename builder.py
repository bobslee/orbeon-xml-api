from utils import generate_xml_root, sanitize_xml


class Builder(object):

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
        xml_root = generate_xml_root(self.xml)

        if xml_root is not None:
            sanitize_xml(xml_root)
            # A reference causes silly issues when traversing the object.
            self.xml_root = xml_root.__copy__()

    def set_binds(self):
        q_left = "//*[@id='fr-form-binds']//*[name()='xforms:bind']"
        q_right = "//*[@id='fr-form-binds']//*[name()='xf:bind']"

        query = "%s|%s" % (q_left, q_right)

        for e in self.xml_root.xpath(query):
            id = e.get('id')
            self.binds[id] = Bind(self, id, e)

    def set_controls(self):
        query = "//*[name()='fr:body']//*[@bind]"

        for e in self.xml_root.xpath(query):
            bind = self.binds[e.get('bind')]
            self.controls[bind.name] = Control(self, bind, e)


class Bind(object):

    def __init__(self, builder, id, element):
        self.builder = builder
        self.id = id
        self.name = element.get('name')
        self.element = element

class Control(object):

    def __init__(self, builder, bind, element):
        self.builder = builder
        self.bind = bind
        self.element = element

        self.refs = {}
        self.set_refs()

    def set_refs(self):
        for child in self.element.iterchildren():
            if child.get('ref'):
                ref = child.get('ref')
                # ref_name: '$form-resources/section-1/label' becomes 'label'
                ref_name = ref.split('/')[-1]
                # ref_value: '$form-resources/section-1/label' becomes 'section-1/label'
                ref_value = '/'.join(ref.split('/')[1:])
                self.refs[ref_name] = ref_value

    def __getattr__(self, name):
        """
        Get Element attr/property via refs.
        For example, a 'label', 'hint', 'alert'
        """
        if name in self.refs:
            query = "//resources/resource[@xml:lang='%s']/%s" % (self.builder.lang, self.refs[name])
            res = self.builder.xml_root.xpath(query)
            if len(res) > 0:
                return res[0].text
            else:
                return None
        else:
            return super(Control, self).__getattr__(name)
