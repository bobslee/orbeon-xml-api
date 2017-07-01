# orbeon-xml-api

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
