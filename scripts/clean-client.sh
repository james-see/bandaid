#!/bin/bash
# cleans out the folder to get ready to deploy lib
cd ../client/
rm -rf build dist bandaid.egg-info
echo "Client is fresh and clean."
echo "Run ./distro-client.sh to create a new distro and upload via twine to pypi."

