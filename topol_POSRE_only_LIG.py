import sys

#Função para encontrar numero da linha que contém o argumemnto desejado
def get_line(txt):
    file = open('topol.top', encoding='utf8')
    for line_num, value in enumerate(file, 1): #le todas as linhas e valores do file começando como 1
        if txt in value:                       #qdo encontra o 'txt' retorna o valor da linha
            return line_num

#Argumentos
lig = sys.argv[1]

#txt para encontrar o numero da linha e add após ou antes os argumentos .prm e .itp
x = str('; Include water topology')
y = str(f'; Ligand position restraints\n'
        f'#ifdef POSRES\n'
        f'#include "posre_{lig}.itp"'
        f'\n#endif\n\n')

#Abrir o topol.top -> Ler as linhas a add o argumento .prm
file = open('topol.top', 'r+', encoding='utf8')
line = file.readlines()
line.insert(get_line(x)-1, y)
file.seek(0)
file.writelines(line)
