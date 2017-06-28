from . import CommonTestCase


class RadioButtonsTestCase(CommonTestCase):

    # TODO item(s) see itemset on control
    def test_radio_buttons(self):
        radio_buttons = self.builder.controls['radio-buttons']
        self.assertEqual(radio_buttons.element.label, 'Radio Buttons')
        self.assertEqual(radio_buttons.element.hint, 'Standard radio buttons')
