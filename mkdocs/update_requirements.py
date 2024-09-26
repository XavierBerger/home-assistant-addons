#!/usr/bin/env python3
"""
This script is showing the latest version of packages listed into requirements.txt
"""
import requests

REQUIREMENTS_FILE = "requirements.txt"

PYPI_URL = "https://pypi.org/pypi/{}/json"


def get_latest_version(package_name):
    """Get latest version of package from Pypi"""
    try:
        response = requests.get(PYPI_URL.format(package_name), timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data["info"]["version"]
        else:
            print(f"Can't find package {package_name} on PyPI.")
            return None
    except Exception as e:
        print(f"Error while getting version of {package_name}: {e}")
        return None


def read_requirements_file(file_path):
    """Get packages from requirements.txt"""
    with open(file_path, "r", encoding="utf-8") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return packages


def update_requirements_with_latest_versions():
    """Display package version in requirement.txt format"""
    packages = read_requirements_file(REQUIREMENTS_FILE)
    updated_packages = []

    packages.sort()
    for package in packages:
        if "==" in package:
            package_name = package.split("==")[0]
        else:
            package_name = package

        version = get_latest_version(package_name)
        if version:
            updated_packages.append(f"{package_name}=={version}")

    for package in updated_packages:
        print(package)


if __name__ == "__main__":
    update_requirements_with_latest_versions()

