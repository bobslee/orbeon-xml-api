from . import CommonTestCase

from ..controls import AnyURIControl


class StaticImageTestCase(CommonTestCase):

    def setUp(self):
        super(StaticImageTestCase, self).setUp()
        self.control = self.builder.controls['static-image']
        self.static_image_value = '/fr/service/persistence/crud/orbeon/builder/data/33/a8523db8eba50aac53dfe15ece2758e6475cfc21.bin'

    def test_control(self):
        self.assertIsInstance(self.control, AnyURIControl)

    def test_builder_bind(self):
        self.assertEqual(self.control.bind.id, 'static-image-bind')
        self.assertEqual(self.control.bind.name, 'static-image')

    def test_builder_parent(self):
        self.assertEqual(self.control.parent.bind.id, 'attachment-controls-bind')
        self.assertEqual(self.control.parent.bind.name, 'attachment-controls')
        self.assertEqual(self.control.parent.resource_element.label, 'Image and File Attachments')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Static Image')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control.resource_element.label, 'Static Image')
        self.assertEqual(self.control.resource_element.hint, None)
        self.assertEqual(self.control.resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value, self.static_image_value)
        self.assertEqual(self.control.default_value, self.static_image_value)

    def test_runner_value(self):
        self.assertEqual(self.runner.get_value('static-image'), self.static_image_value)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.staticimage.label, 'Static Image')
        self.assertEqual(self.runner.form.staticimage.value, self.static_image_value)
