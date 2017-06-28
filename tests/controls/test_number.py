from . import CommonTestCase


class NumberTestCase(CommonTestCase):

    def test_number(self):
        number = self.builder.controls['number']
        self.assertEqual(number.element.label, 'Number')
        self.assertEqual(number.element.hint, 'Number field with validation')
