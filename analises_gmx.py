import os
import sys

#argments(gmx flags)

d = list(filter(os.path.isdir, os.listdir()))
cmd1 = ('echo 1 0 | gmx trjconv -s md_sv_mdh.tpr -f md_sv_mdh.xtc -o md_center.xtc -center -pbc mol -ur compact')
cmd1_gp = ('echo 1 0 | gmx trjconv -s md_gp_mdh.tpr -f md_gp_mdh.xtc -o md_center.xtc -center -pbc mol -ur compact')
cmd2 = ('echo 4 0 | gmx trjconv -s md_sv_mdh.tpr -f md_center.xtc -o md_fit.xtc -fit rot+trans')
cm2_gp = ('echo 4 0 | gmx trjconv -s md_gp_mdh.tpr -f md_center.xtc -o md_fit.xtc -fit rot+trans')
cmd3 = ('echo 1 1 |gmx rms -s md_sv_mdh.tpr -f md_fit.xtc -o rmsd.xvg -tu ns')
cmd4 = ('echo 1 1 | gmx rmsf -s md_sv_mdh.tpr -f md_fit.xtc -o rmsf.xvg -res')
cmd5 = ('echo 1 | gmx sasa -s md_sv_mdh.tpr -f md_fit.xtc -o sasa.xvg')
cmd6 = ('echo 1 | gmx gyrate -s md_sv_mdh.tpr -f md_fit.xtc -o gyrate.xvg')


if len(sys.argv) != 2:
    print('ERROR: put sv_all, sv_trj or gp_trj')

elif sys.argv[1] == str('sv_all'):
    for x in d:
        path = os.path.abspath(x)
        os.chdir(path)
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
        os.system(cmd5)
        os.system(cmd6)
        os.chdir(os.path.join('../../'))

elif sys.argv[1] == str('sv_trj'):
    for x in d:
        path = os.path.abspath(x)
        os.chdir(path)
        os.system(cmd1)
        os.system(cmd2)
        os.chdir(os.path.join('../../'))

elif sys.argv[1] == str('gp_trj'):
    for x in d:
        path = os.path.abspath(x)
        os.chdir(path)
        os.system(cmd1_gp)
        os.system(cmd2_gp)
        os.chdir(os.path.join('../../'))

else:
    print('ERROR: put sv_all, sv_trj or gp_trj')