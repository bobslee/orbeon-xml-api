from . import CommonTestCase

from ..controls import AnyURIControl


class ImageAttachmentTestCase(CommonTestCase):

    def setUp(self):
        super(ImageAttachmentTestCase, self).setUp()
        self.control = self.builder.controls['image-attachment']
        self.image_attachment_value = '/fr/service/persistence/crud/orbeon/runner/data/24/43dbaabe1e3aa8862fd4de321b619709d62cc097.bin'

    def test_control(self):
        self.assertIsInstance(self.control, AnyURIControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'image-attachment-bind')
        self.assertEqual(self.control.bind.name, 'image-attachment')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'attachment-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'attachment-controls')
        self.assertEqual(self.control.parent.resource_element.label, 'Image and File Attachments')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Image Attachment')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.resource_element.label, 'Image Attachment')
        self.assertEqual(self.control.resource_element.hint, None)
        self.assertEqual(self.control.resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, None)
        self.assertEqual(self.control.default_value, None)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('image-attachment'), self.image_attachment_value)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.imageattachment.label, 'Image Attachment')
        self.assertEqual(self.runner.form.imageattachment.value, self.image_attachment_value)
