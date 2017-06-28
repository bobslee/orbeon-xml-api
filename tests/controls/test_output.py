from . import CommonTestCase


class OutputTestCase(CommonTestCase):

    def test_output(self):
        _output = self.builder.controls['output']

        self.assertEqual(_output.label, 'Text Output')
        self.assertEqual(_output.hint, None)
        self.assertEqual(_output.alert, None)
        self.assertEqual(_output.default_value, 'Great love and great achievements involve great risk.')

        self.assertEqual(_output.element.label, 'Text Output')
        self.assertEqual(_output.element.hint, None)
        self.assertEqual(_output.element.alert, None)
