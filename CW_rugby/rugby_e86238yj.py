import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('input_path', metavar='path')
parser.add_argument('output_path',metavar='path')
args = parser.parse_args()

dirs = os.listdir(args.input_path)
os.mkdir(args.output_path)
for file in dirs:
    a = os.getcwd()
    name = file[:-4]
    f1 = open(str(args.input_path)+'/'+str(file),'r')
    f = f1.read()
    f1.close()
    t1 = 0
    t2 = 0
    score = f.split('T')
    for each in score:
        if each == '1t':
            t1 += 5
        if each == '1d' or each == '1p':
            t1 += 3
        if each == '1c':
            t1 += 2
        if each == '2t':
            t2 += 5
        if each == '2d' or each == '2p':
            t2 += 3
        if each == '2c':
            t2 += 2
    os.chdir(args.output_path)
    f2 = open(str(name)+'_e86238yj','w')
    f2.write(str(t1)+':'+str(t2))
    f2.close()
    os.chdir(a)







