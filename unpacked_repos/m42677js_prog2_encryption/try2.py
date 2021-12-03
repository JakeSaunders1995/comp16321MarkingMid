morseText = ".... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"
character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', ' ']
code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.', '/']
morse_dict = {}
zipped_code_char = zip(code,character)
rev_morse_dict = dict(list(zipped_code_char))
print(rev_morse_dict)
while True:
	ori_msg = []
	dec_msg = []
	input_msg = morseText
	ori_msg.append(input_msg)
	new_msg = input_msg.split( )

	for j in range (0,len(new_msg)):
		if new_msg[j] in rev_morse_dict.keys():
			dec_msg.append(rev_morse_dict[new_msg[j]])

	print (''.join(dec_msg))

	break


# encryptedFile = "Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"
# morseText = ""
# pattern = re.compile(r'[^:a-zA-Z]')
# matches = pattern.finditer(encryptedFile)	
# for match in matches:
# 	morseValue = match.group()
# 	morseText = morseText + morseValue
# print(morseText)
# morseText = ".... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"

# character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
# code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
# # Define an empty dictionary 'morse_dict'
# morse_dict = {}
# # Convert the 2 lists into a dictionary using a tuple
# zipped_char_code = zip(character, code)
# morse_dict = dict(zipped_char_code)
# # Print the dictionary 'morse_dict' on the terminal line by line
# # for key, value in morse_dict.items():
# #     print(key, value)

# # reverse the previous dict as it's easier to access the keys
# zipped_code_char = zip(code,character)
# rev_morse_dict = dict(list(zipped_code_char))
# # print(rev_morse_dict)
# # initiating a while loop
# while True:
#     # empty list to store original message
#     ori_msg = [] 
#     # empty list to store decoded message
#     dec_msg = []
    
#     # prompt the user to input morse code
#     input_msg = morseText
#     # append input_msg (string) to ori_msg (string)
#     ori_msg.append(input_msg)
#     # split each morse code by '*'
#     new_msg = input_msg.split("/")
#     print(new_msg)
    
#     # printing out the original message
#     for line in ori_msg: # to print original message without the []
#         print("Original message: " + line + "\n")
    
#     # loop through each morse code representation
#     for j in range (0,len(new_msg)):
#         # get the alphanumeric alphabet based on the dict keys and append to dec_msg
#         if new_msg[j] in rev_morse_dict.keys():
#             dec_msg.append(rev_morse_dict[new_msg[j]])
    
#     # printing out the decoded message
#     print ("Decoded Message is: " + ''.join(dec_msg) + "\n")
#     # end the infinite while loop
#     break