#! /usr/local/bin/python3
# can not be used on windows due to line end difference.
import pip
import re
from subprocess import check_output, call

output = check_output(['pip3', 'list', '--outdated'])
outdated = re.findall('\w+(?= \(\w+)', str(output))
for pkg in outdated:
    try:
        call(['pip3', 'install', pkg, '--no-cache-dir', '--upgrade'])
    except Exception as e:
        print(e)
        print('Can not upgrade package %s' % pkg)
        continue
print('Auto upgrade successful.')
