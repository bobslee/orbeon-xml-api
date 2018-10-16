# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase


class UsStateTestCase(CommonTestCase):

    def test_us_state(self):
        us_state = self.builder.controls['us-state']
        self.assertEqual(us_state._resource_element.label, 'US State')
        self.assertEqual(us_state._resource_element.hint, 'US state selector')
