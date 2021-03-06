# Python project template

A basic structure for a Python project. The following is included:

* A [.gitignore](.gitignore) file for Python projects.
* [The Unlicense](https://unlicense.org/).
* A directory structure for the [package itself](project_template) and for [unit
  tests](test).
* Several submodules in the [package directory](project_template) to demonstrate
  how imports work.
* Configuration for `isort`, `mypy`, `pylint` and `pytest`.
* A dummy [setup.py](setup.py) to be adjusted per project. The current values
  allow building and installing the package as it is.
* Automatic package versioning using
  [setuptools_scm](https://github.com/pypa/setuptools_scm) based on git tags.
* GitHub Actions for CI. After each push with a tag matching `v[0-9]+.*`, the
  unit tests are run and `mypy` coverage is produced.

The configuration files as well as the `.gitignore` file ignore (among others)
the `.venv` and `venv` directories. The `pytest` config explicitly lists the
[test](test) directory as the tests source, so all the other directories are
ignored.

Currently, Python 3.8 is assumed, though this can easily be changed in
`target-version` under `[tool.black]` in [pyproject.toml](pyproject.toml) and in
`python_requires` in [setup.py](setup.py).


## Examples

To set up the environment, run the following in the project root:
```
$ python -m venv ./venv
$ source ./venv/bin/activate
$ python -m pip install -r requirements.txt
```

To format the code and perform static analysis, run the following:
```
$ python -m black .
$ python -m pylint ./project_template ./test
$ python -m isort .
$ python -m mypy .
```

To run unit tests, run the following:
```
$ python -m pytest .
```

To build and install the package, run the following:
```
$ python -m pip install .
```
You can then import and use the package as usual:
```
$ python
>>> import project_template
>>> project_template.main()
```

You can also directly run any of the scripts from the project root:
```
$ python project_template/main.py
```

In addition, there is a [Makefile](Makefile) to automate some of these tasks.


## Git hooks

To setup autoformatting after each commit, use the following scripts. Make sure
you have `black` and `isort` installed!

* `.git/hooks/pre-commit`
  ```
  #!/usr/bin/sh

  # Get all changed (Added, Copied, Modified, Renamed) .py files.
  files=$(git diff --cached --name-only --diff-filter=ACMR "*.py")
  [ -z "$files" ] && exit 0

  # Run black on them.
  echo "$files" | xargs python -m black

  # Run isort on them.
  echo "$files" | xargs python -m isort

  # Add the files back to staging.
  echo "$files" | xargs git add

  exit 0
  ```
* `.git/hooks/post-commit`
  ```
  #!/usr/bin/sh

  git update-index -g
  ```
* Do not forget to set them as executable.


## Using the template

To use the template, do the following:

* Change all the annotated fields in the [setup.py](setup.py) file.
* Rename the [project_template](project_template) directory to match the
  `package` variable in [setup.py](setup.py).
* Remove the example files from the package directory and write your code.
* Remove the example tests from the [test](test) directory and write your tests.
