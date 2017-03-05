#! /usr/local/bin/python3
import pip
from subprocess import check_output, call

output = check_output(['pip3', 'list', '--outdated'])
outdated = re.findall('\w+(?= \(\w+)', output)
for pkg in outdated:
    try:
        call(['pip3', 'install', pkg, '--no-cache-dir', '--upgrade'])
    except Exception as e:
        print(e)
        print('Can not upgrade package %s' % pkg)
        continue
print('Auto upgrade successful.')
