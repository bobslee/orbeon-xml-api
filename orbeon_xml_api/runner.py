import re
from lxml import etree

from builder import Builder, XF_TYPE_CONTROL
from utils import generate_xml_root, unaccent_unicode


class Runner:

    def __init__(self, xml, builder=None, builder_xml=None, lang='en'):
        """
        @param builder Builder
        @param builder_xml str
        """
        self.xml = xml
        self.builder = builder
        self.builder_xml = builder_xml
        self.lang = lang

        self.xml_root = None
        self.set_xml_root()

        if self.builder and self.builder_xml:
            raise Exception("Constructor accepts either builder or builder_xml.")

        if self.builder:
            assert isinstance(self.builder, Builder)
        elif self.builder_xml:
            assert isinstance(self.builder_xml, basestring)
        else:
            raise Exception("Provide either the argument: builder or builder_xml.")

        if self.builder is None and self.builder_xml:
            self.set_builder_by_builder_xml()

        self._form = {}
        self.set_form()

        # init
        self.raw_values = {}
        self.values = {}
        self.controls = {}

        self.init()

        # XXX by setter in RunnerForm
        # runner_form = RunnerForm()
        # runner_form.runner = self
        # self.form = runner_form
        self.form = RunnerForm(self)

    def set_xml_root(self):
        self.xml_root = generate_xml_root(self.xml)

    def set_builder_by_builder_xml(self):
        self.builder = Builder(self.builder_xml, self.lang)

    def set_form(self):
        query = "//form/*/*"
        res = self.xml_root.xpath(query)

        for e in res:
            tag = u"%s" % e.tag
            self._form[unaccent_unicode(tag)] = e

    def init(self):
        for name, control in self.builder.controls.items():
            # XXX Silence maybe isn't the proper way!
            element = None
            try:
                element = self.get_form_element(name)
            except:
                continue

            if element is None:
                continue

            # if callable(getattr(element, 'getchildren', None)):
            self.raw_values[name] = element
            self.values[name] = control.decode(element)

            if control not in XF_TYPE_CONTROL.values():
                control_obj = control
            else:
                # Instantiate the control class (these are imported above)
                control_class = globals()[control.__class__.__name__]
                control_obj = control_class(self.builder, control._bind, element)

            if control_obj is not None:
                control_obj.init_runner_form_attrs(element)
                self.controls[name] = control_obj

    def get_form_element(self, name):
        """
        @param name str The control name (form element tag)
        """

        if name not in self.builder.controls:
            return False

        control = self.builder.controls[name]

        if control._parent is None:
            return None

        return self._form[name]

    def get_raw_value(self, name):
        return self.raw_values[name]

    def get_value(self, name):
        return self.values[name]

    # TODO try/catch KeyError: return ErrorControl with *name* annotated?
    def get_form_control(self, name):
        if name in self.controls:
            return self.controls[name]

    def set_value(self, name, value):
        """
        Set Runner Control XML value.
        """
        pass

    def merge(self, builder_obj, **kwargs):
        # TODO Move and rebuild into RunnerCopyBuilderMerge (class)
        parser = etree.XMLParser(ns_clean=True, encoding='utf-8')
        root = etree.XML('<?xml version="1.0" encoding="UTF-8"?><form></form>', parser)

        no_copy_prefix = kwargs.get('no_copy_prefix', None)

        parents = {}

        for tag, element in builder_obj.controls.iteritems():
            if tag in self.builder.controls.keys():
                # k_: Known elements (present in original runner/builder)
                k_control = self.builder.controls.get(tag, False)

                if not k_control:
                    continue

                k_parent_control = k_control._parent
                k_form_element = self.get_form_element(tag)

                # Sections (escpecially)
                if k_parent_control is None and tag not in parents:
                    parents[tag] = etree.Element(tag)
                    root.append(parents[tag])

                # Controls
                if k_form_element is not None:
                    if k_parent_control is not None and hasattr(k_parent_control, '_bind') and k_parent_control._bind.name not in parents:
                        k_el_parent = etree.Element(k_parent_control._bind.name)
                        parents[k_parent_control._bind.name] = k_el_parent
                        root.append(k_el_parent)

                    if no_copy_prefix is not None and re.search(r"^%s" % no_copy_prefix, tag) is not None:
                        # Instead of the Runner control, add the Builder model_instance
                        parents[k_parent_control._bind.name].append(k_control._model_instance)
                    else:
                        parents[k_parent_control._bind.name].append(k_form_element)
                        # root.append(k_form_element)
            else:
                # n_: New elements
                n_new_control = builder_obj.controls.get(tag, False)

                if not n_new_control:
                    continue

                n_parent_control = n_new_control._parent

                # Sections (escpecially) don't have a parent, hence it's <form> root.
                if n_parent_control is None and tag not in parents:
                    parents[tag] = etree.Element(tag)
                    root.append(parents[tag])
                elif n_parent_control is not None and hasattr(n_parent_control, '_bind') and n_parent_control._bind.name not in parents:
                    if n_parent_control._bind.name in builder_obj._form:
                        n_parent_form_element = builder_obj._form[n_parent_control._bind.name]
                        n_el_parent = etree.Element(n_parent_form_element.tag)
                        parents[n_parent_control._bind.name] = n_el_parent
                        root.append(n_el_parent)

                # Initialize parent
                if hasattr(n_parent_control, '_bind') and n_parent_control._bind.name not in parents:
                    parents[n_parent_control._bind.name] = None

                # Controls
                if hasattr(n_parent_control, '_bind') and n_parent_control._bind.name in parents and n_new_control and n_new_control._model_instance is not None:
                    parents[n_parent_control._bind.name].append(n_new_control._model_instance)
                elif n_new_control and hasattr(n_new_control._parent, '_bind'):
                    parents[n_new_control._parent._bind.name] = n_new_control._model_instance

        # Unicode support
        merge_form_xml = etree.tostring(root)
        merge_form_xml = bytes(bytearray(merge_form_xml, encoding='utf-8'))
        merged_runner = Runner(merge_form_xml, builder_obj)

        return merged_runner


class RunnerForm:

    def __init__(self, runner):
        # XXX getter/setter initialisation
        # self._runner = None
        self._runner = runner

    # def get_runner(self):
    #     return self._runner

    # def set_runner(self, runner):
    #     self._runner = runner

    # XXX getter/setter (Fixes max resursion depth?)
    # runner = property(get_runner, set_runner)

    def __getattr__(self, s_name):
        name = self._runner.builder.sanitized_control_names.get(s_name, False)
        if name:
            return self._runner.get_form_control(name)
        else:
            return None
