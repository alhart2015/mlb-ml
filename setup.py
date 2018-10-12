import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alhart2015-mlb-ml",
    version="0.0.1",
    author="Alden Hart",
    author_email="not.putting.this.in@nope.com",
    description="Use Tensorflow to predict MLB performance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alhart2015/mlb-ml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)