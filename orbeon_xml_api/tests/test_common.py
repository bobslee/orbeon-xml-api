# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import unittest
import re

from ..builder import Builder
from ..runner import Runner
from ..utils import xml_from_file

TEXT_CONTROLS_BIND = ['text-controls-bind', 'input-bind', 'htmlarea-bind', 'output-bind',
                      'secret-bind', 'input-counter-bind', 'textarea-bind', 'textarea-counter-bind',
                      'NC.no-copy-field-bind']

DATE_TIME_CONTROLS_BIND = ['date-time-controls-bind', 'date-bind', 'time-bind', 'datetime-bind',
                           'dropdown-date-bind', 'fields-date-bind']

SELECTION_CONTROLS_BIND = ['selection-controls-bind', 'autocomplete-bind', 'yesno-input-bind',
                           'checkbox-input-bind', 'radio-buttons-bind', 'open-select1-bind',
                           'dropdown-bind', 'dynamic-data-dropdown-bind', 'checkboxes-bind',
                           'multiple-list-bind']

# What about? image-attachments-iteration-bind
# ATTACHMENT_CONTROLS_BIND = ['attachment-controls-bind', 'image-attachments-bind',
#                             'image-attachments-iteration-bind', 'image-attachment-bind',
#                             'file-attachment-bind', 'static-image-bind']

ATTACHMENT_CONTROLS_BIND = ['attachment-controls-bind', 'image-attachment-bind', 'static-image-bind',
                            'image-annotation-bind']

BUTTONS_BIND = ['buttons-bind', 'standard-button-bind', 'link-button-bind']

TYPED_CONTROLS_BIND = ['typed-controls-bind', 'email-bind', 'currency-bind', 'us-phone-bind',
                       'number-bind', 'us-state-bind']

US_ADDRESS_BIND = ['us-address-bind']

BINDS = TEXT_CONTROLS_BIND + DATE_TIME_CONTROLS_BIND + SELECTION_CONTROLS_BIND + \
            ATTACHMENT_CONTROLS_BIND + BUTTONS_BIND + TYPED_CONTROLS_BIND + US_ADDRESS_BIND


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        super(CommonTestCase, self).setUp()

        self.maxDiff = None
        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')
        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')

        self.builder = Builder(self.builder_xml)
        self.runner = Runner(self.runner_xml, None, self.builder_xml)

        self.bind_names = BINDS
        self.control_names = self._set_control_names()

    def _set_control_names(self):
        return [re.sub(r'-bind$', '', b) for b in self.bind_names]
