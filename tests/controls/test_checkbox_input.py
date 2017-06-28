from . import CommonTestCase


class CheckboxInputTestCase(CommonTestCase):

    def test_checkbox_input(self):
        checkbox_input = self.builder.controls['checkbox-input']
        self.assertEqual(checkbox_input.element.label, 'Single Checkbox')
        self.assertEqual(checkbox_input.element.hint, 'An input which captures "true" or "false"')
