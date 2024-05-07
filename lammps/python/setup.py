# this only installs the LAMMPS python package
# it assumes the LAMMPS shared library is already installed
from setuptools import setup
from setuptools.dist import Distribution
from sys import version_info
import os,time

versionfile = os.environ.get("LAMMPS_VERSION_FILE")
if not versionfile:
    # allows installing and building wheel from current directory
    LAMMPS_DIR = os.path.realpath(os.path.join(os.environ['PWD'], '..'))
    versionfile = os.path.join(LAMMPS_DIR, 'src', 'version.h')

def get_lammps_version():
    version_h_file = os.path.join(versionfile)
    with open(version_h_file, 'r') as f:
        line = f.readline()
        start_pos = line.find('"')+1
        end_pos = line.find('"', start_pos)
        t = time.strptime("".join(line[start_pos:end_pos].split()), "%d%b%Y")
        return "{}.{}.{}".format(t.tm_year,t.tm_mon,t.tm_mday)

class BinaryDistribution(Distribution):
    """Wrapper to enforce creating a binary package"""
    def has_ext_modules(self):
        return True

if version_info.major >= 3:
    pkgs = ['lammps', 'lammps.mliap']
else:
    pkgs = ['lammps']

with open("README", "r") as fh:
    long_description = fh.read()

libname = os.environ.get("LAMMPS_SHARED_LIB")
if libname:
    pkgdata = {'lammps': [ libname ]}
    bdist = BinaryDistribution
else:
    pkgdata = {}
    bdist = Distribution

setup(
    name = "lammps",
    version = get_lammps_version(),
    author = "The LAMMPS Developers",
    author_email = "developers@lammps.org",
    url = "https://www.lammps.org",
    project_urls = {
        "Bug Tracker": "https://github.com/lammps/lammps/issues",
    },
    description = "LAMMPS Molecular Dynamics Python package",
    long_description = long_description,
    long_description_content_type = "text/plain",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    license = "GPL",
    packages = pkgs,
    package_data = pkgdata,
    distclass = bdist,
)
