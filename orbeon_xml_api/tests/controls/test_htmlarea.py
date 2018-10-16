# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase

from ..controls import StringControl


class HtmlareaTestCase(CommonTestCase):

    def setUp(self):
        super(HtmlareaTestCase, self).setUp()
        self.control = self.builder.controls['htmlarea']

    def test_control(self):
        self.assertIsInstance(self.control, StringControl)

    def test_builder_bind(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea._bind.id, 'htmlarea-bind')
        self.assertEqual(htmlarea._bind.name, 'htmlarea')

    def test_builder_parent(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea._parent._bind.id, 'text-controls-bind')
        self.assertEqual(htmlarea._parent._bind.name, 'text-controls')
        self.assertEqual(htmlarea._parent._resource_element.label, 'Text Controls')

    def test_builder_form(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea.label, 'Formatted Text')
        self.assertEqual(htmlarea.hint, 'Rich text editor')
        self.assertEqual(htmlarea.alert, None)
        self.assertIn('Giuseppe Fortunino Francesco Verdi', htmlarea.default_value)

        self.assertEqual(htmlarea._resource_element.label, 'Formatted Text')
        self.assertEqual(htmlarea._resource_element.hint, 'Rich text editor')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(htmlarea._resource_element.alert, None)

    def test_builder_form_default_value(self):
        re = '.*Giuseppe Fortunino Francesco Verdi.*'
        self.assertRegexpMatches(self.control.default_raw_value, re)
        self.assertRegexpMatches(self.control.default_value, re)

    def test_runner_value(self):
        re = '.*The Good, the Bad and the Ugly.*'
        self.assertRegexpMatches(self.runner.get_value('htmlarea'), re)

    def test_runner_form(self):
        self.assertRegexpMatches(self.runner.form.htmlarea.label, 'Formatted Text')

        re = '.*The Good, the Bad and the Ugly.*'
        self.assertRegexpMatches(self.runner.form.htmlarea.value, re)
        self.assertRegexpMatches(self.runner.form.htmlarea.raw_value, re)
