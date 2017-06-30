import unittest
import re

from datetime import datetime

from orbeon_xml_api.builder import Builder
from orbeon_xml_api.runner import Runner, RunnerForm
from orbeon_xml_api.utils import xml_from_file


class RunnerTestCase(unittest.TestCase):

    def setUp(self):
        super(RunnerTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner.xml')
        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder.xml')

        self.runner = Runner(self.runner_xml, None, self.builder_xml)

    # TODO
    def _test_constructor(self):
        self.assertRaisesRegex(
            Runner(self.runner_xml)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder_xml)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder)
        )

        self.assertRaisesRegex(
            Runner(self.runner_xml, self.builder_xml, self.builder)
        )

        # Ok tests
        runner = Runner(self.runner_xml, None, self.builder_xml)
        self.assertIsInstance(runner, Runner)

        runner = Runner(self.runner_xml, self.builder)
        self.assertIsInstance(runner, Runner)
        self.assertIsInstance(self.runner.form, RunnerForm)

    def test_input(self):
        self.assertIsInstance(self.runner.form, RunnerForm)

        _input = self.runner.form.get('input')

        self.assertEqual(_input.raw_value, 'John')
        self.assertEqual(_input.value, 'John')

    def test_date(self):
        _date = self.runner.form.get('date')

        date_obj = datetime.strptime('2017-07-01', '%Y-%m-%d').date()

        self.assertEqual(_date.raw_value, '2017-07-01')
        self.assertEqual(_date.value, date_obj)
