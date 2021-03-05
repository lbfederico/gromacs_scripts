import os
import argparse
import textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
                                                            Este script deve ser rodado no diretorio abaixo aos em analise
                                                            Ele acessa os diretorios acima ao dele e cria o arquivo
                                                            pro_ions.gro e retira a linha SOL do topol.top
                                                            sintaxe -> python3 retirar_SOl.py
                                                            '''))

args = parser.parse_args()



#listar diretórios acima
all_dir = list(filter(os.path.isdir, os.listdir()))

#loop

for x in all_dir:
    path = os.path.abspath(x)
    os.chdir(path)

    #Ler linhas que nao contenham SOL -> Criar prot_ions.gro e add linhas sem SOL
    with open('solv_ions.gro', 'r') as f:
        f.seek(0)
        new_f = f.readlines()[2:]
        for line in new_f:
            if 'SOL' not in line:
                file = open('prot_ions.gro', 'a+')
                file.write(line)
        f.close()


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

    #abrir topol.top retira SOL
    file = open('topol.top', encoding='utf8')
    lines = file.readlines()
    file = open('topol.top', 'w')
    for x in lines:
        if 'SOL' not in x:
            file.write(x)
    file.close()
    os.chdir(os.path.join('../'))


