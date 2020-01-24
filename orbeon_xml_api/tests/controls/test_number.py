from . import CommonTestCase

from ..controls import DecimalControl


class NumberTestCase(CommonTestCase):

    def setUp(self):
        super(NumberTestCase, self).setUp()
        self.control = self.builder.controls['number']

    def test_control(self):
        self.assertIsInstance(self.control, DecimalControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'number-bind')
        self.assertEqual(self.control._bind.name, 'number')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'typed-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'typed-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Typed Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Number')
        self.assertEqual(self.control.hint, 'Number field with validation')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Number')
        self.assertEqual(self.control._resource_element.hint, 'Number field with validation')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, '299792458')
        self.assertEqual(self.control.default_value, 299792458)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('number'), 19792017)
        self.assertIsInstance(self.runner.get_value('number'), int)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.number.label, 'Number')
        self.assertEqual(self.runner.form.number.value, 19792017)
        self.assertEqual(self.runner.form.number.raw_value, '19792017')
        self.assertIsInstance(self.runner.form.number.value, int)
