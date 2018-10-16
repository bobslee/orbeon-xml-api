# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from datetime import datetime
from lxml import etree

from . import CommonTestCase
from ..controls import DateTimeControl


class DateTimeTestCase(CommonTestCase):

    def setUp(self):
        super(DateTimeTestCase, self).setUp()
        self.control = self.builder.controls['datetime']

    def test_control(self):
        self.assertIsInstance(self.control, DateTimeControl)

        dt_obj = datetime.strptime('2017-07-01T17:48:03', '%Y-%m-%dT%H:%M:%S')

        el = etree.Element('test')
        el.text = '2017-07-01T17:48:03'

        self.assertEqual(self.control.encode(dt_obj), '2017-07-01T17:48:03')
        self.assertEqual(self.control.decode(el), dt_obj)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'datetime-bind')
        self.assertEqual(self.control._bind.name, 'datetime')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Date and Time')
        self.assertEqual(self.control._resource_element.hint, 'Standard date and time field')
        self.assertEqual(self.control._resource_element.alert, None)

        # Shortcut via element
        self.assertEqual(self.control.label, 'Date and Time')
        self.assertEqual(self.control.hint, 'Standard date and time field')
        self.assertEqual(self.control.alert, None)

    def test_builder_form_default_value(self):
        dt_obj = datetime.strptime('2009-10-16T17:48:03', '%Y-%m-%dT%H:%M:%S')

        self.assertEqual(self.control.default_raw_value, '2009-10-16T17:48:03')
        self.assertEqual(self.control.default_value, dt_obj)

    def test_runner_value(self):
        dt_obj = datetime.strptime('2017-07-01T23:22:21', '%Y-%m-%dT%H:%M:%S')
        self.assertEqual(self.runner.get_value('datetime'), dt_obj)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.datetime.label, 'Date and Time')

        dt_obj = datetime.strptime('2017-07-01T23:22:21', '%Y-%m-%dT%H:%M:%S')
        self.assertEqual(self.runner.form.datetime.value, dt_obj)
        self.assertEqual(self.runner.form.datetime.raw_value, '2017-07-01T23:22:21')
