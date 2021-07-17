import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="linear_algebra",
    version="0.0.1",
    author="Ash Bellett",
    author_email="ash.bellett.ab@gmail.com",
    description="Implementations of linear algebra algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashbellett/linear-algebra",
    project_urls={
        "Bug Tracker": "https://github.com/ashbellett/linear-algebra/issues",
    },
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "linear_algebra"},
    packages=setuptools.find_packages(where="linear_algebra"),
    python_requires=">=3.7",
)