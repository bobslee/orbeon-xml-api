from . import CommonTestCase


class MultipleListTestCase(CommonTestCase):

    # TODO item(s) see itemset on control
    def test_multiple_list(self):
        multiple_list = self.builder.controls['multiple-list']
        self.assertEqual(multiple_list.element.label, 'Scrollable Checkboxes')
        self.assertEqual(multiple_list.element.hint, 'Scrollable selector with checkboxes')
