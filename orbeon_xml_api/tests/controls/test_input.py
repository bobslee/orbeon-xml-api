from . import CommonTestCase

from ..controls import StringControl


class InputTestCase(CommonTestCase):

    def setUp(self):
        super(InputTestCase, self).setUp()
        self.control = self.builder.controls['input']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'input-bind')
        self.assertEqual(self.control.bind.name, 'input')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'text-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'text-controls')
        self.assertEqual(self.control.parent.resource_element.label, 'Text Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Input Field')
        self.assertEqual(self.control.hint, 'Standard input field')
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.resource_element.label, 'Input Field')
        self.assertEqual(self.control.resource_element.hint, 'Standard input field')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control.resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'Michelle')
        self.assertEqual(self.control.default_value, 'Michelle')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('input'), 'John')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.input.label, 'Input Field')
        self.assertEqual(self.runner.form.input.value, 'John')
