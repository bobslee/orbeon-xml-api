import unittest
import re

from builder import Builder
from runner import Runner
from utils import xml_from_file


class RunnerTestCase(unittest.TestCase):

    def setUp(self):
        super(RunnerTestCase, self).setUp()

        runner_xml = xml_from_file('tests/data', 'test_controls_runner.xml')
        builder_xml = xml_from_file('tests/data', 'test_controls_builder.xml')

        self.runner = Runner(runner_xml, builder_xml)
