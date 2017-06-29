from datetime import datetime

from . import CommonTestCase
from orbeon_xml_api.controls import TimeControl


class TimeTestCase(CommonTestCase):

    def test_time(self):
        time_control = self.builder.controls['time']

        self.assertIsInstance(time_control, TimeControl)

        time_obj = datetime.strptime('17:47:57', '%H:%M:%S').time()

        self.assertEqual(time_control.encode(time_obj), '17:47:57')
        self.assertEqual(time_control.decode('17:47:57'), time_obj)

        self.assertEqual(time_control.default_raw_value, '17:47:57')
        self.assertEqual(time_control.default_value, time_obj)

    def test_time_bind(self):
        time_control = self.builder.controls['time']

        self.assertEqual(time_control.bind.id, 'time-bind')
        self.assertEqual(time_control.bind.name, 'time')

    def test_time_element(self):
        time_control = self.builder.controls['time']

        self.assertEqual(time_control.element.label, 'Time')
        self.assertEqual(time_control.element.hint, 'Standard time field')
        self.assertEqual(time_control.element.alert, None)

        # Shortcut via element
        self.assertEqual(time_control.label, 'Time')
        self.assertEqual(time_control.hint, 'Standard time field')
        self.assertEqual(time_control.alert, None)

    def test_time_parent(self):
        time_control = self.builder.controls['time']

        self.assertEqual(time_control.parent.bind.id, 'date-time-controls-bind')
        self.assertEqual(time_control.parent.bind.name, 'date-time-controls')

        self.assertEqual(time_control.parent.label, 'Date and Time')
        self.assertEqual(time_control.parent.element.label, 'Date and Time')
