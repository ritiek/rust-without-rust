#!/usr/bin/env python

from setuptools import setup, find_packages
import playground

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name="rust-playground",
      version=playground.__version__,
      description="Use Python to execute simple Rust code by running"
                  "it on https://play.rust-lang.org/",
      long_description=long_description,
      author="Ritiek Malhotra",
      author_email="ritiekmalhotra123@gmail.com",
      packages = find_packages(),
      entry_points={
            "console_scripts": [
                  "playground = playground.playground:command_line",
            ]
      },
      url="https://www.github.com/ritiek/rust-without-rust",
      keywords=["rust", "python", "playground"],
      license='MIT',
      download_url="https://github.com/ritiek/rust-without-rust/archive/v" + playground.__version__ + ".tar.gz",
      classifiers=[],
)
