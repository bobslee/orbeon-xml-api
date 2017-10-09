from . import CommonTestCase


class UsAddressTestCase(CommonTestCase):

    def test_us_address(self):
        us_address = self.builder.controls['us-address']
        self.assertEqual(us_address.resource_element.label, 'US Address Template')
        self.assertEqual(us_address.resource_element.hint, None)
