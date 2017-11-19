# orbeon-xml-api

Orbeon (Forms) XML API for Python.

For information about Orbeon, see [Orbeon homepage](https://www.orbeon.com)

## Introduction

**orbeon-xml-api** is a Python package, which loads and transforms
Orbeon Builder and Runner XML into usable Python objects.  It's main
aim is to provide easy access to a Form its controls/fields, also
captured as Python objects, which makes this API very versatile and usable.

**Notes about terms:**
  - "Builder" could be read/seen as "Builder Form"
  - "Runner" could be read/seen as "Runner Form"
  - "Control" could be read/seen as "Field"

## Features

  - Compatible with Python 2.7 ([GitHub issu to support 3.3 and later](https://github.com/bobslee/orbeon-xml-api/issues/7))
  - Constructor of the **Builder** and **Runner** class, only requires
    the XML and an optional language code for translations.
  - Get a Runner object Control/Fields as a usable object, by the Pythonic attribute-getter (`__getattr__`)
  - Get the value as Python object (e.g. DateTime object, dict) and attributes of a Runner Control/Field object, by Pythonic attribute-getter (`__getattr__`).
  Conversion of [Runner control-value to Python object][runner-control-value-to-python-object] e.g. DateTime, Boolean, Dict etc.
  - Merging a Runner with a updates/changes in Builder. This results in a new Runner, which kept it's former controls and merged new controls
    from the Builder into it.
  - Open source (MIT License)

## Installation

The source code is currently hosted on GitHub at:
https://github.com/bobslee/orbeon-xml-api

Binary installers for the latest released version are available at the [Python
package index](https://pypi.python.org/pypi/orbeon-xml-api)

```sh
# PyPI
pip install orbeon-xml-api
```

**Dependencies:** `lxml, xmltodict`

## License
[MIT](LICENSE)

## Contributing to pandas
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## Usage examples

Following examples use an Orbeon demo form **"Controls"**
For more examples of usage, see the unit-tests.

``` python
>> from orbeon-xml-api import Builder, Runner

# builder_xml is an Orbeon Builder XML document (text)
# runner_xml is an Orbeon Runner XML document (text)

>> builder = Builder(builder_xml)
>> runner = Runner(builder, runner_xml)

>> print runner.form.inputfield.value
'Michelle'
>> runner.form.inputfield.label
'Input Field'

# Raw XML value
>> print runner.form.inputfield.datetime.raw_value
'2009-10-16T17:30:00'

# Python object
>> print runner.form.inputfield.datetime.value
datetime.datetime(2009 10 16 17 30)

```

## Unit tests

### nose

Currently with **nose**.
Standard Python **unittest** crashes.


*Install nose:*

```
pip install nose
```

*Run nosetests:*

```
nosetests

nosetests tests/controls
nosetests tests.controls

nosetests tests/controls/test_input.py
```

*Send nose STDOUT (pdb support):*

```
nosetests -s
```

*Performance tests (timers) - install nose-timer:*

```
pip install nose-timer

nosetests --with-timer

```

### Python unittest (currently crashes)

```
python -m unittest tests.test_builder
python -m unittest tests.test_runner
```
