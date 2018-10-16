# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from . import CommonTestCase

from ..controls import AnyUriControl


class ImageAttachmentTestCase(CommonTestCase):

    def setUp(self):
        super(ImageAttachmentTestCase, self).setUp()
        self.control = self.builder.controls['image-attachment']
        self.image_attachment_value = '/fr/service/persistence/crud/orbeon/runner/data/24/79novacode17.bin'

    def test_control(self):
        self.assertIsInstance(self.control, AnyUriControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'image-attachment-bind')
        self.assertEqual(self.control._bind.name, 'image-attachment')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'attachment-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'attachment-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Image and File Attachments')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Image Attachment')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Image Attachment')
        self.assertEqual(self.control._resource_element.hint, None)
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value.text, None)
        self.assertEqual(self.control.default_value['uri'], None)
        # self.assertEqual(self.control.default_value['element']['@filename'], '')
        # self.assertEqual(self.control.default_value['element']['@mediatype'], '')
        # self.assertEqual(self.control.default_value['element']['@size'], '')

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('image-attachment')['element']['@filename'], 'feature-fr-browser.png')
        self.assertEqual(self.runner.get_value('image-attachment')['element']['@mediatype'], 'image/png')
        self.assertEqual(self.runner.get_value('image-attachment')['element']['@size'], '128457')

    def test_runner_form(self):
        self.assertEqual(self.runner.form.imageattachment.label, 'Image Attachment')
        self.assertEqual(self.runner.form.imageattachment.value, self.image_attachment_value)
        self.assertEqual(self.runner.form.imageattachment.uri, self.image_attachment_value)
        # self.assertEqual(self.runner.form.imageattachment.filename, 'feature-fr-browser.png')
        self.assertEqual(self.runner.form.imageattachment.raw_value, self.image_attachment_value)
                
