import sys
import re

EnglishAlphaFile = sys.argv[1]
InputFile = sys.argv[2]
OutputFile = sys.argv[3]

punctuations_dict = ["'",",",".",":","-","!","(",")","[","]","#"]
numbers_dict = [0,1,2,3,4,5,6,7,8,9]

with open(InputFile, 'r') as i:
  input_data = i.read()

correctString = " "
UpperCase = 0
punctuations = 0
numbers = 0                #numbers detected counter


#formatting

for i in range (0,len(input_data)):
  if input_data[i].isnumeric():
      numbers += 1
  elif (input_data[i].isalpha() and input_data[i].upper() == input_data[i] and input_data[i] != " "):
      UpperCase += 1
      correctString += input_data[i]
  elif input_data[i] in punctuations_dict:
      punctuations += 1
  else:
      correctString += input_data[1]

#correction

input_data.list()
AllWordsinput = input_data.split(" ")

for x in AllWordsinput:
    if x == " "
        AllWordsinput.remove(x)

totalWords = len(input_data)

with open(EnglishAlphaFile, 'r') as e:
    AllEnglishWords = e.readlines()

AllEnglishArray = []
correctWords = 0
incorrectWords = 0

for word in AllEnglishinput:
    AllEnglishArray.append(word.strip("\n"))
for word in input_data:
    if word in AllEnglishWords:
        correctWords += 1
    else:
        incorrectWords += 1

#outputs

output_string += "u43534sr" + "\n"
output_string += "Formatting ##################\n"
output_string += "Number of upper case letters changed: " + str(UpperCase) + "\n"
output_string += "Number of punctuations removed: " + str(punctuations) + "\n"
output_string += "Number of numbers removed: " + str(numbers) + "\n"
output_string += "Spellchecking ##################\n"
output_string += "Number of words: " + str(totalWords) + "\n"
output_string += "Number of correct words: " + str(correctWords) + "\n"
output_string += "Number of incorrect words: " + str(incorrectWords)

with open(OutputFile, "w") as f:
    f.write(output_string)
