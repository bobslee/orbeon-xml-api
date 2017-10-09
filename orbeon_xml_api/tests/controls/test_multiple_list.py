from . import CommonTestCase

from ..controls import SelectControl


class MultipleListTestCase(CommonTestCase):

    def setUp(self):
        super(MultipleListTestCase, self).setUp()
        self.control = self.builder.controls['multiple-list']

    def test_control(self):
        self.assertIsInstance(self.control, SelectControl)

        string = 'cat dog fish'
        listing = ['cat', 'dog', 'fish']

        self.assertEqual(self.control.decode(string), listing)
        self.assertEqual(self.control.encode(listing), string)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'multiple-list-bind')
        self.assertEqual(self.control.bind.name, 'multiple-list')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.resource_element.label, 'Selection Controls')

    def test_builder_element(self):
        self.assertEqual(self.control.resource_element.label, 'Scrollable Checkboxes')
        self.assertEqual(self.control.resource_element.hint, 'Scrollable selector with checkboxes')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control.resource_element.alert, None)

        self.assertEqual(self.control.label, 'Scrollable Checkboxes')
        self.assertEqual(self.control.hint, 'Scrollable selector with checkboxes')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'cat bird')
        self.assertEqual(self.control.default_value, ['cat', 'bird'])

    def test_runner_value(self):
        self.assertEqual(self.runner.get_raw_value('multiple-list'), 'dog fish')
        self.assertEqual(self.runner.get_value('multiple-list'), ['dog', 'fish'])

    def test_runner_form(self):
        self.assertEqual(self.runner.form.multiplelist.label, 'Scrollable Checkboxes')
        self.assertEqual(self.runner.form.multiplelist.choices_values, ['dog', 'fish'])
        self.assertEqual(self.runner.form.multiplelist.choices_labels, ['Dog', 'Fish'])
        self.assertEqual(self.runner.form.multiplelist.choices, {'Dog': 'dog', 'Fish': 'fish'})
