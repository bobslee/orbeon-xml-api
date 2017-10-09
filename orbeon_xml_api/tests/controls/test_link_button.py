from . import CommonTestCase


class LinkButtonTestCase(CommonTestCase):

    def test_link_button(self):
        link_button = self.builder.controls['link-button']
        self.assertEqual(link_button.resource_element.label, 'Link Button')
        self.assertEqual(link_button.resource_element.hint, 'Button as a link')
