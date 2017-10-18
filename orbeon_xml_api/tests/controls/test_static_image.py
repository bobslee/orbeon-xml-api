from collections import OrderedDict
from . import CommonTestCase

from ..controls import AnyUriControl


class StaticImageTestCase(CommonTestCase):

    def setUp(self):
        super(StaticImageTestCase, self).setUp()
        self.control = self.builder.controls['static-image']

    def test_control(self):
        self.assertIsInstance(self.control, AnyUriControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'static-image-bind')
        self.assertEqual(self.control._bind.name, 'static-image')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'attachment-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'attachment-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Image and File Attachments')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Static Image')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Static Image')
        self.assertEqual(self.control._resource_element.hint, None)
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        value = {
            'uri': '/fr/service/persistence/crud/orbeon/builder/data/33/a8523db8eba50aac53dfe15ece2758e6475cfc21.bin',
            'value': '/fr/service/persistence/crud/orbeon/builder/data/33/a8523db8eba50aac53dfe15ece2758e6475cfc21.bin'
        }

        self.assertEqual(self.control.default_raw_value.__class__.__name__, '_Element')
        # self.assertDictEqual(self.control.default_value, value)

    def test_runner_value(self):

        element = OrderedDict()
        element['@filename'] = "feature-fr-browser-3.png"
        element['@mediatype'] = "image/png"
        element['#text'] = '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin'

        value = {
            'uri': '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin',
            'value': '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin',
            'element': element
        }

        self.assertDictEqual(self.runner.get_value('static-image'), value)

    def test_runner_form(self):
        value = {
            'uri': '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin',
            'value': '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin'
        }

        self.assertEqual(self.runner.form.staticimage.label, 'Static Image')
        self.assertEqual(self.runner.form.staticimage.uri, value['uri'])
        self.assertEqual(self.runner.form.staticimage.value, value['value'])
        self.assertEqual(self.runner.form.staticimage.raw_value, value['value'])
