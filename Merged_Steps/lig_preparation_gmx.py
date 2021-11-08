from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import time
import argparse
import textwrap

#def para procurar os _fix.mol2 e os todos os arqivos de cada ligante (Ls)

def FindFilesEnd(path, sufix):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.endswith(sufix)]

def FindFilesStart(path, prefix):
    filenames = os.listdir(path)
    return [filename for filename in filenames if filename.startswith(prefix)]

 
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
                                             Utilizar Python3. Script utilizado para automatizar o tratamento dos ligantes
                                             Entrada em .mol2 utiliza o Script Perl para correcao das moleculas e gerar _fix.mol2
                                             Entra no site CGenFF, cria o arquivo .srt e converte com o script cgenff_charmm2gmx
                                             Utiliza o gmx editiconf para criar o .gro
                                             salva todos os resltados para cada ligante em respectivos diretorios criados
                                             '''))

args = parser.parse_args()


lista_molecMol2 = FindFilesEnd(os.path.join(os.getcwd()), '.mol2')

for molecMol2 in lista_molecMol2:
     molec_without_ext= os.path.splitext(molecMol2)[0]
     cmd = 'perl' + ' '\
           + 'sort_mol2_bonds.pl' + ' '\
           + molecMol2 + ' '\
           + molec_without_ext + '_fix.mol2'
     os.system(cmd)

FixMol2 = FindFilesEnd(os.path.join(os.getcwd()), '_fix.mol2')

#Abrir pagina CGenFF
browser = webdriver.Chrome()
browser.get("https://cgenff.umaryland.edu/userAccount/userLogin.php")
element = EC.visibility_of_element_located((By.ID, 'username'))
assert 'User' in browser.title #confirmar se a pag foi aberta

#login
username = browser.find_element_by_name('usrName')
password = browser.find_element_by_name('curPwd')
username.send_keys("******")
password.send_keys("*******")
#password.send_keys(Keys.RETURN)

#clicar no botão submit
login_attempt = browser.find_element_by_name('submitBtn')
login_attempt.submit()
element = EC.visibility_of_element_located((By.NAME, 'filename'))

#Loop para cada um dos fix.mol2
for molecFix in FixMol2:
    assert 'Upload' in browser.title #confirmar se esta na pag de download
#input file
    file_input = browser.find_element_by_name('filename')
    file_input.send_keys(os.path.join(os.getcwd(), molecFix))
    up = browser.find_element_by_id('submit')
    browser.execute_script("arguments[0].click();", up)
#nova pag, esperar pelo 'str' e clicar nele
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'str')))
    out = browser.find_element_by_partial_link_text('str').click()

#copiar o txt e criar arquivo .str
    browser.switch_to.window(browser.window_handles[1]) #mudar de aba
    txt = browser.find_element_by_css_selector('body').text
    molecname = molecFix.split('_')[0]
    x = open(molecname + '.str', 'w')
    x.writelines(txt)
    x.close()

#fechar aba
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

#Rodar script cegenff e gmx edit conf

    cmd2 = 'python3' + ' '\
          + 'cgenff_charmm2gmx_py3.py' + ' '\
          + molecname + ' '\
          + molecFix + ' '\
          + molecname + '.str' + ' ' \
          + 'charmm36-mar2019.ff'

    cmd3 = 'gmx' + ' ' \
           + 'editconf' + ' ' \
           + '-f' + ' ' + molecname + '_ini.pdb' + ' '\
           +'-o' + ' ' + molecname + '.gro'
    os.system(cmd2)
    os.system(cmd3)



#criar diretorio e mover resultados

    path_out = os.path.join(os.getcwd(), molecname)
    [os.makedirs(i, exist_ok=True) for i in [path_out]]

    all_prefix = FindFilesStart(os.path.join(os.getcwd()), molecname)
    for results in all_prefix:
        shutil.move(os.path.join(os.getcwd(), results), path_out)
