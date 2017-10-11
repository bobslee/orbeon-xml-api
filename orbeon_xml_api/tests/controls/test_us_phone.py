from . import CommonTestCase

from ..controls import StringControl


class UsPhoneTestCase(CommonTestCase):

    def setUp(self):
        super(UsPhoneTestCase, self).setUp()
        self.control = self.builder.controls['us-phone']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'us-phone-bind')
        self.assertEqual(self.control._bind.name, 'us-phone')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'typed-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'typed-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Typed Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'US Phone Number')
        self.assertEqual(self.control.hint, 'US phone number field')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'US Phone Number')
        self.assertEqual(self.control._resource_element.hint, 'US phone number field')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, '5555555555')
        self.assertEqual(self.control.default_value, '5555555555')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('us-phone'), '1234567890')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.usphone.label, 'US Phone Number')
        self.assertEqual(self.runner.form.usphone.value, '1234567890')
