import sys
import os



inputfolder = sys.argv[1]
outputfolder = sys.argv[2]

t = 5
c = 2
p = 3
d = 3


startdirectory = os.getcwd() + inputfolder.replace('.', '')
os.chdir(startdirectory)

for inputfile in os.listdir():
   file = open(inputfile, 'r')
   line = file.read().rstrip()
   T1 = 0
   T2 = 0
   if "T1t" in line:
     count = line.count("T1t")
     T1 += count*5
   if "T1c" in line:
     count = line.count("T1c")
     T1 += count*2
   if "T1p" in line:
     count = line.count("T1p")
     T1 += count * 3
   if "T1d" in line:
     count = line.count("T1d")
     T1 += count * 3
   if "T2t" in line:
     count = line.count("T2t")
     T2 += count * 5
   if "T2c" in line:
     count = line.count("T2c")
     T2 += count * 2
   if "T2p" in line:
     count = line.count("T2p")
     T2 += count* 3
   if "T2d" in line:
     count = line.count("T2d")
     T2 += count * 3

   print("for file",inputfile, "the result was", T1, ":", T2, "RESULTS HAVE BEEN OUTPUTTED TO",outputfolder) 

   if T1 > T2:
      print("Winner was Team 1!")
   if T1 == T2:
      print("It was a draw!")
   if T2 > T1:
      print("Winner was Team 2!")





   os.chdir('..')
   if not os.path.exists(os.getcwd()  + outputfolder.replace('.', '')):
         os.makedirs(os.getcwd()  + outputfolder.replace('.', ''))
         os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

         f = open(inputfile + "_p80249ra.txt", 'w+')
         f.write(str(T1) + ":" + str(T2))
         f.close()
         os.chdir('..')
         os.chdir(startdirectory)

         file.close()
   else:
     os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

     f = open(inputfile + "_p80249ra.txt", 'w+')
     f.write(str(T1) + ":" + str(T2))
     f.close()
     os.chdir('..')
     os.chdir(startdirectory)

     file.close()
   







