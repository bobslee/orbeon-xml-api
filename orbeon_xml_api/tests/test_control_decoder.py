import unittest
from datetime import datetime, timedelta

from ..builder import Builder
from ..runner import Runner
from ..utils import xml_from_file


class StringDecoder(object):

    def __init__(self):
        self.username = 'novacode'
        self.api_token = 'abc123'

    def decode(self, value):
        new_value = "%s FROM STRING DECODER" % value
        return new_value


class DateDecoder(object):

    def decode(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date() + timedelta(days=10)


class ControlDecoderTestCase(unittest.TestCase):

    def setUp(self):
        super(ControlDecoderTestCase, self).setUp()

        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder.xml')
        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner.xml')

    def test_simple_input_decoder(self):
        control_decoders = {
            'string': StringDecoder()
        }
        self.builder = Builder(self.builder_xml, 'en', control_decoders=control_decoders)
        self.runner = Runner(self.runner_xml, self.builder)

        self.assertEqual(self.runner.form.input.value, 'John FROM STRING DECODER')

    def test_multiple_input_decoder(self):
        control_decoders = {
            'string': StringDecoder(),
            'date': DateDecoder()
        }
        self.builder = Builder(self.builder_xml, 'en', control_decoders=control_decoders)
        self.runner = Runner(self.runner_xml, self.builder)

        self.assertEqual(self.runner.form.input.value, 'John FROM STRING DECODER')

        date_obj_add_10_days = datetime.strptime('2017-07-11', '%Y-%m-%d').date()
        self.assertEqual(self.runner.form.date.value, date_obj_add_10_days)
