from setuptools import setup ,find_packages
from typing import List

def getrequirements(file_path:str)->List[str]:
    '''
    this function will read the file
    '''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace("\n","")  for req in requirements]

    return requirements


setup(
    name="mlproject",
    version="0.0.0.1",
    author="RISHIKESH",
    author_email="rishikeshbharote895@gmail.com",
    packages=find_packages(),
    install_requires = getrequirements("requirements.txt")
)