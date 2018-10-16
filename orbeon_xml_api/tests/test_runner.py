# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from xmlunittest import XmlTestCase

from .test_common import CommonTestCase
from ..runner import Runner, RunnerForm
from ..utils import xml_from_file


class RunnerTestCase(CommonTestCase, XmlTestCase):

    def setUp(self):
        super(RunnerTestCase, self).setUp()

        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')
        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')

        self.runner = Runner(self.runner_xml, None, self.builder_xml)

    def test_constructor_validation_ok(self):
        runner = Runner(self.runner_xml, None, self.builder_xml)
        self.assertIsInstance(runner, Runner)

        runner = Runner(self.runner_xml, self.builder)
        self.assertIsInstance(runner, Runner)
        self.assertIsInstance(self.runner.form, RunnerForm)

    def test_constructor_validation_fails(self):
        with self.assertRaisesRegexp(Exception, "Provide either the argument: builder or builder_xml."):
            Runner(self.runner_xml)

        with self.assertRaisesRegexp(Exception, "Constructor accepts either builder or builder_xml."):
            Runner(self.runner_xml, self.builder, self.builder_xml)
