from setuptools import setup

setup(name='pyOceanus',
      version='0.1',
      description='a python interface to OceanusNLP',
      url='http://github.com/seantyh/pyOceanus',
      author='Sean Tseng',
      author_email='seantyh@gmail.com',
      license='MIT',
      packages=['pyOceanus'],
      install_requires=[
          'requests'
      ],
      zip_safe=False)

