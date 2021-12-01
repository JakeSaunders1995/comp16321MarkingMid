    
import argparse

def main(input, output):
    score = [0, 0]
    k = {'t': 5, 'c': 2, 'p': 3, 'd': 3}
    with open(input, 'r') as f:
        mode = 0
        for s in f.readline():
            if s == 'T':
                continue
            elif s == '1':
                mode = 0
            elif s == '2':
                mode = 1
            else:
                score[mode] += k.get(s)
    with open(output, 'w') as f:
        f.write(':'.join((str(score[0]), str(score[1]))))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()
    main(args.input, args.output)
