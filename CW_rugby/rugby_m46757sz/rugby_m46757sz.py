import sys,os


def mk_paths(inpath,outpath):
    global in_paths, out_paths
    in_paths = []
    out_paths = []
    for i in os.listdir(inpath):
        if i[-4:] == ".txt":
            in_paths.append(inpath + "/" +i)
            out_paths.append(outpath + "/" + i[:-4] + "_m46757sz" + i[-4:])
    return

def out_paths(path,rp):
    paths = []
    for i in path:
        paths.append()

def read_file(path):
    global T1s,T2s
    with open(path,'r') as f:
        score = f.read()
        i = 0
        T1s = 0
        T2s = 0
        for s in range(int(len(score)/3)):
            if score[i:i+2] == "T1" :
                T1s = T1s + select_points(score[i+2])
            elif score[i:i+2] == "T2":
                T2s = T2s + select_points(score[i+2])
            else:
                pass
            i = i + 3
                
def output(path):
    with open(path,'w') as f:
        f.write("%d:%d"%(T1s,T2s))

def select_points(type):
    if type == "t":
        return 5
    elif type == "c":
        return 2
    elif type == "p":
        return 3
    elif type == "d":
        return 3
    else:
        return

def main(paths):
    mk_paths(paths[1],paths[2])
    for p in range(len(in_paths)):
        read_file(in_paths[p])
        output(out_paths[p])


if __name__ == "__main__":
    main(sys.argv)
