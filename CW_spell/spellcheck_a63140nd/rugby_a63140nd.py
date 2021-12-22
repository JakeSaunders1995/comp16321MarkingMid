import os
d= os.getcwd()
fname= os.path.join(d, "midterm_files/Example_inputs/Example_inputs_program1/test_file1.txt")
file = open(fname, "r")
results = file.read()
file.close()
print (results)
t1_points= 0
t2_points= 0
split_strings = []
n  = 3
for index in range(0, len(results), n):
    split_strings.append(results[index : index + n])
team = 0
for i in range (0, (len(split_strings))):
    if split_strings[team][1] == "1":
        if split_strings[team][2] == "t":
            t1_points = t1_points + 5
        elif split_strings[team][2] == "c":
            t1_points = t1_points + 2
        elif split_strings[team][2] == "p":
            t1_points = t1_points + 3
        elif split_strings[team][2] == "d":
            t1_points = t1_points + 3
        team = team + 1
    else:
        if split_strings[team][2] == "t":
            t2_points = t2_points + 5
        elif split_strings[team][2] == "c":
            t2_points = t2_points + 2
        elif split_strings[team][2] == "p":
            t2_points = t2_points + 3
        elif split_strings[team][2] == "d":
            t2_points = t2_points + 3
        team = team + 1
outFileName= os.path.join(d, "midterm_files/output_files/output_program1/output_file1.txt")
with open(outFileName, 'w') as f:
    f.write(str(t1_points) + ":" + str(t2_points))
