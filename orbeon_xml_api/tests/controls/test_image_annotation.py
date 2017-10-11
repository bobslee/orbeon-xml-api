from collections import OrderedDict
from lxml import etree

from . import CommonTestCase

from ..controls import ImageAnnotationControl


class ImageAnnotationTestCase(CommonTestCase):

    def setUp(self):
        super(ImageAnnotationTestCase, self).setUp()
        self.control = self.builder.controls['image-annotation']

        # Builder expected data
        self.builder_image_expected = OrderedDict()
        self.builder_image_expected['@filename'] = "feature-fb-browser-3.png"
        self.builder_image_expected['@mediatype'] = "image/png"
        self.builder_image_expected['@size'] = "107471"
        self.builder_image_expected['#text'] = '/fr/service/persistence/crud/orbeon/builder/data/33/e7d493a347aa07c871fe3cb7fce3393945e9d090.bin'

        self.builder_annotation_expected = '/fr/service/persistence/crud/orbeon/builder/data/33/950ec69749c8d1960f1f57339685c7fd13d3e099.bin'

        # Runner expected data
        self.runner_image_expected = OrderedDict()
        self.runner_image_expected['@filename'] = "feature-fr-browser.png"
        self.runner_image_expected['@mediatype'] = "image/png"
        self.runner_image_expected['@size'] = "128457"
        self.runner_image_expected['#text'] = '/fr/service/persistence/crud/orbeon/runner/data/24/79novacode17.bin'

        self.runner_annotation_expected = '/fr/service/persistence/crud/orbeon/runner/data/24/17novacode79.bin'

    def test_control(self):
        self.assertIsInstance(self.control, ImageAnnotationControl)

    def test_builder_bind(self):
        self.assertEqual(self.control._bind.id, 'image-annotation-bind')
        self.assertEqual(self.control._bind.name, 'image-annotation')

    def test_builder_parent(self):
        self.assertEqual(self.control._parent._bind.id, 'attachment-controls-bind')
        self.assertEqual(self.control._parent._bind.name, 'attachment-controls')
        self.assertEqual(self.control._parent._resource_element.label, 'Image and File Attachments')

    def test_builder_form(self):
        self.assertEqual(self.control.label, 'Image Annotation')
        self.assertEqual(self.control.hint, None)
        self.assertEqual(self.control.alert, None)

        self.assertEqual(self.control._resource_element.label, 'Image Annotation')
        self.assertEqual(self.control._resource_element.hint, None)
        self.assertEqual(self.control._resource_element.alert, None)

    def test_builder_form_default_value(self):
        self.assertEqual(self.control.default_raw_value.__class__.__name__, '_Element')
        self.assertEqual(self.control.default_value['image']['image']['@filename'], self.builder_image_expected['@filename'])
        self.assertEqual(self.control.default_value['annotation']['annotation']['#text'], self.builder_annotation_expected)

    def test_runner_value(self):
        ia = self.runner.get_value('image-annotation')

        self.assertDictEqual(ia['image']['image'], self.runner_image_expected)
        self.assertEqual(ia['annotation']['annotation'], self.runner_annotation_expected)

    def test_runner_form(self):
        self.assertEqual(self.runner.form.imageannotation.label, 'Image Annotation')
        self.assertEqual(self.runner.form.imageannotation.image, self.runner_image_expected)
        self.assertEqual(self.runner.form.imageannotation.annotation, self.runner_annotation_expected)
