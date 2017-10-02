from . import CommonTestCase


class DropdownTestCase(CommonTestCase):

    # TODO item(s) see itemset on control
    def test_dropdown(self):
        dropdown = self.builder.controls['dropdown']
        self.assertEqual(dropdown.element.label, 'Dropdown Menu')
        self.assertEqual(dropdown.element.hint, 'Standard dropdown')
