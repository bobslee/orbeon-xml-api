from . import CommonTestCase

from ..controls import StringControl


class EmailTestCase(CommonTestCase):

    def setUp(self):
        super(EmailTestCase, self).setUp()
        self.control = self.builder.controls['email']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'email-bind')
        self.assertEqual(self.control.bind.name, 'email')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'typed-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'typed-controls')
        self.assertEqual(self.control.parent.resource_element.label, 'Typed Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Email Address')
        self.assertEqual(self.control.hint, 'Email field with validation')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.resource_element.label, 'Email Address')
        self.assertEqual(self.control.resource_element.hint, 'Email field with validation')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control.resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'info@orbeon.com')
        self.assertEqual(self.control.default_value, 'info@orbeon.com')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('input'), 'John')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.email.label, 'Email Address')
        self.assertEqual(self.runner.form.email.value, 'bob@novacode.nl')
