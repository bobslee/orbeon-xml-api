# -*- coding: utf-8 -*-
# Copyright 2017-2018 Bob Leers (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from lxml import etree

import os
import unicodedata


def xml_from_file(path, filename):
    cwd = os.path.dirname(os.path.realpath(__file__))
    return etree.tostring(etree.parse("%s/%s/%s" % (cwd, path, filename)), encoding='UTF-8')


def generate_xml_root(xml):
    try:
        parser = etree.XMLParser(
            ns_clean=True,
            recover=False,
            encoding='utf-8',
            remove_blank_text=True
        )
        root = etree.XML(xml, parser)
    except etree.XMLSyntaxError:
        parser = etree.XMLParser(
            ns_clean=True,
            recover=True,
            encoding='utf-8',
            remove_blank_text=True
        )
        root = etree.XML(xml, parser)

    return root


def unaccent_unicode(unicode_str):
    return unicodedata.normalize('NFKD', unicode_str).encode('ASCII', 'ignore')


def sanitize_xml(xml_root):
    # TODO
    # - Sanitize by whitelist regex: [a-zA-Z0-9] and underscore (_)
    # - Sanitize tag/element names to support Python __getattr__ (tag.tag.tag)
    # - Prevent duplicates

    mapping = {}

    for e in xml_root.xpath('//*[contains(local-name(),"-") or contains(local-name(), ".")]'):
        old_tag = e.tag

        # replacements
        e.tag = e.tag.replace('-', '')
        e.tag = e.tag.replace('.', '_')

        mapping[e.tag] = old_tag

    return mapping


def etree_to_dict(root):
    tags_count = {}

    # Count tag (types), to determine it's a single or
    # multiple/redundant one.
    for item in root:
        if item.tag not in tags_count:
            tags_count[item.tag] = 1
        else:
            tags_count[item.tag] += 1

    datadict = {}
    for item in root:
        if item.tag not in datadict:
            if tags_count[item.tag] > 1:
                datadict[item.tag] = []
            else:
                datadict[item.tag] = None

    for item in root:
        d = {}
        for elem in item:
            d[elem.tag] = elem.text

        if tags_count[item.tag] > 1:
            datadict[item.tag].append(d)
        else:
            datadict[item.tag] = item.text

    return datadict
