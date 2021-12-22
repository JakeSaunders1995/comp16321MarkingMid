import random
theWords = []
difficulty = input("select difficulty 1.Easy 2.Medium 3.Hard")
file = open("EnglishWords.txt", "r")
for line in file:
	line = line.rstrip()
	theWords.append(line)
	word = random.choice(theWords)
while difficulty == 1 and len(word) > 6:
	word = random.choice(theWords)
while difficulty == 2 and len(word) < 7 and len(word) > 10 :
	word = random.choice(theWords)
while difficulty == 3 and len(word) < 11:
	word = random.choice(theWords)
answer = list()
guessed = list()
for x in word:
	answer.append("_")
	guessed.append(False)
correct = False
guessUsed = True
guess = ""
guesses = 10
won = False
while guesses != 0 and won == False:
	print(answer)
	guess = input("guess a letter : ")
	for x in range(len(word)):
		if guess == word[x]:
			correct = True
			guessUsed = False
			guessed[x] = True
		else:
			correct = False
	for x in range(len(word)):
		if guessed[x] == True:
			answer[x] = word[x]
	if guessUsed == True:
		guesses -= 1
	else:
		guessUsed = True
	for x in range(len(word)):
		if guessed[x] != True:
			won = False
			break
		else:
			won = True
if won == True:
	print("the word was " + word + ", you won!")
else:
	print("the word was " + word + ", you lost :(")