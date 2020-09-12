import sys

def get_line(txt):
    file = open('topol.top', encoding='utf8')
    for line_num, value in enumerate(file, 1): 
        if txt in value:                       
            return line_num
        
        
if len(sys.argv) < 2:
    print('ERROR: put lig name without extension')

elif len(sys.argv) > 2:
    print('ERROR: put only lig name without extension')

else:
    lig = sys.argv[1]
    x = str('; Include water topology')
    y = str(f'; Ligand position restraints\n'
            f'#ifdef POSRES\n'
            f'#include "posre_{lig}.itp"'
            f'\n#endif\n\n')


    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(x)-1, y)
    file.seek(0)
    file.writelines(line)
