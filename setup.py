from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """Read the requirements.txt file and return a list of dependencies."""
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()


setup(
    name="projml",
    version="0.0.1",
    author="pops",
    author_email="prashantpoudel745@gmail.com",
    packages=find_packages(),  # Corrected: added parentheses to call the function
    install_requires=get_requirements(),  # Corrected: removed the incorrect argument
)
