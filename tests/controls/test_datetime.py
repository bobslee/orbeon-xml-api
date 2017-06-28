from . import CommonTestCase


class DatetimeTestCase(CommonTestCase):

    def test_datetime(self):
        datetime_control = self.builder.controls['datetime']
        self.assertEqual(datetime_control.element.label, 'Date and Time')
        self.assertEqual(datetime_control.element.hint, 'Standard date and time field')
        self.assertEqual(datetime_control.element.alert, None)
