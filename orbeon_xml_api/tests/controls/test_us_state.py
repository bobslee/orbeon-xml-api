from . import CommonTestCase


class UsStateTestCase(CommonTestCase):

    def test_us_state(self):
        us_state = self.builder.controls['us-state']
        self.assertEqual(us_state._resource_element.label, 'US State')
        self.assertEqual(us_state._resource_element.hint, 'US state selector')
