from datetime import datetime, time


class ResourceElement(object):
    """
    The Resource Element of a Control (fr-form-resources)
    """

    def __init__(self, control):
        self.control = control

    def __getattr__(self, name):
        if self.control.resource and hasattr(self.control.resource, 'element'):
            return self.control.resource.element.get(name, None)
        else:
            return None


class Control(object):

    def __init__(self, builder, bind, element):
        self.builder = builder
        self.bind = bind
        self.element = element

        self.parent = None
        self.set_parent()

        # XXX Maybe set_refs is obsolete by following
        self.resource = None
        self.set_resource()

        # model_instance is like raw default_value.
        # Still called model_instance, because of FB terminology.
        self.model_instance = None
        self.set_model_instance()

        self.default_raw_value = None
        self.set_default_raw_value()

        self.default_value = None
        self.set_default_value()

        self.resource_element = ResourceElement(self)

        # Attributes via Element (which get these dynamically)
        if self.resource:
            self.label = self.resource.element.get('label', None)
            self.hint = self.resource.element.get('hint', None)
            self.alert = self.resource.element.get('alert', None)

        self.raw_value = self.element.text

        self.init()

    def init(self):
        """ This method is called after :meth:`~._init__`."""
        pass

    def set_parent(self):
        if self.bind.parent and self.bind.parent.name in self.builder.controls:
            self.parent = self.builder.controls[self.bind.parent.name]

    def set_model_instance(self):
        if not self.bind.parent:
            return

        # TODO namespace prefix Error
        # query = "//xf:model/xf:instance/form/%s/%s" % (
        query = "//form/%s/%s" % (
            self.bind.parent.name,
            self.bind.name
        )

        res = self.builder.xml_root.xpath(query)

        if len(res) > 0:
            self.model_instance = res[0]

    def set_resource(self):
        if self.bind.name in self.builder.resource:
            self.resource = self.builder.resource[self.bind.name]

    def init_runner_attrs(self, runner_element):
        raise NotImplementedError

    def set_default_raw_value(self):
        raise NotImplementedError

    def set_default_value(self):
        raise NotImplementedError

    def encode(self, value):
        """
        By the self.datatype (handler):
        >> self.datetype.encode(value)
        """
        raise NotImplementedError

    def decode(self, value):
        """
        By the self.datatype (handler):
        >> self.datetype.decode(value)
        """
        raise NotImplementedError


class StringControl(Control):

    def init_runner_attrs(self, runner_element):
        self.value = self.decode(runner_element.text)

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(getattr(self.model_instance, 'text', None))

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class DateControl(Control):

    def init_runner_attrs(self, runner_element):
        self.value = self.decode(runner_element.text)

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        if value:
            return datetime.strptime(value, '%Y-%m-%d').date()

    def encode(self, value):
        return datetime.strftime(value, '%Y-%m-%d')


class TimeControl(Control):

    def init_runner_attrs(self, runner_element):
        self.value = self.decode(runner_element.text)

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return datetime.strptime(value, '%H:%M:%S').time()

    def encode(self, value):
        return time.strftime(value, '%H:%M:%S')


class DateTimeControl(Control):

    def init_runner_attrs(self, runner_element):
        self.value = self.decode(runner_element.text)

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    def encode(self, value):
        return datetime.strftime(value, '%Y-%m-%dT%H:%M:%S')


class BooleanControl(Control):

    def init_runner_attrs(self, runner_element):
        self.choice_value = self.decode(runner_element.text)
        # TODO translations
        self.choice_label = 'Yes' if self.choice_value else 'No'
        self.choice = {self.choice_label: self.choice_value}

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        if value == 'true':
            return True
        elif value == 'false':
            return False

    def encode(self, value):
        # TODO isinstance(value, bool) validate?
        if value:
            return 'true'
        else:
            return 'false'


class Select1Control(StringControl):

    def init_runner_attrs(self, runner_element):
        self.choice_value = self.decode(runner_element.text)
        self.choice_label = None

        for item in self.resource.element['item']:
            if item['value'] == self.choice_value:
                self.choice_label = item['label']

        self.choice = {self.choice_label: self.choice_value}


class OpenSelect1Control(Select1Control):
    def init_runner_attrs(self, runner_element):
        super(OpenSelect1Control, self).init_runner_attrs(runner_element)

        if self.choice_label is None:
            self.choice_label = self.choice_value
            self.choice = {self.choice_label: self.choice_value}


class SelectControl(StringControl):

    def init_runner_attrs(self, runner_element):
        self.choices_values = self.decode(runner_element.text)
        self.choices_labels = []
        self.choices = {}

        for item in self.resource.element['item']:
            if item['value'] in self.choices_values:
                self.choices_labels.append(item['label'])
                self.choices[item['label']] = item['value']

    def decode(self, value):
        return value.split(' ')

    def encode(self, value):
        return ' '.join(value)


class AnyURIControl(Control):

    def init_runner_attrs(self, runner_element):
        pass

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        if self.model_instance is not None:
            self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        return value

    def encode(self, value):
        return value


class DecimalControl(Control):

    def init_runner_attrs(self, runner_element):
        self.value = self.decode(runner_element.text)

    def set_default_raw_value(self):
        self.default_raw_value = getattr(self.model_instance, 'text', None)

    def set_default_value(self):
        self.default_value = self.decode(self.model_instance.text)

    def decode(self, value):
        precision = int(self.element.get('digits-after-decimal', 1))

        if precision > 0:
            return float(value)
        else:
            return int(value)

    def encode(self, value):
        return str(value)


class EmailControl(StringControl):
    pass
