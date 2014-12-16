import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'pyramid',
    ]

entry_points = """
[paste.paster_create_template]
mzhs = mzhs.scaffolds:MzhsProjectTemplate
[pyramid.scaffold]
mzhs = mzhs.scaffolds:MzhsProjectTemplate
"""

setup(name='mzhs',
      version='0.1',
      description='A pyramid scaffold by mzhs',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Framework :: Pyramid :: Scaffold",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='mzhs',
      author_email='mzhsksk@gmail.com',
      url='https://github.com/mzhs/pyramid_mzhs',
      keywords='pyramid scaffold',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points=entry_points,
      )

