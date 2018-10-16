# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from datetime import datetime, time
from lxml import etree

import xmltodict


class ResourceElement(object):
    """
    The Resource Element of a Control (fr-form-resources)
    """

    def __init__(self, control):
        self.control = control

    def __getattr__(self, name):
        if self.control._resource and hasattr(self.control._resource, 'element'):
            return self.control._resource.element.get(name, None)
        else:
            return None


class Control(object):

    def __init__(self, builder, bind, element):
        self._builder = builder
        self._bind = bind
        self._element = element

        self._context = None

        self._parent = None
        self.set_parent()

        # XXX Maybe set_refs is obsolete by following
        self._resource = None
        self.set_resource()

        # model_instance is like raw default_value.
        # Still called model_instance, because of FB terminology.
        self._model_instance = None
        self.set_model_instance()

        self.default_raw_value = None
        self.set_default_raw_value()

        self.default_value = None
        self.set_default_value()

        self._resource_element = ResourceElement(self)

        # Attributes via Element (which get these dynamically)
        self.label = None
        self.hint = None
        self.alert = None

        if self._resource:
            self.label = self._resource.element.get('label', None)
            self.hint = self._resource.element.get('hint', None)
            self.alert = self._resource.element.get('alert', None)

        self._raw_value = None
        self.set_raw_value()

        self.init()

    def init(self):
        """ This method is called after :meth:`~._init__`."""
        pass

    def add_context(self, context):
        self._context = context

    def set_parent(self):
        if self._bind.parent and self._bind.parent.name in self._builder.controls:
            self._parent = self._builder.controls[self._bind.parent.name]

    def set_model_instance(self):
        if not self._bind.parent:
            return

        # TODO namespace prefix Error
        # query = "//xf:model/xf:instance/form/%s/%s" % (
        query = "//form/%s/%s" % (
            self._bind.parent.name,
            self._bind.name
        )

        res = self._builder.xml_root.xpath(query)

        if len(res) > 0:
            self._model_instance = res[0]

    def set_resource(self):
        if self._bind.name in self._builder.resource:
            self._resource = self._builder.resource[self._bind.name]

    def init_runner_form_attrs(self, runner_element):
        raise NotImplementedError

    def set_default_raw_value(self):
        raise NotImplementedError

    def set_default_value(self):
        raise NotImplementedError

    def set_raw_value(self):
        raise NotImplementedError

    def encode(self, value):
        """
        By the self.datatype (handler):
        >> self.datetype.encode(value)
        """
        raise NotImplementedError

    def decode(self, element):
        """
        By the self.datatype (handler):
        >> self.datetype.decode(value)
        """
        raise NotImplementedError


class StringControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.value = self.decode(runner_element)
        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            return element.text

    def encode(self, value):
        return value


class DateControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.value = self.decode(runner_element)
        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            try:
                return datetime.strptime(element.text, '%Y-%m-%d').date()
            except:
                return "%s (!)" % element.text

    def encode(self, value):
        return datetime.strftime(value, '%Y-%m-%d')


class TimeControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.value = self.decode(runner_element)
        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            try:
                return datetime.strptime(element.text, '%H:%M:%S').time()
            except:
                return "%s (!)" % element.text

    def encode(self, value):
        return time.strftime(value, '%H:%M:%S')


class DateTimeControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.value = self.decode(runner_element)
        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            try:
                return datetime.strptime(element.text, '%Y-%m-%dT%H:%M:%S')
            except:
                return "%s (!)" % element.text

    def encode(self, value):
        return datetime.strftime(value, '%Y-%m-%dT%H:%M:%S')


class BooleanControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.choice_value = self.decode(runner_element)
        # TODO translations
        self.choice_label = 'Yes' if self.choice_value else 'No'
        self.choice = {self.choice_label: self.choice_value}

        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            if element.text == 'true':
                return True
            elif element.text == 'false':
                return False

    def encode(self, value):
        # TODO isinstance(value, bool) validate?
        if value:
            return 'true'
        else:
            return 'false'


class Select1Control(StringControl):

    def init_runner_form_attrs(self, runner_element):
        self.choice_value = self.decode(runner_element)
        self.choice_label = None

        if not hasattr(self._resource_element, 'element'):
            return

        for item in self._resource.element['item']:
            # XXX Seems a buggy assumption. Things like 'label'.
            if isinstance(item, basestring):
                continue
            elif item['value'] == self.choice_value:
                self.choice_label = item['label']

        self.choice = {self.choice_label: self.choice_value}
        self.raw_value = runner_element.text

    def set_raw_value(self):
        self._raw_value = self._element.text


class OpenSelect1Control(Select1Control):
    def init_runner_form_attrs(self, runner_element):
        super(OpenSelect1Control, self).init_runner_form_attrs(runner_element)

        if self.choice_label is None:
            self.choice_label = self.choice_value
            self.choice = {self.choice_label: self.choice_value}


class SelectControl(StringControl):

    def init_runner_form_attrs(self, runner_element):
        self.raw_value = runner_element.text
        self.choices_values = self.decode(runner_element)
        self.choices_labels = []
        self.choices = {}

        if not self.choices_values:
            return

        for item in self._resource.element['item']:
            label = None
            value = None

            if isinstance(item, basestring):
                if item == 'label':
                    label = item
                if item == 'value':
                    value = item
            else:
                label = item['label']
                value = item['value']

            if value in self.choices_values:
                self.choices_labels.append(label)
                self.choices[label] = value

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return []
        else:
            return element.text.split(' ')

    def encode(self, value):
        return ' '.join(value)


class AnyUriControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.raw_value = runner_element.text
        decoded = self.decode(runner_element)

        self.uri = decoded['uri']
        self.value = decoded['value']

        # if decoded.get('element', False) and decoded.get('element').get('@filename', False):
        #     self.filename = decoded.get('element', None).get('@filename')

    def set_default_raw_value(self):
        self.default_raw_value = self._model_instance

    def set_default_value(self):
        if self._model_instance is not None:
            self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        # TODO: Quick and dirty, I don't like it! (Because of deadline).
        # This needs to be revised!
        if element is None or not hasattr(element, 'text') or element.text is None:
            res = {'uri': None, 'value': None, 'element': None}
        else:
            res = {'uri': element.text, 'value': element.text}
            element_dict = xmltodict.parse(etree.tostring(element, encoding='UTF-8'))
            if self._bind.name in element_dict:
                res['element'] = element_dict[self._bind.name]

        return res

    def encode(self, value):
        return value


class ImageAnnotationControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.raw_value = runner_element.text
        decoded = self.decode(runner_element)

        if decoded:
            self.image = decoded['image']['image']
            self.annotation = decoded['annotation']['annotation']

    def set_default_raw_value(self):
        # self.default_raw_value = getattr(self._model_instance, 'text', None)
        self.default_raw_value = self._model_instance

    def set_default_value(self):
        if self._model_instance is not None:
            self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        res = {}

        if element is None:
            return res

        for el in element.getchildren():
            res[el.tag] = xmltodict.parse(etree.tostring(el, encoding='UTF-8'))

        return res

    def encode(self, value):
        return value


class DecimalControl(Control):

    def init_runner_form_attrs(self, runner_element):
        self.value = self.decode(runner_element)
        self.raw_value = runner_element.text

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self._model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self._model_instance)

    def set_raw_value(self):
        self._raw_value = self._element.text

    def decode(self, element):
        if element is None or not hasattr(element, 'text') or element.text is None:
            return None
        else:
            precision = int(self._element.get('digits-after-decimal', 1))

            if precision > 0 and hasattr(element, 'text'):
                return float(element.text)
            elif hasattr(element, 'text'):
                return int(element.text)

    def encode(self, value):
        return str(value)


class EmailControl(StringControl):
    pass
