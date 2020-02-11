from setuptools import setup, find_packages
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"', open("bandaid/agent.py").read(), re.M
).group(1)

setup(
    name="bandaid",
    author="James Campbell",
    author_email="james@jamescampbell.us",
    version=version,
    license="GPLv3",
    description="Get band tour info and watchlist from the command line",
    packages=["bandaid"],
    py_modules=["bandaid"],
    keywords=["band", "tracking", "tour-dates", "music-tracking", "bands"],
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    install_requires=["pprint", "bs4", "requests"],
    entry_points={"console_scripts": ["bandaid = bandaid.agent:main"]},
    url="https://github.com/jamesacampbell/bandaid",
    download_url="https://github.com/jamesacampbell/bandaid/archive/{}.tar.gz".format(
        version
    ),
)