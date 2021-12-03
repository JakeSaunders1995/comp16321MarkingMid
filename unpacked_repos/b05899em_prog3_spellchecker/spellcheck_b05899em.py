import sys
import glob
import os
import re
file1=sys.argv[1]
file2=sys.argv[2]


path = os.path.abspath(file1)
files = glob.glob(path + "/*.txt")

for file in files:
	with open(file) as f:
		text=f.read()
		print(text)


#i got stuck with part1 and there is not possibility to complete this task as some code must be same as part1






path = os.path.abspath(file2)
newfile =open("text_file_b05899em.txt", "w")
newfile.write("solving hex is very easy in python")
newfile.close()


