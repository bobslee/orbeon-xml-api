from . import CommonTestCase


class CurrencyTestCase(CommonTestCase):

    def test_currency(self):
        currency = self.builder.controls['currency']
        self.assertEqual(currency.element.label, 'Currency')
        self.assertEqual(currency.element.hint, 'Currency field')
