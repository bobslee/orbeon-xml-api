from . import CommonTestCase


class InputCounterTestCase(CommonTestCase):

    def test_input_counter(self):
        input_counter = self.builder.controls['input-counter']

        self.assertEqual(input_counter.label, 'Input Field with Character Counter')
        self.assertEqual(input_counter.alert, '30 characters maximum')
        self.assertEqual(input_counter.hint, None)
        self.assertEqual(input_counter.default_value, 'This must not be "too long"!')

        self.assertEqual(input_counter.element.label, 'Input Field with Character Counter')
        self.assertEqual(input_counter.element.alert, '30 characters maximum')
        self.assertEqual(input_counter.element.hint, None)
