essay = list()
with open("test_file1.txt") as file:
	essay = file.readline()

theWords = []
word = open("EnglishWords.txt", "r")
for line in word:
	line = line.rstrip()
	theWords.append(line)



upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lower = [x.lower() for x in upper]
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']




a = ''.join(i for i in essay if not i.isdigit())     #remove digit from the essay
b = "".join(c for c in a if c not in punctuation)    #remove punctuation from the essay
c = b.lower()									     #change to lower case
word_list = c.split()								 #set all the words into set

print(c)


i, u, a, n, start = 0, 0, 0, 0, 0




while(i < len(essay)):
	alphabet = essay[i]
	i += 1
	if alphabet in upper:
		u += 1

	elif alphabet in punctuation:
		a += 1

	elif alphabet in digit:
		n += 1

numberOfWords = len(word_list)
print("Number of words in file:", numberOfWords)
b, c = 0, 0

while (start < len(word_list)):
	word = word_list[start]
	start += 1
	if word in theWords:
		b += 1

	if word not in theWords:
		c += 1


f = open("result.txt", "w")
f.write("Number of upper case words transformed:", str(u))
f.write("Number of punctuation's removed:", str(a))
f.write("Number of numbers removed:", str(n))
f.wrie("Number of correct words in file:", b)
f.write("Number of incorrect words in file:", c)
f.close