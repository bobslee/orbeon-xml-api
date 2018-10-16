# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase

from ..controls import StringControl


class DynamicDataDropdownTestCase(CommonTestCase):

    def setUp(self):
        super(DynamicDataDropdownTestCase, self).setUp()
        self.control = self.builder.controls['dynamic-data-dropdown']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'dynamic-data-dropdown-bind')
        self.assertEqual(self.control._bind.name, 'dynamic-data-dropdown')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'selection-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'selection-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Dynamic Data Dropdown')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Dynamic Data Dropdown')
        self.assertEqual(self.control._resource_element.hint, None)

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'ca')
        self.assertEqual(self.control.default_value, 'ca')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('dynamic-data-dropdown'), 'de')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.dynamicdatadropdown.label, 'Dynamic Data Dropdown')
        self.assertEqual(self.runner.form.dynamicdatadropdown.value, 'de')
        self.assertEqual(self.runner.form.dynamicdatadropdown.raw_value, 'de')
