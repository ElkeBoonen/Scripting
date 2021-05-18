from setuptools import setup, find_packages

setup(name='mypackage',
      version='0.1',
      description='My first package!',
      author='Me, myself and I',
      license='MIT',
      install_requires=[],
      packages=find_packages(include=['mypackage'])
)