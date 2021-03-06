from setuptools import find_namespace_packages, setup  # type: ignore


def read_readme():
    with open("README.md", "r", encoding="utf8") as f:
        return f.read()


def main():
    package_name = "project-template"  # TODO: Change.
    package = "project_template"  # TODO: Change.
    subpackages = find_namespace_packages(".", include=[f"{package}.*"])

    setup(
        name=package_name,
        use_scm_version=True,
        setup_requires=["setuptools_scm"],
        author="<author-name>",  # TODO: Change.
        author_email="<author-email>",  # TODO: Change.
        description="<description>",  # TODO: Change.
        long_description=read_readme(),
        license="Unlicense License",
        keywords="<space-separated-keywords>",  # TODO: Change.
        classifiers=["<https://pypi.org/classifiers/>"],  # TODO: Change.
        url="<url>",  # TODO: Change.
        packages=[package, *subpackages],
        package_data={package: ["py.typed"]},
        python_requires=">=3.8",
        zip_safe=False,
        extras_require={
            "testing": ["pytest"],
            "linting": ["pytest", "mypy", "lxml"],
        },
    )


if __name__ == "__main__":
    main()
