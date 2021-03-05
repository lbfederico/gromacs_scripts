import os
import sys
import argparse
import textwrap


def Run(cmds):
    for x in d:
        path = os.path.abspath(x)
        os.chdir(path)
        for cmd in cmds:
            os.system(cmd)
        os.chdir(os.path.join('/'))


d = list(filter(os.path.isdir, os.listdir()))

center_cv = ('echo 1 0 |'
             ' gmx trjconv'
             ' -s md_sv_mdh.tpr'
             ' -f md_sv_mdh.xtc'
             ' -o md_center.xtc'
             ' -center'
             ' -pbc'
             ' mol'
             ' -ur compact'
             )

center_gp = ('echo 1 0 |'
             ' gmx trjconv'
             ' -s md_gp_mdh.tpr'
             ' -f md_gp_mdh.xtc'
             ' -o md_center.xtc'
             ' -center'
             ' -pbc mol'
             ' -ur compact'
             )

fit_sv = ('echo 4 0 |'
          ' gmx trjconv'
          ' -s md_sv_mdh.tpr'
          ' -f md_center.xtc'
          ' -o md_fit.xtc'
          ' -fit rot+trans'
          )

fit_gp = ('echo 4 0 |'
          ' gmx trjconv'
          ' -s md_gp_mdh.tpr'
          ' -f md_center.xtc'
          ' -o md_fit.xtc'
          ' -fit rot+trans'
          )

rmsd = ('echo 3 3 |'
        'gmx rms'
        ' -s md_sv_mdh.tpr'
        ' -f md_fit.xtc '
        '-o rmsd.xvg'
        ' -tu ns'
        )

rmsf = ('echo 4 4 |'
        ' gmx rmsf '
        '-s md_sv_mdh.tpr'
        ' -f md_fit.xtc'
        ' -o rmsf.xvg'
        ' -res'
        )

sasa = ('echo 1 |'
        ' gmx sasa '
        '-s md_sv_mdh.tpr'
        ' -f md_fit.xtc'
        ' -o sasa.xvg'
        )

gyrate = ('echo 1 |'
          ' gmx gyrate'
          ' -s md_sv_mdh.tpr'
          ' -f md_fit.xtc'
          ' -o gyrate.xvg'
          )

rmsd_lig = ('echo COLOCAR NUMERO LIGANTE |'
            'gmx rms'
            ' -s md_sv_mdh.tpr'
            ' -f md_fit.xtc '
            '-o lig_rmsd.xvg'
            ' -tu ns'
            )

if len(sys.argv) != 2:
    print('ERROR1: put sv_all, sv_trj or gp_trj')

elif sys.argv[1] == '-h':

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                     Script utilizado para automatizar análises dos resultados em uma série com muitos ligantes
                                     Ele atua nos diretórios acima ao dele
                                     sintaxe >> python3.9 analises.py arg
                                     arg = sv_all (acerto da trajetória, RMSD, RMSF (complex e ligante), SASA, Gyrate) -> para md_sv.tpr e md_sv.xtc
                                         = sv_trj apenas acerto da trajetória para os soltavados
                                         = gp_trj apenas acerto da trajetória para os gás phase
                                     ATENCAO!!!! NAO ESQUECER DE MUDAR -s e -f NO SCRIPT E ECHO do Ligante
                                    '''))

    args = parser.parse_args()



elif sys.argv[1] == str('sv_all'):
    x = (center_sv, fit_sv, rmsd, rmsf, sasa, gyrate, rmsd_lig)
    Run(x)

elif sys.argv[1] == str('sv_trj'):
    x = (center_sv, fit_sv)
    Run(x)

elif sys.argv[1] == str('gp_trj'):
    x = (center_gp, fit_gp)
    Run(x)

else:
    print('ERROR2: put sv_all, sv_trj or gp_trj')
