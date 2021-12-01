import sys, re, os, glob

# make a list of the files in the input_folder directory
running_dir = __file__

main_dir, py_file =   os.path.split(running_dir)

start = sys.argv[1]
end = sys.argv[2]

input_dir = os.path.join( main_dir,start)
output_dir = os.path.join( main_dir,end)

list_file = os.listdir(input_dir)


# start data extraction from each folder in the list
for i in list_file:
    winner= "Waiting"

    file_name = os.path.join(os.getcwd(),start,i)

    open_file = open(file_name,"r")


    # replace T by #T to create a symbol for splitting br reading line by line
    for line in open_file:

        x = line.replace('T','#T')


		# start the split to separate each data by team T1 and T2
        splitting= x.split("#")

        # call score1 and score2 to store the scores of each team
        score1=0 
        score2=0

        t1= splitting.count("T1t")
        t2= splitting.count("T2t")
        p1= splitting.count("T1p")
        p2= splitting.count("T2p")
        d1= splitting.count("T1d")
        d2= splitting.count("T2d")
        c1= splitting.count("T1c")
        c2= splitting.count("T2c")

        #convert str to score in number
        if "T1t" in splitting: score1= score1+ (5*t1)

        if "T1p" in splitting: score1= score1+ (3*p1)
 
        if "T1d" in splitting: score1= score1+ (3*d1)

        if "T1c" in splitting: score1= score1+ (2*c1)

        if "T2t" in splitting: score2= score2 + (5*t2)

        if "T2p" in splitting: score2= score2 + (3*p2)
   
        if "T2d" in splitting: score2= score2 + (3*d2)

        if "T2c" in splitting: score2= score2 + (2*c2)
        if score1>score2:
           winner="T1"
        if score2>score1:
           winner="T2"
        if score1==score2:
           winner= "draw"
        
        # write output on the screen to .txt file in the output directory and change name
        new_i = i.replace('.txt', '_t02231ss.txt')
        target_output = open(os.path.join(output_dir, new_i),"wt")
        target_output.write(str(score1)), target_output.write(str(":")),target_output.write(str(score2))




      




























