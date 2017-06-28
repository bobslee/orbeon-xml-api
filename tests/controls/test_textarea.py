from . import CommonTestCase


class TextareaTestCase(CommonTestCase):

    def test_textarea(self):
        textarea = self.builder.controls['textarea']

        self.assertEqual(textarea.label, 'Text Area')
        self.assertEqual(textarea.hint, 'Standard text area')
        self.assertIn('Music is an art', textarea.default_value)
        self.assertEqual(textarea.alert, None)

        self.assertEqual(textarea.element.label, 'Text Area')
        self.assertEqual(textarea.element.hint, 'Standard text area')

        self.assertEqual(textarea.element.alert, None)
