import sys
import argparse


#Função para encontrar numero da linha que contém o argumemnto desejado
def get_line(txt):
    file = open('topol.top', encoding='utf8')
    for line_num, value in enumerate(file, 1): #le todas as linhas e valores do file começando como 1
        if txt in value:                       #qdo encontra o 'txt' retorna o valor da linha
            return line_num





if len(sys.argv) == 2 and sys.argv[1] == '-h':
    

    parser = argparse.ArgumentParser(description= 'Este script deve ser rodado no diretorio em analise\n'
                                                  'Ele cria o arquivo complex.gro e faz as adequações ao topol.top\n'
                                                  'Usado para proteina e ligante ou proteina ligante e cofator\n'
                                                  'sintaxe -> python3.9 complex.py prot_name lig_name cof_name\n'
                                                  'as extensoes DEVEM ser adicionadas ao comando')

    args = parser.parse_args()


else:
    print('ERRO! em duvida acesse -h para help')



if len(sys.argv) > 4:
    print('ERROR: Please put protein ligand and cofactor names or -h for help. ')


#-----------------------------------------------------------------------------------------------------

elif len(sys.argv) == 3:
    prot = sys.argv[1]
    lig = sys.argv[2]
    lig2 = lig.rsplit('.', 1)[0]

    # Abre arquivo e lê prot
    file = open(str(prot), 'r')
    prot = file.readlines()

    # Criar complex, parte1 -> prot sem box vector (only_prot)
    file = open('complex.gro', 'a+')
    only_prot = prot[2:-1]
    file.writelines([item for item in only_prot])
    box_vector = prot[-1]
    file.close()

    # incluir ligante sem cabeçalho nem box vector -> incluir box vector
    # Abre arquivo e lê lig e complex
    file = open(str(lig), 'r')
    lig = file.readlines()
    lig_only = lig[2:-1]

    file = open('complex.gro', 'a+')
    file.writelines([item for item in lig_only])
    file.writelines([item for item in box_vector])
    file.close()

    # Verificar o numero de linhas (cont) e a linha2 - como esta sem cabeçalho o numero de moleculas é cont -1
    file = open('complex.gro', 'r')
    line = file.readlines()
    cont = len(line)
    file.close()

    # Substituir o numero de linhas e o nome inicial
    file = open('complex.gro', 'w')
    file.write('complex' + '\n')
    file.write(str(cont - 1) + '\n')
    file = open('complex.gro', 'a')
    file.writelines(line)
    file.close()

#--------------------------------------------------------------------------------------------


    x = str('#include "./charmm36-mar2019.ff/forcefield.itp"')
    y = str('; Include Position restraint file')
    z = str('Protein             1')
    


    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(x), f'\n; Include ligand parameters\n#include "{lig2}.prm"\n')
    file.seek(0)
    file.writelines(line)

    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(y) + 4, f'; Include ligand topology\n#include "{lig2}.itp"\n\n')
    file.seek(0)
    file.writelines(line)

    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(z), f'\n{lig2}                 1\n')
    file.seek(0)
    file.writelines(line)

#---------------------------------------------------------------------------------------------

elif len(sys.argv) == 4:
    prot = sys.argv[1]
    lig = sys.argv[2]
    cof = sys.argv[3]
    lig2 = lig.rsplit('.', 1)[0]
    cof2 = cof.rsplit('.', 1)[0]


    # Abre arquivo e lê prot
    file = open(str(prot), 'r')
    prot = file.readlines()

    #Criar complex, parte1 -> prot sem box vector (only_prot)
    file = open('complex.gro', 'a+')
    only_prot = prot[2:-1]
    file.writelines([item for item in only_prot])
    box_vector = prot[-1]
    file.close()

    #incluir ligante sem cabeçalho nem box vector -> incluir box vector
    #Abre arquivo e lê lig e complex
    file = open(str(lig), 'r')
    lig = file.readlines()
    lig_only = lig[2:-1]

    file = open(str(cof), 'r')
    cof = file.readlines()
    cof_only = cof[2:-1]

    file = open('complex.gro', 'a+')
    file.writelines([item for item in lig_only])
    file.writelines([item for item in cof_only])
    file.writelines([item for item in box_vector])
    file.close()

    #Verificar o numero de linhas (cont) e a linha2 - como esta sem cabeçalho o numero de moleculas é cont -1
    file = open('complex.gro', 'r')
    line = file.readlines()
    cont = len(line)
    file.close()

    #Substituir o numero de linhas e o nome inicial
    file = open('complex.gro', 'w')
    file.write('complex' + '\n')
    file.write(str(cont -1)+ '\n')
    file = open('complex.gro', 'a')
    file.writelines(line)
    file.close()

#-----------------------------------------------------------------
    

    x = str('#include "./charmm36-mar2019.ff/forcefield.itp"')
    y = str('; Include Position restraint file')
    z = str('Protein             1')

    # Abrir o topol.top -> Ler as linhas a add o argumento .prm
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(x), f'\n; Include ligand parameters\n#include "{lig2}.prm"\n#include "{cof2}.prm"\n')
    file.seek(0)
    file.writelines(line)

    # Abrir o topol.top -> Ler as linhas a add o argumento .itp
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(y) + 4, f'; Include ligand topology\n#include "{lig2}.itp"\n#include "{cof2}.itp"\n\n')
    file.seek(0)
    file.writelines(line)
    # Abrir o topol.top -> Ler as linhas a add o argumento numero de moleculas finais
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(z), f'\n{lig2}                 1\n{cof2}                 1\n')
    file.seek(0)
    file.writelines(line)
