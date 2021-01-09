from submodule1.example_submodule import example as example1
from submodule1.subsubmodule.example_subsubmodule import example as sub_example
from submodule2.example_submodule import example as example2


def main():
    print("Main")
    example1()
    example2()
    sub_example("main")


if __name__ == "__main__":
    main()
