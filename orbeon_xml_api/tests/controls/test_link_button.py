# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase


class LinkButtonTestCase(CommonTestCase):

    def test_link_button(self):
        link_button = self.builder.controls['link-button']
        self.assertEqual(link_button._resource_element.label, 'Link Button')
        self.assertEqual(link_button._resource_element.hint, 'Button as a link')
