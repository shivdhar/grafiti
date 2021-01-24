BASEPYTHON := /usr/bin/python3

.ONESHELL:

PYTHON := 
.PHONY: docs
docs:
	cd docs/
	poetry run make html
