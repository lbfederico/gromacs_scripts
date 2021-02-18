import os
import sys
import argparse

cmd1_sv = ('echo 1 0 |'
           ' gmx trjconv'
           ' -s md_sv_mdh.tpr'
           ' -f md_sv_mdh.xtc'
           ' -o md_center.xtc'
           ' -center'
           ' -pbc'
           ' mol'
           ' -ur compact'
           )

cmd1_gp = ('echo 1 0 |'
           ' gmx trjconv'
           ' -s md_gp_mdh.tpr'
           ' -f md_gp_mdh.xtc'
           ' -o md_center.xtc'
           ' -center'
           ' -pbc mol'
           ' -ur compact'
           )

cmd2_sv = ('echo 4 0 |'
           ' gmx trjconv'
           ' -s md_sv_mdh.tpr'
           ' -f md_center.xtc'
           ' -o md_fit.xtc'
           ' -fit rot+trans'
           )

cmd2_gp = ('echo 4 0 |'
           ' gmx trjconv'
           ' -s md_gp_mdh.tpr'
           ' -f md_center.xtc'
           ' -o md_fit.xtc'
           ' -fit rot+trans'
           )

cmd3_sv = ('echo 4 4 |'
           'gmx rms'
           ' -s md_sv_mdh.tpr'
           ' -f md_fit.xtc '
           '-o rmsd.xvg'
           ' -tu ns'
           )

cmd4_sv = ('echo 4 4 |'
           ' gmx rmsf '
           '-s md_sv_mdh.tpr'
           ' -f md_fit.xtc'
           ' -o rmsf.xvg'
           ' -res'
           )

cmd5_sv = ('echo 1 |'
           ' gmx sasa '
           '-s md_sv_mdh.tpr'
           ' -f md_fit.xtc'
           ' -o sasa.xvg'
           )

cmd6_sv = ('echo 1 |'
           ' gmx gyrate'
           ' -s md_sv_mdh.tpr'
           ' -f md_fit.xtc'
           ' -o gyrate.xvg'
           )

cmd7_sv = ('echo COLOCAR NUMERO LIGANTE |'
        'gmx rms'
        ' -s md_sv_mdh.tpr'
        ' -f md_fit.xtc '
        '-o rmsd.xvg'
        ' -tu ns'
         )

only_directories = list(filter(os.path.isdir, os.listdir()))


def RunAnalysis(cmds):
    for each_directory in only_directories:
        path = os.path.abspath(each_directory)
        os.chdir(path)
        for cmd in cmds:
            os.system(cmd)
        os.chdir(os.path.join('../'))


if len(sys.argv) != 2:
    print('ERROR1: put sv_all, sv_trj or gp_trj')


elif sys.argv[1] == '-h':

    parser = argparse.ArgumentParser(
        description='Script utilizado para automatizar análises dos resultados em uma série com muitos ligantes/\n'
                    'Ele atua nos diretórios acima ao dele/\n'
                    'sintaxe >> python3.9 analises.py arg/\n'
                    'arg = sv_all (acerto da trajetória, RMSD, RMSF, SASA, Gyrate) -> para md_sv.tpr e md_sv.xtc/\n'
                    '    = sv_trj apenas acerto da trajetória para os soltavados/\n'
                    '   = gp_trj apenas acerto da trajetória para os gás phase/'
                    'ATENCAO!!!! NAO ESQUECER DE MUDAR -s e -f NO SCRIPT')

    args = parser.parse_args()




elif sys.argv[1] == str('sv_all'):
    x = (cmd1_sv, cmd2_sv, cmd3_sv, cmd4_sv, cmd5_sv, cmd6_sv, cmd7_sv)
    RunAnalysis(x)

elif sys.argv[1] == str('sv_trj'):
    x = (cmd1_sv, cmd2_sv)
    RunAnalysis(x)

elif sys.argv[1] == str('gp_trj'):
    x= (cmd1_gp, cmd2_gp)
    RunAnalysis(x)

else:
    print('ERROR2: put sv_all, sv_trj or gp_trj')
