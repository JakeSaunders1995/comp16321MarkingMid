import argparse, os

arg_parser= argparse.ArgumentParser()
arg_parser.add_argument("inpath")
arg_parser.add_argument("outpath")
arguments= arg_parser.parse_args()
folder= os.listdir(arguments.inpath)

for i in folder:

	count=int(0)
	T1_points=int(0)
	T2_points=int(0)
	input_path= os.path.join(arguments.inpath, i)
	output_path= str(arguments.outpath + "/" + i[:10] + "_s62508as" + i[10:])


	with open(input_path, "r") as f:
		lines= int(len(f.readline()))
	f=open(input_path, "r")
	while count<lines:
			count+=3
			team= str(f.read(2))
			types= str(f.read(1))
			if "T1" in team:
				if types=="t":
					T1_points+=5
				elif types=="c":
					T1_points+=2
				elif types=="p" or "d":
					T1_points+=3
				else:
					print("Error reading score type")
			elif "T2" in team:
				if types=="t":
					T2_points+=5
				elif types=="c":
					T2_points+=2
				elif types=="p" or "d":
					T2_points+=3
				else:
					print("Error reading score type")
			else:
				print("")
			
	with open(output_path, "w") as g:
		g.write(str(T1_points) + ":" + str(T2_points))




