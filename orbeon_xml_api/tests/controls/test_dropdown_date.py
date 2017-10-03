from datetime import datetime

from . import CommonTestCase
from ..controls import DateControl


class DropdownDateTestCase(CommonTestCase):

    def setUp(self):
        super(DropdownDateTestCase, self).setUp()
        self.control = self.builder.controls['dropdown-date']

    def test_control(self):
        self.assertIsInstance(self.control, DateControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'dropdown-date-bind')
        self.assertEqual(self.control.bind.name, 'dropdown-date')

    def test_builder_form(self):
        self.assertEqual(self.control.element.label, 'Dropdown Date')
        self.assertEqual(self.control.element.hint, 'Date selector with dropdown menus')
        self.assertEqual(self.control.element.alert, None)

    def test_builder_form_default_value(self):
        dt_obj = datetime.strptime('2009-10-16', '%Y-%m-%d').date()

        self.assertEqual(self.control.default_raw_value, '2009-10-16')
        self.assertEqual(self.control.default_value, dt_obj)

    def test_runner_form(self):
        dt_obj = datetime.strptime('2017-07-01', '%Y-%m-%d').date()

        self.assertEqual(self.runner.get_value('dropdown-date'), dt_obj)
        self.assertEqual(self.runner.form.dropdowndate.value, dt_obj)
