from . import CommonTestCase

from ..controls import BooleanControl


class YesnoInputTestCase(CommonTestCase):

    def setUp(self):
        super(YesnoInputTestCase, self).setUp()
        self.control = self.builder.controls['yesno-input']

    def test_control(self):
        self.assertIsInstance(self.control, BooleanControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'yesno-input-bind')
        self.assertEqual(self.control._bind.name, 'yesno-input')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'selection-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'selection-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Yes/No Answer')
        self.assertEqual(self.control._resource_element.hint, None)

        self.assertEqual(self.control.label, 'Yes/No Answer')
        self.assertEqual(self.control.hint, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'false')
        self.assertEqual(self.control.default_value, False)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_raw_value('yesno-input').text, 'true')
        self.assertEqual(self.runner.get_value('yesno-input'), True)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.yesnoinput.label, 'Yes/No Answer')
        self.assertEqual(self.runner.form.yesnoinput.choice_label, 'Yes')
        self.assertEqual(self.runner.form.yesnoinput.choice_value, True)
        self.assertEqual(self.runner.form.yesnoinput.choice, {'Yes': True})
