Instructions for Installing LAMMPS and running Tests: 

After logging onto the Adroit cluster, clone the respository into your home directory using the command - 
```
git clone https://github.com/philippebaron4152/APC523-Final-Project.git
```
After this, our modified version of lammps can be installed with the sequence of commands - 
```
cd APC523-Final-Project
bash compile_lammps.sh
```
This will install the exectuable "lmp_adroit_min_drude" in the ~/.local/bin/ folder. 

"simple_e_field" is our analytically tractable test case. This case can be run by running the commands - 
```
cd APC523-Final-Project/simple_e_field
sbatch sub_lammps.sh
```
The output trajectory file "dump.coord" should contain the same coordinates for the Drude particle (index 2) as our analytical calculation. 

"swm4_ndp_water" is our advanced test case of 64 polarizable water molecules. The simulation can be run by entering the following commands - 
```
cd APC523-Final-Project/swm4_ndp_water
sbatch sub_lammps.sh
```
This runs our SCF minimization implementation of polarizable simulation. To plot the resulting density and energy trajectories and compare them to the EL implementation, the following commands should be entered from within the folder - 
```
module load anaconda3/2023.9
pip install lammps-logfile
python plot.py
```
The plots will be output as an image titled "method_comp.png". The output data of simulation with our method is found in "log_min.lammps". 
