from . import CommonTestCase

from orbeon_xml_api.controls import Select1Control


class RadioButtonsTestCase(CommonTestCase):

    def setUp(self):
        super(RadioButtonsTestCase, self).setUp()
        self.control = self.builder.controls['radio-buttons']

    def test_control(self):
        self.assertIsInstance(self.control, Select1Control)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'radio-buttons-bind')
        self.assertEqual(self.control.bind.name, 'radio-buttons')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'selection-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'selection-controls')
        self.assertEqual(self.control.parent.element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Radio Buttons')
        self.assertEqual(self.control.element.hint, 'Standard radio buttons')

        self.assertEqual(self.control.label, 'Radio Buttons')
        self.assertEqual(self.control.hint, 'Standard radio buttons')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'cat')
        self.assertEqual(self.control.default_value, 'cat')

    def test_runner_form(self):
        self.assertEqual(self.runner.get_value('radio-buttons'), 'dog')
        self.assertEqual(self.runner.form.radiobuttons, 'dog')
