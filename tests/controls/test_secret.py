from . import CommonTestCase


class SecretTestCase(CommonTestCase):

    def test_secret(self):
        secret = self.builder.controls['secret']

        self.assertEqual(secret.label, 'Password Field')
        self.assertEqual(secret.hint, 'The password is 42 ;)')
        self.assertEqual(secret.alert, None)
        self.assertEqual(secret.default_value, '42')

        self.assertEqual(secret.element.label, 'Password Field')
        self.assertEqual(secret.element.hint, 'The password is 42 ;)')
        self.assertEqual(secret.element.alert, None)
