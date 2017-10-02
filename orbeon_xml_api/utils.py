from lxml import etree

import os


def xml_from_file(path, filename):
    cwd = os.path.dirname(os.path.realpath(__file__))
    return etree.tostring(etree.parse("%s/%s/%s" % (cwd, path, filename)))


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
