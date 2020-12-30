import sys

if len(sys.argv) < 4:
    print('ERROR: Please put protein ligand and cofactor names. ')

else:
    prot = sys.argv[1]
    lig = sys.argv[2]
    cof = sys.argv[3]


    # Open and read protein file
    file = open(str(prot), 'r')
    prot = file.readlines()

    #Build complex, Part1 -> prot without box vector (only_prot)
    file = open('complex.gro', 'a+')
    only_prot = prot[2:-1]
    file.writelines([item for item in only_prot])
    box_vector = prot[-1]
    file.close()

    #Add ligand without title and box vector -> add box vector
    #Open and read lig and complex
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

    #Check number of lines (cont) and line2 - as this one without title the number of molecules is cont -1
    file = open('complex.gro', 'r')
    line = file.readlines()
    cont = len(line)
    file.close()

    #Replace number of lines and title
    file = open('complex.gro', 'w')
    file.write('complex' + '\n')
    file.write(str(cont -1)+ '\n')
    file = open('complex.gro', 'a')
    file.writelines(line)
    file.close()

