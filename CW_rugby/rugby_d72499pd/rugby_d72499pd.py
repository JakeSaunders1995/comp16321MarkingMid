import sys, os

def count_scores(line):
    T1_score = 0
    T2_score = 0
    for i in range(2, len(line), 3):
        if line[i-2:i] == "T1":
            if line[i] == "t":
                T1_score += 5
            elif line[i] == "c":
                T1_score += 2
            elif line[i] == "d" or line[i] == "p":
                T1_score += 3
        elif line[i-2:i] == "T2":
            if line[i] == "t":
                T2_score += 5
            elif line[i] == "c":
                T2_score += 2
            elif line[i] == "d" or line[i] == "p":
                T2_score += 3
    result = str(T1_score) + ":" + str(T2_score)
    global winner
    if T1_score > T2_score:
        winner = "T1"
    elif T1_score == T2_score:
        winner = "draw"
    else:
        winner = "T2"
    return result

files = sys.argv
winner = ""
input_file_path = files[1]
output_file_path = files[2]
files_names = os.listdir(input_file_path)
count = 0
with os.scandir(input_file_path) as files:
    for entry in files:
        with open(entry, "r") as file:
            line = file.readline().rstrip()
            i = 0
            file_name = ""
            while files_names[count][i] != ".":
                file_name += files_names[count][i]
                i+=1
            file_name += "_d72499pd.txt"
            save_file = os.path.join(output_file_path, file_name)
            with open(save_file, "w") as output_file:
                output_file.write(count_scores(line))
            count += 1
