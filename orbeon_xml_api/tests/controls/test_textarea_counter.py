from . import CommonTestCase

from ..controls import StringControl


class TextareaCounterTestCase(CommonTestCase):

    def setUp(self):
        super(TextareaCounterTestCase, self).setUp()
        self.control = self.builder.controls['textarea-counter']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'textarea-counter-bind')
        self.assertEqual(self.control._bind.name, 'textarea-counter')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Text Area with Character counter')
        self.assertEqual(self.control._resource_element.alert, '140 characters at most')
        self.assertEqual(self.control._resource_element.hint, None)

        self.assertEqual(self.control.default_value, "Let's write a Tweet. It must fit in 140 characters.")

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, "Let's write a Tweet. It must fit in 140 characters.")
        self.assertEqual(self.control.default_value, "Let's write a Tweet. It must fit in 140 characters.")

    def test_runner_value(self):
        text = "Let's write some code. It must fit in 1000 bytes."
        self.assertEqual(self.runner.get_value('textarea-counter'), text)

    def test_runner_form(self):
        text = "Let's write some code. It must fit in 1000 bytes."
        self.assertEqual(self.runner.form.textareacounter.label, 'Text Area with Character counter')
        self.assertEqual(self.runner.form.textareacounter.value, text)
        self.assertEqual(self.runner.form.textareacounter.raw_value, text)
