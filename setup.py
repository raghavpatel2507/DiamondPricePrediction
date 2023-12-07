from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        return requirements

setup(
    name='DIAMOND_PRICE_PREDICTION',
    version='0.0.1',
    author='Raghav',
    author_email='patelraghav014@gamil.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()



)