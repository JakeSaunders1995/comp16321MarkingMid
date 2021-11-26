# Python midterm - Program 1
# Rugby scores
# by Matt Schofield - G75342ms

# Import sys and os libs
import sys, os

# Create the output directory if it does not already exist
if not os.path.exists(str(sys.argv[2])):
    os.makedirs(str(sys.argv[2]))

# Get array of all file names in input directory given command line parameter
encryptedFileArray = os.listdir(str(sys.argv[1]))

# Define morse code dictionary
MORSE_CODE = {  '.-':'A', '-...':'B',
                '-.-.':'C', '-..':'D', '.':'E',
                '..-.':'F', '--.':'G', '....':'H',
                '..':'I', '.---':'J', '-.-':'K',
                '.-..':'L', '--':'M', '-.':'N',
                '---':'O', '.--.':'P', '--.-':'Q',
                '.-.':'R', '...':'S', '-':'T',
                '..-':'U', '...-':'V', '.--':'W',
                '-..-':'X', '-.--':'Y', '--..':'Z',
                '.----':'1', '..---':'2', '...--':'3',
                '....-':'4', '.....':'5', '-....':'6',
                '--...':'7', '---..':'8', '----.':'9',
                '-----':'0', '--..--':', ', '.-.-.-':'.',
                '..--..':'?', '-..-.':'/', '-....-':'-',
                '-.--.':'(', '-.--.-':')', '.-..-.':":",
                '.----.':'\'', '-.-.--':'!', '---...':':'}

# For each file in array, process the score file
for file in encryptedFileArray:
    # Reset message
    decryptedMessage = ""

    # Open file
    encryptedFile = open(str(sys.argv[1]) + file)

    # Read encrypted string from file
    encryptedString = encryptedFile.read()

    # Close the file
    encryptedFile.close()

    # Display current string being parsed
    print("Encrypted string:", encryptedString)

    # Determine encryption method
    if encryptedString[0].lower() == "h":
        # Hex encrypted - remove encryption identifier
        encryptedString = encryptedString[4:]
        # Decrypt hex by iterating over each 2 digit hex value and converting it to a letter
        for char in range(0, len(encryptedString), 3):
            decryptedMessage += chr(int(encryptedString[char] + encryptedString[char + 1], 16))

    elif encryptedString[0].lower() == "c":
        # Ceaser-cipher encrypted - remove encryption identifier
        encryptedString = encryptedString[18:]
        # Decrypt ceaser-cipher by converting the (unicode - 3) to a letter
        for char in encryptedString:
            decryptedMessage += chr(ord(char) - 3) if char != " " else " "

    else:
        # Morse encrypted - remove encryption identifier
        # Space added to flag the end of the string
        encryptedString = encryptedString[11:] + " "
        # Decrypt morse using lookup table
        # Keep adding characters to morseValue until the end of a
        # character, a " " is reached then process the value
        morseValue = ""
        for codeIndex in range(len(encryptedString)):
            code = encryptedString[codeIndex]
            # "/" signifies the end of a word
            # We check if the last character was a "/" so we can skip the space
            # that follows immediatly afterwards
            if encryptedString[codeIndex-1] == "/":
                continue
            elif code == "/":
                decryptedMessage += " "
            elif code == " ":
                decryptedMessage += MORSE_CODE[morseValue]
                morseValue = ""
            else:
                morseValue += code

    print(decryptedMessage)

    # Generate new file name
    outputFilePath = str(sys.argv[2])

    # Effectively ensures output command line argument is a folder
    if outputFilePath[len(outputFilePath)-1] != "/":
        outputFilePath += "/"

    # [:-4] is used to drop the '.txt' from the file before adding the uni ID
    outputFilePath += file[:-4] + "_g75342ms" + ".txt"

    resultsFile = open(outputFilePath, "w")
    resultsFile.write(decryptedMessage)

    # Close file
    resultsFile.close()
