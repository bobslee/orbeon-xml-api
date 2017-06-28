from . import CommonTestCase


class AutocompleteTestCase(CommonTestCase):

    def test_autocomplete(self):
        autocomplete = self.builder.controls['autocomplete']
        self.assertEqual(autocomplete.element.label, 'Autocomplete')
        self.assertEqual(autocomplete.element.hint, 'Enter the name of a country')
        # TODO code (us-code?)
        # self.assertEqual(autocomplete.element.code, 'Country code')
        self.assertEqual(autocomplete.element.alert, None)
