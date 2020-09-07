import os


# Definitions (or Functions)
def findfiles_ByExtension(path, extension='.mol2'):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(extension)]


# Create list of files
lista_bases = findfiles_ByExtension(
    os.path.join(os.getcwd()), extension='.mol2', )

# Print list
for base in lista_bases:
    x = os.path.splitext(base)[0]
    cmd = 'perl' + ' ' + 'sort_mol2_bonds.pl' + ' ' + base + ' ' + x + '_fix.mol2'
    os.system(cmd)
