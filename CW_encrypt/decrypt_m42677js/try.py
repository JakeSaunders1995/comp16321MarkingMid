

    



# plaintext = input("Plaintext: ")
# cipherText = ""
# plaintextPosition = 0
# while plaintextPosition < len(plaintext):
#     plaintextChar = plaintext[plaintextPosition]
#     ASCIIValue = ord(plaintextChar)
#     ASCIIValue = ASCIIValue - 3
#     cipherText = cipherText + chr(ASCIIValue)
#     plaintextPosition += 1
# print (cipherText)

# def split(word):
#     return [char for char in word]

plainText = "exw fdhvdu lv d olwwoh pruh gliilfxow"
cipherText = ""
plaintextPosition = 0
# while plaintextPosition < len(plainText):
#     plainChar = plainText[plaintextPosition]
#     ASCIIValue = ord(split(plainText))
#     ASCIIValue = ASCIIValue - 3
#     cipherText = cipherText + chr(ASCIIValue)
#     plainPosition += 1
# print(cipherText)
# print(type(plaintext))



hexText = "exw"
lower="xyzabcdefghijklmnopqrstuvwxyzabc"
decryptedText = ""
space = " "
textPosition = 0
# while textPosition < len(hexText):
#     hexChar = hexText[textPosition]    
#     i = 3
#     for hexChar in range(0, len(hexText)):
#         if hexText != lower[i]:
#             i += 1
#             if lower[i] == hexChar:
#                 break
#             elif hexChar == space:
#                 continue
#         else:
#             break
#     i -= 3
#     decryptedText = decryptedText + lower[i]
#     textPosition += 1


	# while hexChar != lower[lowerPosition]:
	# 	lowerPosition += 1
	# 	if lower[lowerPosition] == hexChar:
	# 		break
 #    	else:
 #    		continue
	# lowerPosition -= 3
	# decryptedText = decryptedText + lower[lowerPosition]
	# textPosition += 1


print(decryptedText)