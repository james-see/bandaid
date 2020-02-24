#!/bin/bash
# Builds and Deploys distro to pypi
cd ../client/
python3 setup.py sdist bdist_wheel
twine upload dist/*
echo "Uploaded."
echo "Run ./clean-client.sh to clean and ensure ready for next version."