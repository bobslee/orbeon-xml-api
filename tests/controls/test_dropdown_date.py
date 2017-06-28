from . import CommonTestCase


class DropdownDateTestCase(CommonTestCase):

    def test_dropdown_date(self):
        dropdown_date = self.builder.controls['dropdown-date']
        self.assertEqual(dropdown_date.element.label, 'Dropdown Date')
        self.assertEqual(dropdown_date.element.hint, 'Date selector with dropdown menus')
        self.assertEqual(dropdown_date.element.alert, None)
