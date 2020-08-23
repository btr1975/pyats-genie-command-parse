
# This Makefile is to run pytest tests, and coverage reports
#
#   To run just CLI tests install the following
#      pip3 install pytest coverage
#
#   To run tests and output a HTML report install the following
#      pip3 install pytest pytest-html coverage
#
#   Running all will show failed is a test fails, but it will still build
#   the coverage data
#

.PHONY: all pytest_html pytest_min pytest_verbose coverage_run coverage_report coverage_html

REPORT_NAME = tests/reports/pytest-$(shell date +'%Y-%m-%d-%H-%M-%S').html
COVERAGE_REPORT_DIR = tests/reports/coverage-$(shell date +'%Y-%m-%d-%H-%M-%S')
COVERAGE_REPORT_TITLE = $(shell date +'%Y-%m-%d-%H-%M-%S')

all: coverage_run

pytest_min:
	python -m pytest

pytest_verbose:
	python -m pytest -vv -rs

pytest_html:
	python -m pytest --html $(REPORT_NAME) -vv

coverage_run:
	python -m coverage erase
	python -m coverage run

coverage_report:
	python -m coverage report

coverage_html:
	python -m coverage html --directory=$(COVERAGE_REPORT_DIR) --title=$(COVERAGE_REPORT_TITLE)
