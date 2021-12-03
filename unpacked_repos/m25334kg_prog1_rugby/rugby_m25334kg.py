import argparse
import os


try:
	parser=argparse.ArgumentParser()
	parser.add_argument("input_folder",help="path of the input folder with team scores",type=str)
	parser.add_argument("output_folder",help="path of output folder to store final score",type=str)
	folders=parser.parse_args()

	fol_in=folders.input_folder
	fol_out=folders.output_folder

	input_files=os.listdir(fol_in)

	for file in input_files:

		f_in=open(fol_in+"/"+file)
		output_file= file.rstrip(".txt")+ "_m25334kg" + ".txt"
		f_out=open(fol_out+"/"+output_file,"w")

		scores=f_in.read()

		team1=0
		team2=0
		i=0
		while i<len(scores):
			team=scores[i:i+2]
			point=scores[i+2].lower()
			if point=="t":
				point=5
			elif point=="c":
				point=2
			elif point=="p":
				point=3
			elif point=="d":
				point=3
			else:
				point=0

			if team=="T1":
				team1+=point
			elif team=="T2":
				team2+=point
			else:
				continue
			i+=3

		if team1>team2:
			winner="T1"
			print(winner,"won",end= " ")
		elif team2>team1:
			winner="T2"
			print(winner,"won", end=" ")
		else:
			winner="draw"
			print("It is a draw", end= " ")

		print("in the match",file)

		final_score=str(team1)+":"+str(team2)
		f_out.write(final_score)
		f_in.close()
		f_out.close()


except SyntaxError as Error:
	print(Error)

except Exception as err:
	print("Sorry something went wrong!")