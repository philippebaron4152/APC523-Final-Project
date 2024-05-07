#!/bin/bash

DIR=./lammps/build/
if [ -d "${DIR}" ]; then
	cd ${DIR}
else
	cd lammps
	mkdir build
	cd ..
	cd ${DIR}
fi

pwd

# include the modules below in your Slurm scipt
module purge
module load intel/19.1.1.217 intel-mpi/intel/2019.7

cmake3 \
-D CMAKE_INSTALL_PREFIX=$HOME/.local \
-D LAMMPS_MACHINE=adroit_min_drude \
-D CMAKE_BUILD_TYPE=Release \
-D CMAKE_CXX_COMPILER=icpc \
-D CMAKE_CXX_FLAGS_RELEASE="-Ofast -xHost -DNDEBUG" \
-D CMAKE_Fortran_COMPILER=/opt/intel/compilers_and_libraries_2020.1.217/linux/bin/intel64/ifort \
-D BUILD_OMP=yes \
-D BUILD_MPI=yes \
-D PKG_KSPACE=yes -D FFT=MKL -D FFT_SINGLE=no \
-D PKG_OPENMP=yes \
-D PKG_DRUDE=yes \
-D PKG_MOLECULE=yes \
-D PKG_RIGID=yes \
-D ENABLE_TESTING=yes ../cmake

make -j 10
#make test
make install
