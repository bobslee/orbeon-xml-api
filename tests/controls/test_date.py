from datetime import datetime

from . import CommonTestCase
from orbeon_xml_api.controls import DateControl, StringControl


class DateTestCase(CommonTestCase):

    def test_date(self):
        date_control = self.builder.controls['date']

        self.assertIsInstance(date_control, DateControl)
        self.assertEqual(date_control.label, 'Date')
        self.assertEqual(date_control.hint, 'Standard date field')
        self.assertEqual(date_control.alert, None)

        self.assertEqual(date_control.element.label, 'Date')
        self.assertEqual(date_control.element.hint, 'Standard date field')
        self.assertEqual(date_control.element.alert, None)

        self.assertEqual(date_control.default_raw_value, '2009-10-16')
        self.assertEqual(date_control.default_value, datetime.strptime('2009-10-16', '%Y-%m-%d').date())

    def test_date_bind(self):
        date_control = self.builder.controls['date']

        self.assertEqual(date_control.bind.id, 'date-bind')
        self.assertEqual(date_control.bind.name, 'date')

    def test_date_parent(self):
        date_control = self.builder.controls['date']

        self.assertEqual(date_control.parent.bind.id, 'date-time-controls-bind')
        self.assertEqual(date_control.parent.bind.name, 'date-time-controls')

        self.assertEqual(date_control.parent.label, 'Date and Time')
        self.assertEqual(date_control.parent.element.label, 'Date and Time')
