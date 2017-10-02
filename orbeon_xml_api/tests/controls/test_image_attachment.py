from . import CommonTestCase


class ImageAttachmentTestCase(CommonTestCase):

    def test_image_attachment(self):
        image_attachment = self.builder.controls['image-attachment']
        self.assertEqual(image_attachment.element.label, 'Image Attachment')
        self.assertEqual(image_attachment.element.hint, None)
