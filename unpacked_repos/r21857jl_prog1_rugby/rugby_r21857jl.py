import argparse
import os

def parse_chunk(chunk: str):
    assert(len(chunk) == 3)
    team = chunk[0:2]
    ty = chunk[2:3]
    if ty == "t":
        points = 5
    elif ty == "c":
        points = 2
    elif ty == "p":
        points = 3
    elif ty == "d":
        points = 3
    return (team, points)

def work(ipath, opath):
    t1, t2 = 0, 0
    with open(ipath) as ifile:
        contents = ifile.readline().strip()
        for i in range(0, len(contents), 3):
            chunk = contents[i:i+3]
            team, points = parse_chunk(chunk)
            if team == "T1":
                t1 += points
            else:
                t2 += points

    # compare results
    if t1 == t2:
        print("draw")
    elif t1 > t2:
        print("Team 1 wins!")
    else:
        print("Team 2 wins!")

    # write results
    with open(opath, "w+") as ofile:
        ofile.write(f"{t1}:{t2}")

    pass

def main(args):
    ifiles = os.listdir(args.input_dir)
    for ipath in ifiles:
        if ipath.endswith(".txt"):
            opath = f"{ipath.rstrip('.txt')}_r21857jl.txt"
            
            ipath = os.path.join(args.input_dir, ipath)
            opath = os.path.join(args.output_dir, opath)

            work(ipath, opath)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()
    main(args)