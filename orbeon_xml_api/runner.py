# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

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
        no_copy_prefix = kwargs.get('no_copy_prefix', None)
        parents = {}
        merged_form = builder_obj.get_form_instance_raw()
        merged_form = etree.fromstring(merged_form)

        for element in merged_form.iter():
            tag = element.tag
            if tag not in ['annotation', 'image']:
                if isinstance(tag, basestring):
                    if no_copy_prefix and tag.startswith(no_copy_prefix):
                        pass
                    else:
                        ov = self.xml_root.xpath('//%s' % tag)
                        if len(ov) > 0 and ov[0].text:
                            if len(ov[0].text.strip()) > 0:
                                element.text = ov[0].text

        merge_form_xml = etree.tostring(merged_form)
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
