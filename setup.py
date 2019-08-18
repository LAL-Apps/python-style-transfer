import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='deepdream',
      version='0.1.0',
      description='Stylize images using the deep dream approach',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Lorenz Lehmann',
      author_email='apps.lal@gmail.com',
      license="MIT",
      packages=find_packages(exclude=("tests",)),
      zip_safe=False)
