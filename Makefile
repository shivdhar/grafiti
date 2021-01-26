BASEPYTHON := /usr/bin/python3

.ONESHELL:

.PHONY: docs
docs:
	cd docs/
	poetry run make html
