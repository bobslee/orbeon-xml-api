from . import CommonTestCase

from orbeon_xml_api.controls import StringControl


class TextareaTestCase(CommonTestCase):

    def setUp(self):
        super(TextareaTestCase, self).setUp()
        self.control = self.builder.controls['textarea']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'textarea-bind')
        self.assertEqual(self.control.bind.name, 'textarea')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Text Area')
        self.assertEqual(self.control.hint, 'Standard text area')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.element.label, 'Text Area')
        self.assertEqual(self.control.element.hint, 'Standard text area')

        self.assertEqual(self.control.element.alert, None)

    def test_builder_form_default_value(self):
        self.assertIn('Music is an art', self.control.default_raw_value)
        self.assertIn('Music is an art', self.control.default_value)

    def test_runner_form(self):
        text = 'Programming is an art form whose medium is a computer.'
        self.assertEqual(self.runner.get_value('textarea'), text)
        self.assertEqual(self.runner.form.textarea, text)
