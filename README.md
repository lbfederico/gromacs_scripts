# gmx_scripts(Gromacs)
Simple scripts for automating some steps of Justin A. Lemkul's tutorial for Gromacs. Useful mainly for simulations with large series of ligands.


### Step_by_Step Folder ###

-> Topology Ligands

*Fix.py
- Searches for '.mol2' files and run the script 'sort_mol2_bonds.pl' generating the '_fix.mol2'.

          python3 fix.py 
          
*pos_cgenff.py
- Use after generating '.str' on CGenff site - Script searches for '_fix.mol2' and '.str' runs the 'cgenff_charmm2gmx_py3.py' script to generate the '_ini.pdb' used in the sequence by 'editconf' to generate '.gro

          python3 pos_cgenff.py



-> Topology Complex 

*complex.py 
- The script merge prot.gro with lig.gro (or lig and cof) keeps the box_vector of prot and changes the total number of molecules at the beginning of the file.

          python3 complex.py prot.gro lig.gro

          python3 complex.py prot.gro lig.gro cof.gro
          
*topol_lig.py and topol_lig_cof.py
- Depending on topol_ it includes ligand parameters , ligand topology and molecules at the end of the file or position restraints 

          python3 topol_lig.py lig 
          python3 topol_lig_cof.py lig cof
          (do not put extension)
          
*topol_POSRE_lig.py and tpol_POSRE_lig_cof.py
- Restraining the Ligand Step - Include the position restraint topology information in our topology file.
- Restrain only ligand whenever but if you want a bit more control during equilibration, i.e. restraining the protein and ligand independently, change #ifdef POSRES to #ifdef POSRES_LIG in script file
          
          python3 topol_POSRE_lig.py
          python3 topol_POSRE_lig_cof.py
 
 
          

*remove_SOL.py 
- For gas-phase simulations, input solv_ions.gro and the script remove SOL from the file, change the final number of molecules and return prot_ions.gro.
          
          python3 remove_SOL.py




### Merged_Steps Folder ###

*LigPreparationGMX.py

- The three steps above in only one.
- Automates the preparation of ligand. Download script sort_mol2_bonds.pl and cgenff_charmm2gmx.py for use this.
- Putting the script in the directory with ligands in .mol2.
- It perform the script sort_mol2_bonds.pl obtain fix.mol2 obtain the .str file from CGenFF website runs the script cgenff_charmm2gmx and generates the .gro file by editconf.
- Finally creates directories for the results of each ligand.

          python3 LigPreparationGMX.py



*complex_topol.py

- This script must be run in the directory under analysis. It creates the complex.gro file and makes adjustments to topol.top. Used for protein and ligand or protein ligand and cofactor.
- Extensions MUST be added.

          python3 complex.py prot_name lig_name lig_name cof_name



*analises_gmx.py
- Obtains only the "center" and/or "fit" trajectory for solvent or gas-phase complexes (pcouple = no, only nvt equilibrium) with sv_trj and gp_trj or sv_all = RMSD, RMSF, SASA, Gyrate.
- Changing the name of the .tpr in "cmd"

          python3 analises_gmx.py <sv_all or sv_trj or gp_trj>





