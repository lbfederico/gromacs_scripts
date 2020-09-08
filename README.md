# gmx_scripts
Simple scripts for automating some steps of Justin A. Lemkul's tutorial for GMX. Useful mainly for simulations with large series of ligands.

-> Topology Ligands

fix.py - Searches for '.mol2' files and run the script 'sort_mol2_bonds.pl' generating the '_fix.mol2'.

pos_cgenff.py - Use after generating '.str' on CGenff site - Script searches for '_fix.mol2' and '.str' runs the 'cgenff_charmm2gmx_py3.py' script to generate the '_ini.pdb' used in the sequence by 'editconf' to generate '.gro


-> Topology Complex 

Complex.py - The script merge prot.gro with lig.gro (or lig and cof) keeps the box_vector of prot and changes the total number of molecules at the beginning of the file.

          python3 complex.py prot.gro lig.gro

          python3 complex.py prot.gro lig.gro cof.gro

remove_SOL.py - For gas-phase simulations, input solv_ions.gro and the script remove SOL from the file, change the final number of molecules and return prot_ions.gro.


-> Topols

          python3 topol_<>.py lig cof
          (do not put extension)

Depending on topol_ it includes ligand parameters , ligand topology and molecules at the end of the file or position restraints 

