#! /usr/local/bin/python3
# can not be used on windows due to line end difference.
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip3 install --upgrade --format=columns --no-cache-dir " + dist.project_name, shell=True)
