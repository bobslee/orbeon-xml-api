from . import CommonTestCase


class DropdownTestCase(CommonTestCase):

    def test_fields_date(self):
        fields_date_control = self.builder.controls['fields-date']
        self.assertEqual(fields_date_control.element.label, 'Fields Date')
        self.assertEqual(fields_date_control.element.hint, 'Date selector with separate fields')
        self.assertEqual(fields_date_control.element.alert, None)
