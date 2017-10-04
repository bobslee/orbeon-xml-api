from . import CommonTestCase
from ..controls import OpenSelect1Control


class OpenSelect1TestCase(CommonTestCase):

    def setUp(self):
        super(OpenSelect1TestCase, self).setUp()
        self.control = self.builder.controls['open-select1']

    def test_control(self):
        self.assertIsInstance(self.control, OpenSelect1Control)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'open-select1-bind')
        self.assertEqual(self.control.bind.name, 'open-select1')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Ice Cream Flavor')
        self.assertEqual(self.control.element.hint, None)

        self.assertEqual(self.control.label, 'Ice Cream Flavor')
        self.assertEqual(self.control.hint, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'Pistachio')
        self.assertEqual(self.control.default_value, 'Pistachio')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_raw_value('open-select1'), 'Pistachio')
        self.assertEqual(self.runner.get_value('open-select1'), 'Pistachio')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.openselect1.label, 'Ice Cream Flavor')
        self.assertEqual(self.runner.form.openselect1.choice_value, 'Pistachio')
        self.assertEqual(self.runner.form.openselect1.choice_label, 'Pistachio')
        self.assertEqual(self.runner.form.openselect1.choice, {'Pistachio': 'Pistachio'})
