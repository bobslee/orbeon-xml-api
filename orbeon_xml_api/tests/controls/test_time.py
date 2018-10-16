# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from datetime import datetime
from lxml import etree

from . import CommonTestCase
from ..controls import TimeControl


class TimeTestCase(CommonTestCase):

    def setUp(self):
        super(TimeTestCase, self).setUp()
        self.control = self.builder.controls['time']

    def test_control(self):
        self.assertIsInstance(self.control, TimeControl)

        time_obj = datetime.strptime('17:47:57', '%H:%M:%S').time()

        el = etree.Element('test')
        el.text = '17:47:57'

        self.assertEqual(self.control.decode(el), time_obj)
        self.assertEqual(self.control.encode(time_obj), '17:47:57')

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'time-bind')
        self.assertEqual(self.control._bind.name, 'time')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'date-time-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'date-time-controls')

        self.assertEqual(self.control._parent.label, 'Date and Time')
        self.assertEqual(self.control._parent._resource_element.label, 'Date and Time')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Time')
        self.assertEqual(self.control._resource_element.hint, 'Standard time field')
        self.assertEqual(self.control._resource_element.alert, None)

        # Shortcut via element
        self.assertEqual(self.control.label, 'Time')
        self.assertEqual(self.control.hint, 'Standard time field')
        self.assertEqual(self.control.alert, None)

    def test_builder_form_default_value(self):
        time_obj = datetime.strptime('17:47:57', '%H:%M:%S').time()

        self.assertEqual(self.control.default_raw_value, '17:47:57')
        self.assertEqual(self.control.default_value, time_obj)

    def test_runner_value(self):
        time_obj = datetime.strptime('08:15:01', '%H:%M:%S').time()

        self.assertEqual(self.runner.get_value('time'), time_obj)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.time.label, 'Time')

        time_obj = datetime.strptime('08:15:01', '%H:%M:%S').time()
        self.assertEqual(self.runner.form.time.value, time_obj)
        self.assertEqual(self.runner.form.time.raw_value, '08:15:01')
