#
# Module: Makefile
#

HIDE                        ?= @
VENV                        := env
PIP                         := $(VENV)/bin/pip
PYTHON                      := $(VENV)/bin/python
SHELL                       := /bin/bash


prepare-venv:
	$(HIDE)virtualenv $(VENV) --no-pip
	$(HIDE)$(VENV)/bin/easy_install pip==18.0
	$(HIDE)$(PIP) install --upgrade -r requirements.txt
	$(HIDE)$(PIP) install -e .

$(BUILDDIR):
	mkdir -p $@


requirements:
	$(HIDE)$(PIP) uninstall -y $(PACKAGE)
	$(HIDE)$(PIP) freeze > requirements.txt
	$(HIDE)$(PIP) install -e .

