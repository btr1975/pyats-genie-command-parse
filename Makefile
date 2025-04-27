# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.3
#

.PHONY: info all build coverage format pylint pytest check-security pip-export pdf

info:
	@echo "make options"
	@echo "    info                      To display this message"
	@echo "    all                       To run all tasks"
	@echo "    build                     To build"
	@echo "    coverage                  To run coverage and display ASCII and output to htmlcov"
	@echo "    format                    To run black on pyats_genie_command_parse and tests"
	@echo "    pylint                    To run pylint"
	@echo "    pytest                    To run pytest with verbose option"
	@echo "    check-security            To run bandit"
	@echo "    pip-export                To export requirements.txt and requirements-dev.txt"
	@echo "    pdf                       To create PDF Docs"

all: format pylint coverage check-security pip-export

build:
	@python -m build

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black pyats_genie_command_parse/
	@uv run black tests/

pylint:
	@uv run pylint pyats_genie_command_parse/

pytest:
	@uv run pytest --cov -vvv

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

pdf:
	@uv run sphinx-build -b rinoh ./docs ./docs/_build/pdf
