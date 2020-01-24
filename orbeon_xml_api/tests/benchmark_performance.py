import unittest

from ..builder import Builder
from ..runner import Runner
from ..utils import xml_from_file


class BenchmarkPerformanceTestCase(unittest.TestCase):

    def setUp(self):
        super(BenchmarkPerformanceTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')
        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')
        self.builder = Builder(self.builder_xml)

    # TODO remove this from API support?
    # Too slow
    def test_performance_10_runners_with_builder_xml(self):
        for i in range(1, 10):
            Runner(self.runner_xml, None, self.builder_xml)

    def test_performance_100_runners_with_builder_xml(self):
        for i in range(1, 100):
            Runner(self.runner_xml, None, self.builder_xml)

    def test_performance_1000_runners_with_builder_xml(self):
        for i in range(1, 1000):
            Runner(self.runner_xml, None, self.builder_xml)

    # Fast enough ;)
    def test_performance_10_runners_with_builder_object(self):
        for i in range(1, 10):
            Runner(self.runner_xml, self.builder)

    def test_performance_100_runners_with_builder_object(self):
        for i in range(1, 100):
            Runner(self.runner_xml, self.builder)

    def test_performance_1000_runners_with_builder_object(self):
        for i in range(1, 1000):
            Runner(self.runner_xml, self.builder)
