from . import CommonTestCase


class StandardButtonTestCase(CommonTestCase):

    def test_standard_button(self):
        standard_button = self.builder.controls['standard-button']
        self.assertEqual(standard_button.element.label, 'Standard Button')
        self.assertEqual(standard_button.element.hint, 'Standard browser button')
