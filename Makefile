-include Makefile.local

PYTEST_ARGS ?= -vv -x

VENV_NAME ?= .env
SYS_PYTHON = python3
VENV_PYTHON = $(VENV_NAME)/bin/python

.PHONY: venv
venv: requirements.txt
	$(MAKE) clean
	virtualenv --python=$(SYS_PYTHON) $(VENV_NAME)
	$(VENV_PYTHON) -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

.PHONY: clean
clean:
	rm -rf $(VENV_NAME)

.PHONY: test
test: venv
	PYTHONPATH=$(VENV_PYTHON)
	$(VENV_PYTHON) -m pytest $(PYTEST_ARGS)

