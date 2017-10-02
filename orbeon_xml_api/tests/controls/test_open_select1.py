from . import CommonTestCase


class DropdownTestCase(CommonTestCase):

    # TODO item(s) see itemset on control
    def test_open_select1(self):
        open_select1 = self.builder.controls['open-select1']
        self.assertEqual(open_select1.element.label, 'Ice Cream Flavor')
        self.assertEqual(open_select1.element.hint, None)
