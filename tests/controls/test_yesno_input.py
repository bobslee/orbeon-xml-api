from . import CommonTestCase


class YesnoInputTestCase(CommonTestCase):

    def test_yesno_input(self):
        yesno_input = self.builder.controls['yesno-input']
        self.assertEqual(yesno_input.element.label, 'Yes/No Answer')
        self.assertEqual(yesno_input.element.hint, None)
