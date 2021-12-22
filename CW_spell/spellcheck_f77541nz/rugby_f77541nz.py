import os, argparse, re
from pathlib import Path

#takes folder input
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
parser.add_argument("destination_path", type=Path)
p = parser.parse_args()

add = 0
team = 0
T1Score = 0
T2Score = 0


#loops through folders files
for file in os.listdir(p.file_path):
      openedFile = open((str(p.file_path) + "/" + str(file)),"r")
      line = openedFile.read()
      openedFile.close()

      add = 0
      team = 0
      T1Score = 0
      T2Score = 0

      for x in range(0,len(line)):
          #looks at team
          if (x % 3) == 1:
              #chooses team
               if line[x] == "1":
                   team = 1
               else:
                   team = 2
          #looks at point type
          if (x % 3) == 2:
               #chooses point
              if line[x] == "t":
                  add = 5
              elif line[x] == "c":
                  add = 2
              elif line[x] == "p":
                  add = 3
              elif line[x] == "d":
                  add = 3
              if team == 1:
                  T1Score = T1Score + add
              elif team == 2:
                  T2Score = T2Score + add

      file = file.replace(".txt", "_f77541nz.txt", 1)
      openedFile = open((str(p.destination_path) + "/" + str(file)),"w")
      openedFile.write(str(T1Score))
      openedFile.write(":")
      openedFile.write(str(T2Score))
      openedFile.close()
