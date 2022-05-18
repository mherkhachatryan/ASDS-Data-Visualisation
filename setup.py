from setuptools import find_packages, setup
from urbanmob import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='urbanmob',
      version=__version__,
      description='Urban mobility dashboard from taxi movement data',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='',
      author='Mher Khachatryan',
      author_email='mkhachatryan@krisp.ai',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.8',
      install_requires=["dash==2.4.1",
                        "plotly==5.6.0"],
      zip_safe=False)
