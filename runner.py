from builder import Builder
from utils import generate_xml_root


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

        self.form = RunnerForm(self)

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_builder(self):
        self.builder = Builder(self.builder_xml, self.lang)


class RunnerForm:

    def __init__(self, runner):
        self.runner = runner

    # TODO implement Pythonic object/attr notation to get control values.
    def __getattr__(self, name):
        raise NotImplementedError
