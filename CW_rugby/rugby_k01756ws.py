import sys, os

filenames = os.listdir(sys.argv[1])
for input_file in filenames:
    with open(sys.argv[1] + "/" + input_file) as f:
        game = f.read()

    t1_score = 0
    t2_score = 0

    count = 1
    while count < len(game):
        score_type = game[count + 1]
        temp_score = 3
        if score_type == "t":
            temp_score = 5
        elif score_type == "c":
            temp_score = 2

        if game[count] == "1":
            t1_score += temp_score
        else:
            t2_score += temp_score

        count += 3

        output_filename = sys.argv[2] + "/" + input_file[:-4] + "_k01756ws.txt"

    with open(output_filename, 'w') as f:
        f.write(str(t1_score) + ':' + str(t2_score))