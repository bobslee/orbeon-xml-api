from . import CommonTestCase

from orbeon_xml_api.controls import StringControl


class OutputTestCase(CommonTestCase):

    def setUp(self):
        super(OutputTestCase, self).setUp()
        self.control = self.builder.controls['output']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Text Output')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.element.label, 'Text Output')
        self.assertEqual(self.control.element.hint, None)
        self.assertEqual(self.control.element.alert, None)

    def test_builder_form_default_value(self):
        text = 'Great love and great achievements involve great risk.'
        self.assertEqual(self.control.default_raw_value, text)
        self.assertEqual(self.control.default_value, text)

    def test_runner_form(self):
        text = 'Great risk and less achievements involve great love.'
        self.assertEqual(self.runner.get_value('output'), text)
        self.assertEqual(self.runner.form.output, text)
