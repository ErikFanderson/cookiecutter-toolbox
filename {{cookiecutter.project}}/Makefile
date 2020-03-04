# Author: Erik Anderson 
# Date Created: 03/03/2020

default: test

# Lints project directory recursively
lint:
	pylint {{cookiecutter.project}} tests

# Formats project directory recursively
format:
	yapf -i -r {{cookiecutter.project}} tests

# Type checks project directory recursively
type:
	mypy {{cookiecutter.project}} tests

# Runs all tests in tests directory 
test:
	pytest -v --ignore=$(TOOLBOX_HOME)/tests

# Runs example
example:
	toolbox-cli -c examples/example_config.yml -t examples/example_tools.yml example_job
