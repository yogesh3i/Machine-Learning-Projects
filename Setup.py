from setuptools import find_packages,setup 

from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function willl return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        






setup(
    name='ML_Project',
    version ='0.0.1',
    author='Yogesh7',
    author_email='yogideotale33@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn','matplotlib'],
    instal_requires=get_requirements('requirements.txt')
)