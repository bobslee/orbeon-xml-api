from . import CommonTestCase


class LinkButtonTestCase(CommonTestCase):

    def test_link_button(self):
        link_button = self.builder.controls['link-button']
        self.assertEqual(link_button.element.label, 'Link Button')
        self.assertEqual(link_button.element.hint, 'Button as a link')
