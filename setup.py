import setuptools

setuptools.setup(
    name='find',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
