#!/usr/bin/env python3

""" Post generation hooks.

.. codeauthor:: Raymond Ehlers <raymond.ehlers@cern.ch>, ORNL
"""

from pathlib import Path

if __name__ == "__main__":
    #project_directory = Path("{{cookiecutter.directory_name}}")
    project_directory = Path(".")

    # Create drafts and images directories
    for dirname in ["drafts", "images"]:
        drafts = project_directory / dirname
        drafts.mkdir(exist_ok=True, parents=True)

