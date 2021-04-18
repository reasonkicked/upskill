from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    
    return requirements


setup(
    name='Lottery',
    version='0.1',
    py_modules=['lottery'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),

    entry_points='''
        [console_scripts]
        lottery=lottery.__main__:main
    ''',

)