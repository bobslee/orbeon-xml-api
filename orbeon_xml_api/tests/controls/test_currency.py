from . import CommonTestCase

from ..controls import DecimalControl


class CurrencyTestCase(CommonTestCase):

    def setUp(self):
        super(CurrencyTestCase, self).setUp()
        self.control = self.builder.controls['currency']

    def test_control(self):
        self.assertIsInstance(self.control, DecimalControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'currency-bind')
        self.assertEqual(self.control._bind.name, 'currency')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'typed-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'typed-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Typed Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Currency')
        self.assertEqual(self.control.hint, 'Currency field')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Currency')
        self.assertEqual(self.control._resource_element.hint, 'Currency field')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, '10.99')
        self.assertEqual(self.control.default_value, 10.99)
        self.assertIsInstance(self.control.default_value, float)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('currency'), 101.33)
        self.assertIsInstance(self.runner.get_value('currency'), float)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.currency.label, 'Currency')
        self.assertEqual(self.runner.form.currency.value, 101.33)
        self.assertEqual(self.runner.form.currency.raw_value, '101.33')
        self.assertIsInstance(self.runner.form.currency.value, float)
