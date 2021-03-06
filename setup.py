import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sf",
    version="0.0.2",
    author="Tommy Markstein",
    author_email="signed-boolean@sys.fail",
    description="A python package for earth, balloon and rocket physics",
    long_description="A python package for earth, balloon and rocket physics",
    long_description_content_type="text/markdown",
    url="https://github.com/sys-fail/sf,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
