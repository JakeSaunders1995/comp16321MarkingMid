# Python midterm - Program 3
# Spellchecker
# by Matt Schofield - G75342ms

# Import sys and os libs
import sys, os

# Create the output directory if it does not already exist
if not os.path.exists(str(sys.argv[3])):
    os.makedirs(str(sys.argv[3]))

# Get array of all file names in input directory given command line parameter
spellingFileArray = os.listdir(str(sys.argv[2]))

# For each file in array, process the score file
for file in spellingFileArray:
    # Reset report variables
    upperToLower = 0
    symbsRemoved = 0
    numsRemoved = 0
    wordCount = 0
    correctWords = 0
    incorrectWords = 0

    # Open file
    spellingFile = open(str(sys.argv[2]) + file)

    # Read encrypted string from file
    sillyString = spellingFile.read()

    # Close the file
    spellingFile.close()

    # Remove and flag numbers and symbols from the string
    charIndex = 0#
    while charIndex < len(sillyString):
    # Change uppercase letters to lowercase
        char = sillyString[charIndex]
        # print(len(sillyString))
        # print(charIndex, end="")
        # print(char)
        if char in "1 2 3 4 5 6 7 8 9 0".split(" "):
            sillyString = sillyString.replace(char, "", 1)
            numsRemoved += 1
        elif char in "! \" # $ % & ' ( ) * + ,  - . / : ; < = > ? @ [ ] \n\ ^ _ ` { } | ~".split(" "):
            sillyString = sillyString.replace(char, "", 1)
            symbsRemoved += 1
        elif char in "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" "):
            sillyString = sillyString.replace(char, char.lower(), 1)
            upperToLower += 1
            charIndex += 1
        else:
            # Else character is lowercase or a space
            charIndex += 1
            continue

    # Get word count
    wordCount = len(sillyString.split(" "))

    # Open englishWords.txt
    engWordsFile = open(str(sys.argv[1]))
    engWords = engWordsFile.read()

    # Run each word in  string against
    for word in sillyString.split(" "):
        if word not in engWords:
            incorrectWords += 1
        else:
            correctWords += 1

    # Generate new file name
    outputFilePath = str(sys.argv[3])

    # Effectively ensures output command line argument is a folder
    if outputFilePath[len(outputFilePath)-1] != "/":
        outputFilePath += "/"

    # [:-4] is used to drop the '.txt' from the file before adding the uni ID
    outputFilePath += file[:-4] + "_g75342ms" + ".txt"

    # Open results file
    resultsFile = open(outputFilePath, "w")

    # Cast report variables to string types
    upperToLower, symbsRemoved, numsRemoved, wordCount, correctWords, incorrectWords = str(upperToLower), str(symbsRemoved), str(numsRemoved), str(wordCount), str(correctWords), str(incorrectWords)
    # Write report to file
    resultsFile.writelines(["Username: G75342ms" + "\n",
                            "Formatting ###################" + "\n",
                            "Number of upper case words transformed: " + upperToLower + "\n",
                            "Number of punctuation’s removed: " + symbsRemoved + "\n",
                            "Number of numbers removed: " + numsRemoved + "\n",
                            "Spellchecking ###################" + "\n",
                            "Number of words in file: " + wordCount + "\n",
                            "Number of correct words in file: " + correctWords + "\n",
                            "Number of incorrect words in file: " + incorrectWords])

    # Close file
    resultsFile.close()
