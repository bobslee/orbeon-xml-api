from . import CommonTestCase

from ..controls import StringControl


class SecretTestCase(CommonTestCase):

    def setUp(self):
        super(SecretTestCase, self).setUp()
        self.control = self.builder.controls['secret']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Password Field')
        self.assertEqual(self.control.hint, 'The password is 42 ;)')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Password Field')
        self.assertEqual(self.control._resource_element.hint, 'The password is 42 ;)')
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, '42')
        self.assertEqual(self.control.default_value, '42')

    def test_runner_value(self):
        text = 'The question to life and everything is 42.'
        self.assertEqual(self.runner.get_value('secret'), text)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.secret.label, 'Password Field')
        text = 'The question to life and everything is 42.'
        self.assertEqual(self.runner.form.secret.value, text)
