import os
import sys
import shutil
import getpass
from setuptools import setup, find_packages

_context = "pyingestionengine"
_version = "1.0.0"
_username = getpass.getuser()
_update_external_dependents_apps = False

if __name__ == "__main__":
    setup(
        name=_context,
        description="Biblioteca de " + _context,
        author=_username,
        packages=[_context],
        include_package_data=True,
        zip_safe=True,
        version=_version,
        script_args=['--quiet', 'bdist_egg'],
    )

    _assembly = "dist/%s-%s-py2.7.egg" % (_context, _version)
    _bin = _context + "/bin"

    if _update_external_dependents_apps:
        shutil.copy2(_assembly, "~/Documents")

    if not os.path.exists(_bin):
        os.makedirs(_bin)

    shutil.copy2(_assembly, _bin)

    shutil.rmtree("build")
    shutil.rmtree("dist")
    shutil.rmtree(_context + ".egg-info")