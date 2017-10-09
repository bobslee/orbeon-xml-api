from . import CommonTestCase


class StaticImageTestCase(CommonTestCase):

    def test_static_image(self):
        static_image = self.builder.controls['static-image']
        self.assertEqual(static_image.resource_element.label, 'Static Image')
        self.assertEqual(static_image.resource_element.hint, None)
