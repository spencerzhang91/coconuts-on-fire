#! /usr/local/bin/python3
# can not be used on windows due to line end difference.
import pip
import re
from subprocess import check_output, call

output = check_output(['pip3', 'list', '--outdated'])
outdated = re.findall('^(?=b)\S+(?= \(\w+)|(?<=\\\\n)\S+(?= \(\w+)', str(output))
if not outdated:
    print('Everything is up to date.')
else:
    outdated[0] = outdated[0][2:] # This line is so ugly, but this is all I can do.

    for pkg in outdated:
        try:
            call(['pip3', 'install', pkg, '--no-cache-dir', '--upgrade'])
            print('updating...')
        except Exception as e:
            print(e)
            print('Can not upgrade package %s' % pkg)
            continue
    print('Auto upgrade successful.')