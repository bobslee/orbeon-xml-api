from . import CommonTestCase


class EmailTestCase(CommonTestCase):

    def test_email(self):
        email = self.builder.controls['email']
        self.assertEqual(email.element.label, 'Email Address')
        self.assertEqual(email.element.hint, 'Email field with validation')
