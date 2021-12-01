import sys
import os
folder_output= sys.argv[2]
folder_input = sys.argv[1]

if not os.path.isdir(folder_output):
	os.mkdir(folder_output)


for file in os.listdir(folder_input):
	with open(os.path.join(folder_input,file),"r") as file_input:
		inputstr=file_input.read()
	
		length=int(len(inputstr)/3)
		list=[""]*length

		def devide (list,inputstr):
			temp=0
			for i in range(len(list)):
				list[i]=inputstr[temp:temp+3]
				temp+=3
			return list
		def teams_total(list):
			total_t1=0
			total_t2=0
			for i in range(len(list)):
				if list[i][1]=="1":
					if list[i][2]=="t":
						total_t1+=5
					elif list[i][2]=="c":
						total_t1+=2
					elif list[i][2]=="p":
						total_t1+=3
					else:
						total_t1+=3
				else:
					if list[i][2]=="t":
						total_t2+=5
					elif list[i][2]=="c":
						total_t2+=2
					elif list[i][2]=="p":
						total_t2+=3
					else:
						total_t2+=3
			return total_t1,total_t2
		list=devide(list,inputstr)
		total1,total2=teams_total(list)
		result=str(total1)+":"+str(total2)
	with open(os.path.join(folder_output,os.path.basename(file)[:-4]+"_p80873ab"),"w") as file_output:
		file_output.write(result)


