from . import CommonTestCase

from ..controls import StringControl


class AutocompleteTestCase(CommonTestCase):

    def setUp(self):
        super(AutocompleteTestCase, self).setUp()
        self.control = self.builder.controls['autocomplete']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'autocomplete-bind')
        self.assertEqual(self.control.bind.name, 'autocomplete')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Autocomplete')
        self.assertEqual(self.control.element.hint, 'Enter the name of a country')
        self.assertEqual(self.control.element.alert, None)

        self.assertEqual(self.control.label, 'Autocomplete')
        self.assertEqual(self.control.hint, 'Enter the name of a country')
        self.assertEqual(self.control.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'us')
        self.assertEqual(self.control.default_value, 'us')

    def test_runner_form(self):
        self.assertEqual(self.runner.get_value('autocomplete'), 'nl')
        self.assertEqual(self.runner.form.autocomplete.value, 'nl')
