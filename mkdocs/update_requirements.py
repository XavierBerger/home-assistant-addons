#!/bin/env python3
"""
This script is updating requirements.txt with the latest version of modules listed into requirements.txt
"""
import subprocess
import importlib.metadata

def remove_versions(requirements_file):
    """Remove version of packages in requirements_file."""
    with open(requirements_file, 'r', encoding="utf-8") as file:
        requirements = file.readlines()

    with open(requirements_file, 'w', encoding="utf-8") as file:
        for requirement in requirements:
            if '==' in requirement:
                package_name = requirement.split('==')[0]
                file.write(package_name.strip() + '\n')
            else:
                file.write(requirement)

def upgrade_packages(requirements_file):
    """Upgrade packages with pip"""
    subprocess.run(['pip', 'install', '--upgrade', '-r', requirements_file], check=True)

def update_requirements(requirements_file):
    """Update requirements_file with installed versions."""
    with open(requirements_file, 'r', encoding="utf-8") as file:
        requirements = file.readlines()

    updated_requirements = []
    for requirement in requirements:
        requirement = requirement.strip()
        if requirement and not requirement.startswith('#'):
            package_name = requirement.split('==')[0]
            try:
                installed_version = importlib.metadata.version(package_name)
                updated_requirements.append(f"{package_name}=={installed_version}\n")
            except importlib.metadata.PackageNotFoundError:
                print(f"Le package {package_name} n'est pas installé.")
        else:
            updated_requirements.append(requirement + '\n')

    with open(requirements_file, 'w', encoding="utf-8") as file:
        file.writelines(updated_requirements)



if __name__ == '__main__':
    REQUIREMENTS_FILE = 'requirements.txt'
    remove_versions(REQUIREMENTS_FILE)
    upgrade_packages(REQUIREMENTS_FILE)
    update_requirements(REQUIREMENTS_FILE)
