from . import CommonTestCase


class TextareaCounterTestCase(CommonTestCase):

    def test_textarea_counter(self):
        textarea_counter = self.builder.controls['textarea-counter']

        self.assertEqual(textarea_counter.element.label, 'Text Area with Character counter')
        self.assertEqual(textarea_counter.element.alert, '140 characters at most')
        self.assertEqual(textarea_counter.element.hint, None)

        self.assertEqual(textarea_counter.default_value, "Let's write a Tweet. It must fit in 140 characters.")
