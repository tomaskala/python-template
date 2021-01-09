from setuptools import find_namespace_packages, setup  # type: ignore


def read_readme():
    with open("README.rst", "r", encoding="utf8") as f:
        return f.read()


def main():
    project_name = "<project-name>"

    setup(
        name=project_name,
        version="<project-version>",
        author="<author-name>",
        author_email="<author-email>",
        description="<description>",
        long_description=read_readme(),
        license="Unlicense License",
        keywords="<space-separated-keywords>",
        classifiers=["<https://pypi.org/classifiers/>"],
        url="<url>",
        packages=find_namespace_packages(where="src"),
        package_dir={project_name: "src"},
        package_data={project_name: ["py.typed"]},
        python_requires=">=3.6",
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
