# Python project template

Basic directory structure for a Python project. The following is included:
* A `.gitignore` file for Python projects.
* [The Unlicense](https://unlicense.org/).
* A directory structure for the package itself and for unit tests.
* Several submodules in the package directory to demonstrate how imports work.
* Configuration files for `flake8`, `isort`, `mypy` and `pytest`. The `isort` configuration assumes that `black` is used for code formatting.
* A dummy `setup.py` to be adjusted per project. The current values allow building and installing the package as it is.

The configuration files as well as the `.gitignore` file ignore (among others) the `.venv` and `venv` directories. The `pytest` config explicitly lists the [test](test) directory as the tests source, so all the other directories are ignored.

To set up the environment, run the following in the project root:
```
$ python -m venv ./venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

To format the code and perform static analysis, run the following:
```
$ black .
$ flake8 .
$ isort .
$ mypy .
```

To build and install the package, run the following:
```
$ python setup.py build
$ python setup.py install
```
You can then import and use the package as usual:
```
$ python
>>> import project_template
>>> project_template.main()
```

To use the template, do the following:
* Change all the annotated fields in the [setup.py](setup.py) file.
* Rename the [project_template](project_template) directory to match the `package` variable in [setup.py](setup.py).
* Remove the example files from the package directory and write your code.
* Remove the example tests from the [test](test) directory and write your tests.

## TODO: Move to pyproject.toml? This will need to fix static analysers' versions in requirements.txt.
## TODO: Import something from `project_template` in tests and assert it.
## TODO: Makefile with build && install, format, check, clean.
## TODO: Configure black to ignore venv and other directories. Look into defaults, it already ignores some.
## TODO: Continuous integration.
