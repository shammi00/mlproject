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
