import sys


def get_line(txt):
    file = open('topol.top', encoding='utf8')
    for line_num, value in enumerate(file, 1): 
        if txt in value:                       
            return line_num

        
if len(sys.argv) < 3:
    print('ERROR: put lig and cof names without extension')
    
else:        
    lig = sys.argv[1]
    cof = sys.argv[2]

    x = str('; Include water topology')
    y = str(f'; Ligand position restraints\n'
            f'#ifdef POSRES\n'
            f'#include "posre_{lig}.itp"'
            f'\n#include "posre_{cof}.itp"'
            f'\n#endif\n\n')

    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(x)-1, y)
    file.seek(0)
    file.writelines(line)
