import argparse
import os


    
n = 0

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Enter input folder name")
    parser.add_argument("output_file", help="Enter output folder name")
    args = parser.parse_args()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    files = os.listdir(folder)
    files.sort()
    
    for filename in files:
        file = os.path.join(folder, filename)
        
        openfile = open(file, "r")
        newval = openfile.read()
        stat = str(newval)
        listval = list()
        team1 = 0
        team2 = 0
        for i in range(0,len(stat),3):
            listval.append(stat[i:i+3])

        for score in listval:
            if score[1] == "1":
                if score[2] == "t":
                    team1 += 5
                if score[2] == "c":
                    team1 += 2
                if score[2] == "p":
                    team1 += 3
                if score[2] == "d":
                    team1 += 3

            else:
                if score[2] == "t":
                    team2 += 5
                if score[2] == "c":
                    team2 += 2
                if score[2] == "p":
                    team2 += 3
                if score[2] == "d":
                    team2 += 3    
        outval = (str(team1) + ":" + str(team2))
        out_name = files[n]
        out_name = out_name.replace(".txt", "_f06903rd.txt")
        final_out = os.path.join(outfolder, out_name)
        out_open = open(final_out, "w")
        out_open.write(outval)    
        n += 1