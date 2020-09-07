#Argumentos
import sys

prot = sys.argv[1]
lig = sys.argv[2]


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

file = open('complex.gro', 'a+')
file.writelines([item for item in lig_only])
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

