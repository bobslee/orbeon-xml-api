from . import CommonTestCase


class TimeTestCase(CommonTestCase):

    def test_time(self):
        time_control = self.builder.controls['time']
        self.assertEqual(time_control.element.label, 'Time')
        self.assertEqual(time_control.element.hint, 'Standard time field')
        self.assertEqual(time_control.element.alert, None)

    def test_time_bind(self):
        time_control = self.builder.controls['time']

        self.assertEqual(time_control.bind.id, 'time-bind')
        self.assertEqual(time_control.bind.name, 'time')

    def test_time_parent(self):
        time_control = self.builder.controls['time']

        self.assertEqual(time_control.parent.bind.id, 'date-time-controls-bind')
        self.assertEqual(time_control.parent.bind.name, 'date-time-controls')

        self.assertEqual(time_control.parent.label, 'Date and Time')
        self.assertEqual(time_control.parent.element.label, 'Date and Time')
