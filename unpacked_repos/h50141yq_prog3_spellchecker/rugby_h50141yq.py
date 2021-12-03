import sys, os
input_path = sys.argv[1]
output_path = sys.argv[2]
for input_file in os.listdir(input_path):
    os.chdir(input_path)
    with open(input_file) as f:
        contents = f.read()
        T1 = 0
        T2 = 0
        x = 1
        times = len(contents)/3
        for i in range(int(times)):
            if contents[x] == "1":
                x+=1
                if contents[x] == "t":
                    T1 += 5
                if contents[x] == "c":
                    T1 += 2
                if contents[x] == "p":
                    T1 += 3
                if contents[x] == "d":
                    T1 += 3
            if contents[x] == "2":
                x += 1
                if contents[x] == "t":
                    T2 += 5
                if contents[x] == "c":
                    T2 += 2
                if contents[x] == "p":
                    T2 += 3
                if contents[x] == "d":
                    T2 += 3
            x += 2
        if T1 > T2:
            y = "T1 is the winner."
        if T1 < T2:
            y = "T2 is the winner."
        if T1 == T2:
            y = "T1 and T2 are tied."
        print(y)
        name = str(f.name)
        file_list = name.split('.')
        os.chdir(output_path)
        output_file = file_list[0]+"_h50141yq."+file_list[1]
        new = open(output_file, 'w')
        new.write(str(T1)+ ":"+ str(T2))
        new.close()
