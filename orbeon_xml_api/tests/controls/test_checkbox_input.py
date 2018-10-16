# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase

from ..controls import BooleanControl


class CheckboxInputTestCase(CommonTestCase):

    def setUp(self):
        super(CheckboxInputTestCase, self).setUp()
        self.control = self.builder.controls['checkbox-input']

    def test_control(self):
        self.assertIsInstance(self.control, BooleanControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'checkbox-input-bind')
        self.assertEqual(self.control._bind.name, 'checkbox-input')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'selection-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'selection-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Single Checkbox')
        self.assertEqual(self.control._resource_element.hint, 'An input which captures "true" or "false"')

        self.assertEqual(self.control.label, 'Single Checkbox')
        self.assertEqual(self.control.hint, 'An input which captures "true" or "false"')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'false')
        self.assertEqual(self.control.default_value, False)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_raw_value('checkbox-input').text, 'true')
        self.assertEqual(self.runner.get_value('checkbox-input'), True)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.checkboxinput.label, 'Single Checkbox')
        self.assertEqual(self.runner.form.checkboxinput.choice_label, 'Yes')
        self.assertEqual(self.runner.form.checkboxinput.choice_value, True)
        self.assertEqual(self.runner.form.checkboxinput.choice, {'Yes': True})
