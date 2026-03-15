from setuptools import setup, find_packages
from typing import List
# def get_requirements(file_path):
#     with open(file_path) as f:
#         requirements = f.read().splitlines()
#     return requirements

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as f:
        requirements = f.read().splitlines()
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


# HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
    
#     return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Shammi',
    author_email='shammikumar3833@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
    )
# The above code is a setup script for a Python project named "mlproject".
# It uses the `setuptools` library to define the package metadata and
# dependencies. The `get_requirements` function reads the dependencies from a
# `requirements.txt` file and returns them as a list, while also removing any
# occurrence of the string '-e .'. The `setup` function is then called with the
# project name, version, author information, packages to include, and the list
# of install requirements. This script is typically used to package and
# distribute the Python project.