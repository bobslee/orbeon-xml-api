from builder import Builder
from utils import generate_xml_root


class Runner:

    def __init__(self, xml, builder_xml, lang='en'):
        self.xml = xml
        self.builder_xml = builder_xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        self.builder = None
        self.set_builder()

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_builder(self):
        self.builder = Builder(self.builder_xml, self.lang)
