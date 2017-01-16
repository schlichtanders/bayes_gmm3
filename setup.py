#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from setuptools import setup, find_packages
from distutils.command.clean import clean as Clean
__author__ = "kamperh"

class CleanCmd(Clean):
    description = "Cleans ..."

    def run(self):

        Clean.run(self)

        if os.path.exists('build'):
            shutil.rmtree('build')

        for dirpath, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                if (filename.endswith('.so') or
                        filename.endswith('.pyd') or
                        filename.endswith('.pyc') or
                        filename.endswith('_wrap.c') or
                        filename.startswith('wrapper_') or
                        filename.endswith('~')):
                    os.unlink(os.path.join(dirpath, filename))

            for dirname in dirnames:
                if dirname == '__pycache__' or dirname == 'build':
                    shutil.rmtree(os.path.join(dirpath, dirname))
                if dirname == "pymscons.egg-info":
                    shutil.rmtree(os.path.join(dirpath, dirname))


setup(
    name='bayes_gmm3',
    version='0.1.0',
    description='bayes_gmm3 as package',
    author=__author__,
    author_email='s.sahm@reply.de, a.loosley@reply.de, a.salles@reply.de',
    license='to be announced',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "numpy",
        "scipy",
        "nose"
    ],
    dependency_links=[],
    # include_package_data=True,  # should work, but doesn't, I think pip does not recognize git automatically
    package_data={
        'data': ['*/*'],
    },
    cmdclass={'clean': CleanCmd}
)
