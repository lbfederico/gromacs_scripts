#Ler linhas que nao contenham SOL -> Criar prot_ions.gro e add linhas sem SOL
with open('solv_ions.gro', 'r') as f:
    f.seek(0)
    new_f = f.readlines()[2:]
    for line in new_f:
        if 'SOL' not in line:
            file = open('prot_ions.gro', 'a+')
            file.write(line)
    f.close()
#Retirar linhas se houverem linhas em branco no final do arquivo


#Ler prot_ions.gro e contar numero de linhas
file = open('prot_ions.gro', 'r')
num_linhas = file.readlines()
cont = len(num_linhas)
file.close()

#modificar numero de moléculas e nome de prot_ions
file = open('prot_ions.gro', 'w')
file.seek(0)
file.write('prot in gas-phase' + '\n')
file.write(str(cont -1) + '\n')
file.close()
#adicionar o prot_ions
file = open('prot_ions.gro', 'a')
file.writelines(num_linhas)
file.close





