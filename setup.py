#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

from setuptools import setup

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
        command = ""

    if command == "uninstall":
        uninstall(package)
    else:
        install(package, __version__)
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

    import sys, shutil
    # clean up local egg-info
    try:
        shutil.rmtree(package + '.egg-info')
    except:
        pass     

        # setup up uninstall arguments
    args = sys.argv
    del args[0:1+1]
    args = ['uninstall', package] + args
    
    # uninstall
    try:
        pip.main(args)
    except:
        pass

if __name__ == "__main__":
    main()