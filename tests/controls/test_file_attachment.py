from . import CommonTestCase


class FileAttachmentTestCase(CommonTestCase):

    def test_file_attachment(self):
        file_attachment = self.builder.controls['file-attachment']
        self.assertEqual(file_attachment.element.label, 'File Attachment')
        self.assertEqual(file_attachment.element.hint, None)
