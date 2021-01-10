from project_template.submodule1.example_submodule import example as example1
from project_template.submodule1.subsubmodule.example_subsubmodule import (
    example as sub_example,
)
from project_template.submodule2.example_submodule import example as example2

__all__ = ["main"]


def main():
    print("Main")
    example1()
    example2()
    sub_example("main")


def return_true():
    return True


if __name__ == "__main__":
    main()
