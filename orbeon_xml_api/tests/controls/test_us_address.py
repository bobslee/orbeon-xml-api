# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase


class UsAddressTestCase(CommonTestCase):

    def test_us_address(self):
        us_address = self.builder.controls['us-address']
        self.assertEqual(us_address._resource_element.label, 'US Address Template')
        self.assertEqual(us_address._resource_element.hint, None)
