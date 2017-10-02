from . import CommonTestCase


class DynamicDataDropdownTestCase(CommonTestCase):

    def test_dynamic_data_dropdown(self):
        dynamic_data_dropdown = self.builder.controls['dynamic-data-dropdown']
        self.assertEqual(dynamic_data_dropdown.element.label, 'Dynamic Data Dropdown')
        self.assertEqual(dynamic_data_dropdown.element.hint, None)
