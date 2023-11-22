#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.sdist import sdist

# See also: https://github.com/kennethreitz/setup.py/blob/master/setup.py
here = os.path.abspath(os.path.dirname(__file__))

def get_package_version() -> str:
    """Get the package version from the __init__ file"""
    __version__: str = re.findall(
        r"""__version__ = ["']+([0-9\.]*)["']+""",
        open("src/airfoils/__version__.py", encoding="UTF-8").read(),
    )[0]
    return __version__

def main():
    package = 'airfoils'
    __version__ = get_package_version()

    if len(sys.argv) >= 2:
        command: str = sys.argv[1]
    else:
        command = "install"

    if command == "dist_info":
        setup(cmdclass={"sdist": sdist})
    if command == "editable_wheel":
        setup(cmdclass={"develop": develop})
    if command == "install":
        install(package, __version__)
    elif command == "uninstall":
        uninstall(package)
    else:
        print(f"Command {command} not recognized")


def install(package: str, version: str) -> None:
    """INSTALL THE PACKAGE

    Args:
        package (str): Package Name
        version (str): Version Number
    """
    setup(
        name=package,
        version=version,
        include_package_data=True,
    )


def uninstall(package: str) -> None:
    """Uninstall the package

    Args:
        package (str): Package Name
    """
    try:
        import pip
    except ImportError:
        print("Error importing pip")
        return
    pip.main(["uninstall", package, "-y"])

main()