from setuptools import setup, find_packages

__pckg__ = "date"
__version__ = "0.0.1"

setup(
    name=__pckg__,
    version=__version__,
    description="Contains two Classes (Date and TimeDelta) required for working with dates.",
    author="Nataliia Igrashkina",
    author_email="natasha_igra@mail.ru",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extra_require={
        "tests: ["
        "pytest==6.2.2"
        "pytest-cov==2.11.1"
    }
)