# vehicle-tracking-system

to run:
first `cd src` then execute command `python3 -m PigeonBox.main`

To run individual parsers:
run command `python3 -m parsers.{readJson, writeJson}` choose one between both

## Tests

Ensure pytest-mock is installed by using the command 'pip install pytest-mock', run unit tests using the command `pytest`, include the option `-q` to make it run silently 

### Commands
- Integration tests: `python3 -m unittest PigeonBox.tests.integration.main`
- System tests: `python3 -m unittest PigeonBox.tests.system.main`
