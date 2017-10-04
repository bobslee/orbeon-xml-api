from . import CommonTestCase
from ..controls import SelectControl


class CheckboxesTestCase(CommonTestCase):

    def setUp(self):
        super(CheckboxesTestCase, self).setUp()
        self.control = self.builder.controls['checkboxes']

    def test_control(self):
        self.assertIsInstance(self.control, SelectControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'checkboxes-bind')
        self.assertEqual(self.control.bind.name, 'checkboxes')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Checkboxes')
        self.assertEqual(self.control.element.hint, 'Standard checkboxes')

        self.assertEqual(self.control.label, 'Checkboxes')
        self.assertEqual(self.control.hint, 'Standard checkboxes')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'cat bird')
        self.assertEqual(self.control.default_value, ['cat', 'bird'])

    def test_runner_form(self):
        self.assertEqual(self.runner.get_raw_value('checkboxes'), 'dog fish')
        self.assertEqual(self.runner.get_value('checkboxes'), ['dog', 'fish'])

        self.assertEqual(self.runner.form.checkboxes.choice_values, ['dog', 'fish'])
        self.assertEqual(self.runner.form.checkboxes.choice_labels, ['Dog', 'Fish'])
        self.assertEqual(self.runner.form.checkboxes.choices, {'Dog': 'dog', 'Fish': 'fish'})
