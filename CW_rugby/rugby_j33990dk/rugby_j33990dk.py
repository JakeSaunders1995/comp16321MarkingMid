import sys


# read file
file = open(sys.argv[1], "r")
line = file.readlines()
for line in line:
    print(line)

# create output file
newFile = open(sys.argv[2], "w")

# separate game

game = []

n=0
while n < len(line):
    game.append(line[n:n+3])
    n = n+3
print(game)

# define winner and score

winner = []
w=0
while w < len(line):
    winner.append(line[w: w+2])
    w = w+3

score=[]
s=2
while s<len(line):
    score.append(line[s])
    s = s+3

print(list(enumerate(winner)))
print(list(enumerate(score)))

# change scoring type to quantity
for i in range(len(score)):
    if "t" in score[i]:
        score[i] = 5
    elif "c" in score[i]:
        score[i] = 2
    elif "p" in score[i]:
        score[i] = 3
    elif "d" in score[i]:
        score[i] = 3

print(score)

# find which team win
T1_win = list(filter(lambda x: winner[x] == "T1", range(len(winner))))
print(T1_win)
T2_win = list(filter(lambda x: winner[x] == "T2", range(len(winner))))
print(T2_win)

T1_score = []
T2_score = []

# calculate team score
for i in (T1_win):
    T1_score.append(score[i])
print(T1_score)

for j in (T2_win):
    T2_score.append(score[j])
print(T2_score)

result1 = sum(T1_score)
print(result1)

result2 = sum(T2_score)
print(result2)

print("T1 : T2 = ", result1, ":", result2)

result = f'{result1}:{result2}'

# output file
newFile.write(result)

newFile.close()

file.close()