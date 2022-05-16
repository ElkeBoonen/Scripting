from setuptools import setup, find_packages

setup(name='BirdPackage',
      version='0.1',
      description='My bird package!',
      author='Me, myself and I',
      license='MIT',
      install_requires=[],
      packages=find_packages(include=['birds'])
)