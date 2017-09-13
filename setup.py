#!/usr/bin/env python
import sys
import os
from setuptools import setup

if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist")
    os.system("twine upload dist/*")
    os.system("rm -rf dist/*")
    sys.exit()

# Load the __version__ variable without importing the package
exec(open('coco/version.py').read())

# Command-line tools
entry_points = {'console_scripts': [
    'coco = coco.coco:coco',
]}

setup(name='coco',
      version=__version__,
      description="astronomical coordinate conversion.",
      long_description="",
      author='Tom Barclay',
      author_email='tom@tombarclay.com',
      license='MIT',
      packages=['coco'],
      install_requires=['numpy>=1.8',
                        ],
      entry_points=entry_points,
      include_package_data=True,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          ],
      )
