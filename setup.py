import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='treesource',
      version='0.0.5',
      description=' commented source file-trees generator ',
      author='Marco Pascucci',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email='marpas.paris@gmail.com',
      url='https://github.com/mpascucci/treesource-doc',
      packages=['treesource', 'treesource.render'],
      install_requires=['anytree'],
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ]
)