import argparse
import os

def mainargparse():
    par = argparse.ArgumentParser()
    par.add_argument('inp')
    par.add_argument('out')
    a = par.parse_args()
    return a.inp, a.out

def compare(inpath, outpath):
    # read the file
    with open(inpath) as inf:
        rec = inf.readline().strip()
    team1 = 0
    team2 = 0
    n = 0
    while n < len(rec):
        team = rec[n + 1]
        sco = rec[n + 2]
        if sco == 't':
            if team == '1':
                team1 += 5
            else:
                team2 += 5
        elif sco == 'p' or sco == 'd':
            if team == '1':
                team1 += 3
            else:
                team2 += 3
        else:
            if team == '1':
                team1 += 2
            else:
                team2 += 2
        n += 3

    with open(outpath, 'w') as outf:
        outf.write('{}:{}'.format(team1, team2))

if __name__ == '__main__':

    inp, out = mainargparse()
    list = os.listdir(inp)
    for file in list:
        input = os.path.join(inp, file)
        outpath = os.path.abspath(out)
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        output = os.path.join(outpath,
                                   os.path.splitext(file)[0] + '_x36049yl.txt')
        compare(input, output)
