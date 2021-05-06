import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name = 'numbersystems',
    version='1.0.1',
    author = 'Aryansh Gupta',
    author_email = 'Aryanshappmaker@gmail.com',
    description = 'Python Module to convert one Number System to other with ease',
    py_modules = ["converter"],
    package_dir = {'':'source'},
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/aryanshdev/numbersystems',
    python_requires = '>=3.1',
)