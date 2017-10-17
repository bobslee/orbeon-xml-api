from xmlunittest import XmlTestCase

from .test_common import CommonTestCase
from ..builder import Builder
from ..runner import Runner
from ..utils import xml_from_file


class RunnerMergeBuilderTestCase(CommonTestCase, XmlTestCase):

    def setUp(self):
        super(RunnerMergeBuilderTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')
        self.builder_1_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')

        # Adds: input-2 (name, is text control)
        self.builder_2_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration_verion2.xml')

        self.runner = Runner(self.runner_xml, None, self.builder_1_xml)
        self.builder_2 = Builder(self.builder_2_xml)

    def test_merge(self):
        merged_runner = self.runner.merge(self.builder_2)

        root = self.assertXmlDocument(merged_runner.xml)

        # Original data
        self.assertXpathsOnlyOne(root, ['//input'])
        #self.assertXpathValues(root, '//input/text()', ('John'))

        # New controls
        self.assertXpathsOnlyOne(root, ['//input-2'])
