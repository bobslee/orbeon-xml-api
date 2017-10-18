from xmlunittest import XmlTestCase

from .test_common import CommonTestCase
from ..builder import Builder
from ..runner import Runner
from ..runner_copy_builder_merge import RunnerCopyBuilderMerge
from ..utils import xml_from_file


class RunnerBuilderMergeTestCase(CommonTestCase, XmlTestCase):

    def setUp(self):
        super(RunnerBuilderMergeTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')
        self.builder_1_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')

        # Adds: input-2 (name, is text control)
        self.builder_2_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration_verion2.xml')

        self.runner = Runner(self.runner_xml, None, self.builder_1_xml)
        self.builder_2 = Builder(self.builder_2_xml)

    def test_merge_by_runner_object(self):
        merged_runner = self.runner.merge(self.builder_2)

        root = self.assertXmlDocument(merged_runner.xml)

        # Check original data (not harmed by merge)
        self.assertXpathsOnlyOne(root, ['//input'])
        self.assertEqual(merged_runner.form.input.label, 'Input Field')
        self.assertEqual(merged_runner.form.input.value, 'John')

        # New controls
        self.assertXpathsOnlyOne(root, ['//input-2'])
        self.assertEqual(merged_runner.form.input2.label, 'Input Field 2')
        self.assertEqual(merged_runner.form.input2._parent._bind.name, 'text-controls')

    def test_merge_by_runner_builer_merge_object(self):
        merger = RunnerCopyBuilderMerge(self.runner, self.builder_2)
        merged_runner = merger.merge()

        root = self.assertXmlDocument(merged_runner.xml)

        # Check original data (not harmed by merge)
        self.assertXpathsOnlyOne(root, ['//input'])
        self.assertEqual(merged_runner.form.input.label, 'Input Field')
        self.assertEqual(merged_runner.form.input.value, 'John')

        # New controls
        self.assertXpathsOnlyOne(root, ['//input-2'])
        self.assertEqual(merged_runner.form.input2.label, 'Input Field 2')

    def test_merge_no_copy(self):
        # Check first for value
        self.assertEqual(self.runner.form.NC_nocopyfield.value, 'After merge this should be empty.')

        merger = RunnerCopyBuilderMerge(self.runner, self.builder_2, no_copy_prefix='NC.')
        merged_runner = merger.merge()

        self.assertEqual(merged_runner.form.NC_nocopyfield.value, None)
