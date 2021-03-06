from sys import version_info, pypy_version_info as vi
import platform

py = '3' if version_info[0] == 3 else ''

name = 'pypy' + py + '-' + '.'.join(map(str, vi[:2 if not vi[2] else 3]))

if vi.releaselevel != 'final':
    name += '-' + vi.releaselevel

    if vi.serial:
        name += str(vi.serial)

if vi.releaselevel == 'alpha':
    from datetime import datetime
    name += '-' + datetime.now().strftime('%Y%m%d')

name += '-linux_' + platform.machine() + '-portable'

print(name)
