from datetime import datetime
from lxml import etree

from . import CommonTestCase
from ..controls import DateControl


class DateTestCase(CommonTestCase):

    def setUp(self):
        super(DateTestCase, self).setUp()
        self.control = self.builder.controls['date']

    def test_control(self):
        self.assertIsInstance(self.control, DateControl)

        date_obj = datetime.strptime('2009-10-16', '%Y-%m-%d').date()

        el = etree.Element('test')
        el.text = '2009-10-16'

        self.assertEqual(self.control.encode(date_obj), '2009-10-16')
        self.assertEqual(self.control.decode(el), date_obj)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'date-bind')
        self.assertEqual(self.control._bind.name, 'date')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'date-time-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'date-time-controls')

        self.assertEqual(self.control._parent.label, 'Date and Time')
        self.assertEqual(self.control._parent._resource_element.label, 'Date and Time')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Date')
        self.assertEqual(self.control._resource_element.hint, 'Standard date field')
        self.assertEqual(self.control._resource_element.alert, None)

        # Shortcut via element
        self.assertEqual(self.control.label, 'Date')
        self.assertEqual(self.control.hint, 'Standard date field')
        self.assertEqual(self.control.alert, None)

    def test_builder_form_default_value(self):
        date_obj = datetime.strptime('2009-10-16', '%Y-%m-%d').date()

        self.assertEqual(self.control.default_raw_value, '2009-10-16')
        self.assertEqual(self.control.default_value, date_obj)

    def test_runner_value(self):
        date_obj = datetime.strptime('2017-07-01', '%Y-%m-%d').date()

        self.assertEqual(self.runner.get_value('date'), date_obj)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.date.label, 'Date')

        date_obj = datetime.strptime('2017-07-01', '%Y-%m-%d').date()
        self.assertEqual(self.runner.form.date.value, date_obj)
