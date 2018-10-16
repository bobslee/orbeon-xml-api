from setuptools import setup

setup(
    name='orbeon-xml-api',
    version='0.1.0.dev28',
    description='A Python object API for Orbeon XML',
    url='https://github.com/bobslee/orbeon-xml-api',
    author='Bob Leers',
    author_email='bob@novacode.nl',
    license='MIT',
    packages=[
        'orbeon_xml_api'
    ],
    install_requires=['lxml', 'xmltodict', 'xmlunittest']
)
