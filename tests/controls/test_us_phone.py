from . import CommonTestCase


class UsPhoneTestCase(CommonTestCase):

    def test_us_phone(self):
        us_phone = self.builder.controls['us-phone']
        self.assertEqual(us_phone.element.label, 'US Phone Number')
        self.assertEqual(us_phone.element.hint, 'US phone number field')
