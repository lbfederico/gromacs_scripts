import sys

if len(sys.argv) < 3:
    print('ERROR: Please put protein and ligand name with extension')

elif len(sys.argv) > 3:
    print('ERROR: Please put only protein and ligand name, to ligand and cofactor use complex_lig_cof.py')


else:
  #Arguments
  prot = sys.argv[1]
  lig = sys.argv[2]


  # Open file and read prot
  file = open(str(prot), 'r')
  prot = file.readlines()

  #Build complex, part1 -> prot without box vector (only_prot)
  file = open('complex.gro', 'a+')
  only_prot = prot[2:-1]
  file.writelines([item for item in only_prot])
  box_vector = prot[-1]
  file.close()

  #Add ligand without title and box vector -> include box vector
  #Abre arquivo e lê lig e complex
  file = open(str(lig), 'r')
  lig = file.readlines()
  lig_only = lig[2:-1]

  file = open('complex.gro', 'a+')
  file.writelines([item for item in lig_only])
  file.writelines([item for item in box_vector])
  file.close()

  #Check the number of lines  (cont) and line2 - (as this without title the number of molecules is cont -1)
  file = open('complex.gro', 'r')
  line = file.readlines()
  cont = len(line)
  file.close()

  #Replace the number of lines and the initial name
  file = open('complex.gro', 'w')
  file.write('complex' + '\n')
  file.write(str(cont -1)+ '\n')
  file = open('complex.gro', 'a')
  file.writelines(line)
  file.close()

