from . import CommonTestCase


class HtmlareaTestCase(CommonTestCase):

    def test_htmlarea(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea.label, 'Formatted Text')
        self.assertEqual(htmlarea.hint, 'Rich text editor')
        self.assertEqual(htmlarea.alert, None)
        self.assertIn('Giuseppe Fortunino Francesco Verdi', htmlarea.default_value)

        self.assertEqual(htmlarea.element.label, 'Formatted Text')
        self.assertEqual(htmlarea.element.hint, 'Rich text editor')

        # Doesn't exist, but shouldn't raise Exception
        self.assertEqual(htmlarea.element.alert, None)

    def test_htmlarea_bind(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea.bind.id, 'htmlarea-bind')
        self.assertEqual(htmlarea.bind.name, 'htmlarea')

    def test_htmlarea_parent(self):
        htmlarea = self.builder.controls['htmlarea']

        self.assertEqual(htmlarea.parent.bind.id, 'text-controls-bind')
        self.assertEqual(htmlarea.parent.bind.name, 'text-controls')
        self.assertEqual(htmlarea.parent.element.label, 'Text Controls')
