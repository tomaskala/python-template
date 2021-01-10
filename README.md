# Python project template

Basic directory structure for a Python project. The following is included:
* A `.gitignore` file for Python projects.
* [The Unlicense](https://unlicense.org/).
* A directory structure for the package itself and for unit tests.
* Several submodules in the package directory to demonstrate how imports work.
* Configuration for `isort`, `mypy`, `pylint` and `pytest`.
* A dummy `setup.py` to be adjusted per project. The current values allow building and installing the package as it is.

The configuration files as well as the `.gitignore` file ignore (among others) the `.venv` and `venv` directories. The `pytest` config explicitly lists the [test](test) directory as the tests source, so all the other directories are ignored.

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
$ python -m py.test .
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

To use the template, do the following:
* Change all the annotated fields in the [setup.py](setup.py) file.
* Rename the [project_template](project_template) directory to match the `package` variable in [setup.py](setup.py).
* Remove the example files from the package directory and write your code.
* Remove the example tests from the [test](test) directory and write your tests.

## TODO: Continuous integration.
## TODO: Automatic version numbers.
