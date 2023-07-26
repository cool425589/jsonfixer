import pathlib
from setuptools import setup, find_packages
 
HERE = pathlib.Path(__file__).parent.resolve()
 
PACKAGE_NAME = "jsonfixer"
AUTHOR = "ZhengYu Wu, Liphen Yen"
AUTHOR_EMAIL = "cool425589@gmail.com"
URL = "https://github.com/cool425589/jsonfixer"
DOWNLOAD_URL = "https://github.com/cool425589/jsonfixer"
 
LICENSE = "MIT"
VERSION = "0.0.1"
DESCRIPTION = "JSON Fixer is a versatile Python package designed to efficiently handle and correct JSON data. With its user-friendly interface, the package offers seamless JSON data manipulation and restoration capabilities, making it an essential tool for developers working with JSON files and APIs. JSON Fixer simplifies the process of rectifying JSON errors, ensuring the data remains consistent and accurate. Empower your projects with JSON Fixer and experience hassle-free JSON data management like never before.(Note: If you have a specific name for your package, you can replace 'JSON Fixer' with the chosen name in the introduction.)"
# LONG_DESCRIPTION = (HERE / "docs" / "README.md").read_text(encoding="utf8")
# LONG_DESC_TYPE = "text/markdown"
 
# requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
# INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]
 
# dev_requirements = (HERE / "dev_requirements.txt").read_text(encoding="utf8")
# EXTRAS_REQUIRE = {"dev": [s.strip() for s in dev_requirements.split("\n")]}
 
CLASSIFIERS = [f"Programming Language :: Python :: 3.{str(v)}" for v in range(7, 12)]
PYTHON_REQUIRES = ">=3.7"
 
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=LONG_DESCRIPTION,
    # long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    # install_requires=INSTALL_REQUIRES,
    # extras_require=EXTRAS_REQUIRE,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
)