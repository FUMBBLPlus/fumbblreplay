"""
FUMBBL SR Rankings module and scripts
"""

import pathlib
import re

from setuptools import setup


thisdir = pathlib.Path(__file__).parent
srcdir = thisdir / "fumbblreplay"


with (thisdir / "README.md").open(encoding="utf8") as f:
  readme = f.read()


metadata_pobj = re.compile(r"__([a-z]+)__ = \"([^\"]+)")
with (srcdir / "__init__.py").open(encoding="utf8") as f:
  initpy = f.read()
metadata = dict(metadata_pobj.findall(initpy))


setup(
  name = "fumbblreplay",
  version = metadata["version"],
  description = "FUMBBL Replay Fetcher",
  long_description = readme,
  url = "https://github.com/FUMBBLPlus/fumbblreplay",
  author = "Szieberth Ádám",
  author_email = "sziebadam@gmail.com",
  license = "MIT",
  classifiers = [
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Topic :: Games/Entertainment :: Board Games"
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.6",
  ],
  keywords = [
      "game",
      "fantasyfootball",
      "fumbbl",
  ],
  packages = ["fumbblreplay"],
  package_dir = {
      "fumbblreplay": "fumbblreplay",
  },
  include_package_data = True,
  package_data={
      "": [
          "LICENSE.txt",
          "README.md",
          "*.json",
      ],
  },
  install_requires = [
      "websockets",
  ],
  extras_require = {
  },
  scripts = [
  ],
  )
