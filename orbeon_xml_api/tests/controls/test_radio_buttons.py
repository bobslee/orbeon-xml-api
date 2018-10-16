# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase

from ..controls import Select1Control


class RadioButtonsTestCase(CommonTestCase):

    def setUp(self):
        super(RadioButtonsTestCase, self).setUp()
        self.control = self.builder.controls['radio-buttons']

    def test_control(self):
        self.assertIsInstance(self.control, Select1Control)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'radio-buttons-bind')
        self.assertEqual(self.control._bind.name, 'radio-buttons')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'selection-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'selection-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Selection Controls')

    def test_builder_form(self):
        self.assertEqual(self.control._resource_element.label, 'Radio Buttons')
        self.assertEqual(self.control._resource_element.hint, 'Standard radio buttons')

        self.assertEqual(self.control.label, 'Radio Buttons')
        self.assertEqual(self.control.hint, 'Standard radio buttons')

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, 'cat')
        self.assertEqual(self.control.default_value, 'cat')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('radio-buttons'), 'dog')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.radiobuttons.label, 'Radio Buttons')
        self.assertEqual(self.runner.form.radiobuttons.choice_value, 'dog')
        self.assertEqual(self.runner.form.radiobuttons.choice_label, 'Dog')
        self.assertEqual(self.runner.form.radiobuttons.choice, {'Dog': 'dog'})
