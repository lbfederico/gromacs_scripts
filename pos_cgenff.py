import os


# Definitions (or Functions)
def findfiles_ByExtension1(path, extension='_fix.mol2'):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(extension)]

# Create list of files
lista_bases1 = findfiles_ByExtension1(os.path.join(os.getcwd()), extension='_fix.mol2', )

# Definitions (or Functions)
def findfiles_ByExtension2(path, extension='_ini.pdb'):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(extension)]


# Print list

for base in lista_bases1:
	x = base.split('_')[0]
	cmd = 'python3' + ' ' + 'cgenff_charmm2gmx_py3.py' + ' ' +  x + ' ' +  x + '_fix.mol2' + ' ' + x + '.str' + ' ' + 'charmm36-mar2019.ff'
	os.system(cmd)
	
# Create list of files
lista_bases2 = findfiles_ByExtension2(os.path.join(os.getcwd()), extension='_ini.pdb', )
# Print list

for base in lista_bases2:
	x = base.split('_')[0]
	cmd = 'gmx' + ' ' + 'editconf' + ' ' + '-f' + ' ' + base + ' ' + '-o' + ' ' +x + '.gro'
	os.system(cmd)

