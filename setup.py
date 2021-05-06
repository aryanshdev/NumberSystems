import setuptools

setuptools.setup(
    name = 'numbersystems',
    version='1.0.1',
    author = 'Aryansh Gupta',
    author_email = 'Aryanshappmaker@gmail.com',
    description = 'Python Module to allow the use of Vectors',
    py_modules = ["numbersystems"],
    package_dir = {'':'src'},
    long_description = long_description+'<br>Full Documentaion can be found on [ReadTheDocs](https:///VectorsPY.readthedocs.io)',
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/aryanshdev/numbersystems',
    python_requires = '>=3.1',
)