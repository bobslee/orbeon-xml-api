import unittest
import xmltodict
from datetime import datetime, timedelta
from lxml import etree

from ..controls import StringControl, DateControl, ImageAnnotationControl, AnyUriControl
from ..builder import Builder
from ..runner import Runner
from ..utils import xml_from_file


class ControlDecoderTestCase(unittest.TestCase):

    def setUp(self):
        super(ControlDecoderTestCase, self).setUp()

        self.builder_xml = xml_from_file('tests/data', 'test_controls_builder_no-image-attachments-iteration.xml')
        self.runner_xml = xml_from_file('tests/data', 'test_controls_runner_no-image-attachments-iteration.xml')

    def test_my_string_control(self):
        controls = {
            'StringControl': MyStringControl
        }
        self.builder = Builder(self.builder_xml, 'en', controls=controls)
        self.runner = Runner(self.runner_xml, self.builder)

        self.assertEqual(self.runner.form.input.value, 'John FROM MyStringControl')

    def test_my_multiple_controls(self):
        controls = {
            'StringControl': MyStringControl,
            'DateControl': MyDateControl
        }
        self.builder = Builder(self.builder_xml, 'en', controls=controls)
        self.runner = Runner(self.runner_xml, self.builder)

        self.assertEqual(self.runner.form.input.value, 'John FROM MyStringControl')

        date_obj_add_10_days = datetime.strptime('2017-07-11', '%Y-%m-%d').date()
        self.assertEqual(self.runner.form.date.value, date_obj_add_10_days)

    def test_my_image_annotation_control(self):
        controls = {
            'ImageAnnotationControl': MyImageAnnotationControl
        }
        self.builder = Builder(self.builder_xml, 'en', controls=controls)
        self.runner = Runner(self.runner_xml, self.builder)

        self.assertEqual(self.runner.form.imageannotation.image, 'image FROM MyImageAnnotationControl')
        self.assertEqual(self.runner.form.imageannotation.annotation, 'annotation FROM MyImageAnnotationControl')

    def test_my_static_image_control(self):
        controls = {
            'AnyUriControl': MyAnyUriStaticImageControl
        }
        self.builder = Builder(self.builder_xml, 'en', controls=controls)
        self.runner = Runner(self.runner_xml, self.builder)

        expected = "%s BY THE MyAnyUriStaticImageControl" % '/fr/service/persistence/crud/orbeon/runner/data/33/17novacode79.bin'

        self.assertEqual(self.runner.form.staticimage.uri, expected)
        self.assertEqual(self.runner.form.staticimage.value, expected)

    def test_my_image_attachment_control(self):
        controls = {
            'AnyUriControl': MyAnyUriImageAttachmentControl
        }
        self.builder = Builder(self.builder_xml, 'en', controls=controls)
        self.runner = Runner(self.runner_xml, self.builder)

        expected = "%s FROM MyAnyUriImageAttachmentControl" % '/fr/service/persistence/crud/orbeon/runner/data/24/79novacode17.bin'

        self.assertEqual(self.runner.form.imageattachment.uri, expected)
        self.assertEqual(self.runner.form.imageattachment.value, expected)


"""
My subclassed Controls
"""


class MyStringControl(StringControl):

    def __init__(self, builder, bind, element):
        super(MyStringControl, self).__init__(builder, bind, element)
        self.username = 'novacode'
        self.api_token = 'abc123'

    def decode(self, element):
        if hasattr(element, 'text'):
            new_value = "%s FROM %s" % (element.text, self.__class__.__name__)
            return new_value


class MyDateControl(DateControl):

    def decode(self, element):
        if element is None or not hasattr(element, 'text'):
            return
        return datetime.strptime(element.text, '%Y-%m-%d').date() + timedelta(days=10)


class MyImageAnnotationControl(ImageAnnotationControl):

    def decode(self, element):
        res = {}

        if element is None:
            return res

        for el in element.getchildren():
            res[el.tag] = {el.tag: "%s FROM %s" % (el.tag, self.__class__.__name__)}

        return res


class MyAnyUriStaticImageControl(AnyUriControl):

    def decode(self, element):
        res = {'uri': None, 'value': None}

        if element is None:
            return res

        if isinstance(element.text, basestring):
            return {
                'uri': "%s BY THE %s" % (element.text, self.__class__.__name__),
                'value': "%s BY THE %s" % (element.text, self.__class__.__name__)
            }
        # else:
        #     return {
        #         'uri': "%s BY THE %s" % (ele.text, self.__class__.__name__),
        #         'value': "%s BY THE %s" % (value.text, self.__class__.__name__)
        #     }


class MyAnyUriImageAttachmentControl(AnyUriControl):

    def decode(self, value):
        res = {'uri': None, 'value': None}

        if value is None:
            return res

        if isinstance(value, basestring):
            return {
                'uri': "%s FROM %s" % (value, self.__class__.__name__),
                'value': "%s FROM %s" % (value, self.__class__.__name__)
            }
        else:
            return {
                'uri': "%s FROM %s" % (value.text, self.__class__.__name__),
                'value': "%s FROM %s" % (value.text, self.__class__.__name__)
            }
