# orbeon-xml-api

## Run unit tests

```
python -m unittest tests.test_builder
python -m unittest tests.test_runner
```

### nose

```
nosetests tests/controls
nosetests tests.controls

nosetests tests/controls/test_input.py
```

With STDOUT (for pdb usage) support:

```
nosetests -s tests.controls
```