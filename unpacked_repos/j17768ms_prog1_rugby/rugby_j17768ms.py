import argparse
import os

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Enter input folder: ")
    parser.add_argument("output_file", help="Enter output folder: ")
    args = parser.parse_args()
    folder = str(args.input_file)
    outfolder = str(args.output_file)
    files = os.listdir(folder)

    print(files)
    
    for file in files:
        my_file = open(folder + "/" + file, "r")

        content = my_file.read()

        print(content)

        st=str(content)

        T1l = []
        T2l = []
        t = 5 
        c = 2 
        p = 3 
        d = 3
        stp = st.split('T')
        stp.pop(0)
        char = [x[0] for x in stp]
        if char[0] == ("1"):
            T1l.append(stp[0][1])
        else:
            T2l.append(stp[0])
        if char[1] == ("1"):
            T1l.append(stp[1][1])
        else:
            T2l.append(stp[1][1])
        if char[2] == ("1"):
            T1l.append(stp[2][1])
        else:
            T2l.append(stp[2][1])
        if char[3] == ("1"):
            T1l.append(stp[3][1])
        else:
            T2l.append(stp[3][1])
        if char[4] == ("1"):
            T1l.append(stp[4][1])
        else:
            T2l.append(stp[4][1])

        print(T1l)

        T1l = [d if i=='d' else i for i in T1l]
        T1l = [p if i=='p' else i for i in T1l]
        T1l = [c if i=='c' else i for i in T1l]
        T1l = [t if i=='t' else i for i in T1l]
        print(T1l)

        T2l = [d if i=='d' else i for i in T2l]
        T2l = [p if i=='p' else i for i in T2l]
        T2l = [c if i=='c' else i for i in T2l]
        T2l = [t if i=='t' else i for i in T2l]

        a = str(sum(T1l))
        b = str(sum(T2l))

        y = (a+":"+b)
        temp = file.split(".")
        output_file_name = temp[0] + "_" + "j17768ms" + "." + temp[1]
        outputfile = open(outfolder + "/" + output_file_name, "w+")
        outputfile.write(y)















