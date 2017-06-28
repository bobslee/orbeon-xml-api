from . import CommonTestCase


class CheckboxesTestCase(CommonTestCase):

    # TODO item(s) see itemset on control
    def test_checkboxes(self):
        checkboxes = self.builder.controls['checkboxes']
        self.assertEqual(checkboxes.element.label, 'Checkboxes')
        self.assertEqual(checkboxes.element.hint, 'Standard checkboxes')
