.POSIX:
SHELL := bash
.SHELLFLAGS: -eu -o pipefail -c
.DELETE_ON_ERROR:
.SUFFIXES:

IGNORED_DIRS := '.*\.eggs|\.git|\.hg|\.mypy_cache|\.tox|\.venv|venv|_build|buck-out|build|dist.*'

.PHONY: format
format:
	@python -m black .
	@python -m isort .

.PHONY: check
check:
	@find . -name '*.py' -type f | grep -E -v $(IGNORED_DIRS) | xargs python -m pylint
	@python -m mypy .

.PHONY: test
test:
	@python -m py.test .

.PHONY: install
install:
	@python -m pip install .

.PHONY: clean
clean:
	@find . -type d -name "__pycache__" -exec rm -r "{}" \+

	@if [ -d ./.mypy_cache ]; then \
		rm -r ./.mypy_cache; \
	fi;

	@if [ -d ./.pytest_cache ]; then \
		rm -r ./.pytest_cache; \
	fi;
