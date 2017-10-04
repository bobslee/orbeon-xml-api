from . import CommonTestCase
from ..controls import Select1Control


class DropdownTestCase(CommonTestCase):

    def setUp(self):
        super(DropdownTestCase, self).setUp()
        self.control = self.builder.controls['dropdown']

    def test_control(self):
        self.assertIsInstance(self.control, Select1Control)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'dropdown-bind')
        self.assertEqual(self.control.bind.name, 'dropdown')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Dropdown Menu')
        self.assertEqual(self.control.element.hint, 'Standard dropdown')

        self.assertEqual(self.control.label, 'Dropdown Menu')
        self.assertEqual(self.control.hint, 'Standard dropdown')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'cat')
        self.assertEqual(self.control.default_value, 'cat')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_raw_value('dropdown'), 'bird')
        self.assertEqual(self.runner.get_value('dropdown'), 'bird')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.dropdown.label, 'Dropdown Menu')
        self.assertEqual(self.runner.form.dropdown.choice_value, 'bird')
        self.assertEqual(self.runner.form.dropdown.choice_label, 'Bird')
        self.assertEqual(self.runner.form.dropdown.choice, {'Bird': 'bird'})
