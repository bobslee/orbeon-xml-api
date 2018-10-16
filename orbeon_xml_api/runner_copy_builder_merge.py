# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

class RunnerCopyBuilderMerge:

    def __init__(self, runner, builder, **kwargs):
        self.runner = runner
        self.builder = builder

        self.no_copy_prefix = None
        if kwargs.get('no_copy_prefix', False):
            self.set_no_copy_prefix(kwargs['no_copy_prefix'])

        if kwargs.get('no_copy_prefix', False):
            self.set_no_copy_prefix(kwargs['no_copy_prefix'])

    def set_no_copy_prefix(self, no_copy_prefix):
        self.no_copy_prefix = no_copy_prefix

    # TODO move Runner merge() implementation to this function.
    def merge(self):
        return self.runner.merge(self.builder, no_copy_prefix=self.no_copy_prefix)
