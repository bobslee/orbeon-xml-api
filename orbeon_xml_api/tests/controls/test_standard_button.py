# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase


class StandardButtonTestCase(CommonTestCase):

    def test_standard_button(self):
        standard_button = self.builder.controls['standard-button']
        self.assertEqual(standard_button._resource_element.label, 'Standard Button')
        self.assertEqual(standard_button._resource_element.hint, 'Standard browser button')
