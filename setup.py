import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="searcher",
    version="0.1.0",
    author="Fernando Dantas",
    license="MIT",
    description="Find almost anything in a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fmndantas/searcher',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ),
)
