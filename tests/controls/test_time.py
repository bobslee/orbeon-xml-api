from datetime import datetime

from . import CommonTestCase
from orbeon_xml_api.controls import TimeControl


class TimeTestCase(CommonTestCase):

    def setUp(self):
        super(TimeTestCase, self).setUp()
        self.control = self.builder.controls['time']

    def test_control(self):
        self.assertIsInstance(self.control, TimeControl)

        time_obj = datetime.strptime('17:47:57', '%H:%M:%S').time()

        self.assertEqual(self.control.encode(time_obj), '17:47:57')
        self.assertEqual(self.control.decode('17:47:57'), time_obj)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'time-bind')
        self.assertEqual(self.control.bind.name, 'time')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'date-time-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'date-time-controls')

        self.assertEqual(self.control.parent.label, 'Date and Time')
        self.assertEqual(self.control.parent.element.label, 'Date and Time')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Time')
        self.assertEqual(self.control.element.hint, 'Standard time field')
        self.assertEqual(self.control.element.alert, None)

        # Shortcut via element
        self.assertEqual(self.control.label, 'Time')
        self.assertEqual(self.control.hint, 'Standard time field')
        self.assertEqual(self.control.alert, None)

    def test_builder_form_default_value(self):
        time_obj = datetime.strptime('17:47:57', '%H:%M:%S').time()

        self.assertEqual(self.control.default_raw_value, '17:47:57')
        self.assertEqual(self.control.default_value, time_obj)

    def test_runner_form(self):
        time_obj = datetime.strptime('08:15:01', '%H:%M:%S').time()

        self.assertEqual(self.runner.get_value('time'), time_obj)
        self.assertEqual(self.runner.form.time, time_obj)
