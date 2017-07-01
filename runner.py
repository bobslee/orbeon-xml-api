from orbeon_xml_api.builder import Builder
from orbeon_xml_api.utils import generate_xml_root


class Runner:

    def __init__(self, xml, builder=None, builder_xml=None, lang='en'):
        """
        @param builder Builder
        @param builder_xml str
        """

        if builder and builder_xml:
            raise Exception("Constructor accepts either builder or builder_xml.")

        if builder:
            assert isinstance(builder, Builder)
        elif builder_xml:
            assert isinstance(builder_xml, bytes)
        else:
            raise Exception("Provide either the argument: builder or builder_xml.")

        self.xml = xml
        self.builder_xml = builder_xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        self.builder = None
        self.set_builder()

        self.values = {}
        self.set_values()

        self.form = RunnerForm(self)

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_builder(self):
        self.builder = Builder(self.builder_xml, self.lang)

    def set_values(self):
        for name, control in self.builder.controls.items():
            element = self.get_form_element(name)

            if element is not False:
                self.values[name] = control.decode_form_element(element)

    def get_form_element(self, name):
        """
        @param name str The control name (form element tag)
        """

        if name not in self.builder.controls:
            return False

        control = self.builder.controls[name]
        if control.parent is None:
            return False
            # query = "//form/%s" % name
        else:
            query = "//form/%s/%s" % (control.parent.bind.name, name)

        res = self.xml_root.xpath(query)

        # TODO Fix composite controls like 'us-address'
        # if len(res) > 1 or not res or len(res[0].getchildren()) > 1:
        #     return False

        return res[0]

    def get_value(self, name):
        return self.values[name]

    def set_value(self, name, value):
        """
        Set Runner Control XML value.
        """
        pass


class RunnerForm:

    def __init__(self, runner):
        self._runner = runner

    def __getattr__(self, s_name):
        name = self._runner.builder.sanitized_control_names.get(s_name, False)
        if name:
            return self._runner.get_value(name)
        else:
            return False
