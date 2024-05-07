import numpy as np
import matplotlib.pyplot as plt
import lammps_logfile

rho_el = np.array(lammps_logfile.File('log_el.lammps').get("Density"))
rho_min = np.array(lammps_logfile.File('log_min.lammps').get("Density"))

U_el = np.array(lammps_logfile.File('log_el.lammps').get("PotEng"))
U_min = np.array(lammps_logfile.File('log_min.lammps').get("PotEng"))

step = np.array(lammps_logfile.File('log_el.lammps').get("Step"))

fig, axs = plt.subplots(1, 2, figsize=(12,4))
T = step * 0.001
axs[0].plot(T, rho_el, label='EL')
axs[0].plot(T, rho_min, label='SCF')
axs[0].set_xlabel("time (ps)")
axs[0].set_ylabel(r"$\rho$" + " " + r"$(kg/m^3)$")
axs[0].legend()

axs[1].plot(T, U_el, label='EL' )
axs[1].plot(T, U_min, label='SCF')
axs[1].set_xlabel("time (ps)")
axs[1].set_ylabel(r"$U$" + " " + r"$(kcal/mol)$")
plt.legend()

plt.savefig("method_comp.png", dpi=700, bbox_inches="tight")
