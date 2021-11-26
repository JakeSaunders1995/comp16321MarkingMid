import os, argparse, re
#help(os)
#help(argparse)
#help(re)
parser = argparse.ArgumentParser()
parser.add_argument('x', type = str)
parser.add_argument('y', type = str)
parser.add_argument('z', type = str)
args = parser.parse_args()

def spell_bee(dictionary_111, file_111, file_222):
	file_output_ = file_111[0:(len(file_111) - 4)] + "_y48052as" + ".txt"
	file_output_ = file_222 + file_output_
	file_111 = args.y + file_111
	file1 = open(file_111)
	file2 = open(file_output_, "w")
	file2.write('y48052as\n')
	file2.write('Formatting ###################\n')
	s1 = file1.read()
	def remover(s):
		c1, c2 = 0, 0
		counter = 0
		x,s2 = "",""
		for x in s:
			if(str(x).isnumeric()):
				s2 += ""
				c1 += 1
			elif(str(x) == " "):
				s2 += " "
			elif(str(x) == "." or str(x) == "," or str(x) == ";" or str(x) == '"' or str(x) == "'" or str(x) == ":" or str(x) == "?" or str(x)=="-" or str(x)=="[" or str(x)=="]" or str(x)=="{" or str(x)=="}" or str(x)=="(" or str(x)==")" or str(x)=="..." or str(x)=="@" or str(x)=="!"):
				s2 += ""
				c2 += 1
			else:
				if(str(x).isupper()):
					counter = counter + 1
				s2 += str(x).lower()
		statement1 = 'Number of upper case words changed:' + str(counter) + '\n'
		file2.write(statement1)
		statement1 = 'Number of punctuations removed:' + str(c2) + '\n'
		file2.write(statement1)
		statement1 = 'Number of numbers removed: ' + str(c1) + '\n'
		file2.write(statement1)

		return s2

	s1 = remover(s1)

	dictionary = open(dictionary_111)


	file2.write('Spellchecking ###################\n')
	def compare_characterbycharacter(s1, s2):
		c = 0

		for i in range(0, len(s1)-1):
			if(str(s1[i]) == str(s2[i])):
				c += 1
		return c


	def word_generator(s_w):
		'''print("chal ja")'''
		s_new, s5 = "", ""
		s_end = ""
		c = 0
		c_initial = 0
		len_sw = len(s_w)
		'''print(len_sw)'''
		while True:
			s4 = dictionary.readline()
			if len(s4) == 0:
				break
			else:
				if(len(s4) == len_sw + 1):
					c = int(compare_characterbycharacter(s4, s_w))
					if(c>=c_initial):
						c_initial = c
						s_end = s4
						continue
				elif (len(s4) == len_sw):
					for i in range(0, len(s4)):
						s_new = s4[0:int(i)] + " " + s4[int(i):int(len_sw - 1)]
						c = int(compare_characterbycharacter(s_w, s_new))
						if(c>c_initial):
							c_initial = c
							s_end = s4
							continue
				elif (len(s4) == len_sw+2):
					for i in range(0, len_sw+1):
						s5 = s_w[0:int(i)] + " " + s_w[int(i):int(len_sw)]					
						c = int(compare_characterbycharacter(s4, s5))
						if(c>c_initial):
							c_initial = c
							s_end = s4
							continue
				else:
					continue

		dictionary.seek(0)
		return s_end

	def main(s_input_1):
		c3, c4 = 0, 0
		answer = ""
		splits = s_input_1.split()
		for split in splits:
			actual = split
			split = str(word_generator(actual))
			c4 += 1
			if(str(split).strip() == str(actual).strip()):
				c3 += 1
			answer = answer + (str(split).rstrip('\n') + " ")
			continue
		statement2 = 'Number of words: ' + str(c4) + '\n'
		file2.write(statement2)
		statement2 = 'Number of correct words: ' + str(c3) + '\n'
		file2.write(statement2)
		statement2 = 'Number of incorrect words: ' + str(c4 - c3) + '\n'
		file2.write(statement2)
		return answer


	'''print(word_generator("triger"))'''



	'''print('y48052as\n')
	print('Formatting ###################\n')
	print('Number of upper case words changed:', c3, '\n')
	print('Number of punctuations removed:', c2, '\n')
	print('Number of numbers removed: ', c1, '\n')
	print('Spellchecking ###################\n')
	print('Number of words: ', c4, '\n')
	print('Number of correct words: ', c3, '\n')
	print('Number of incorrect words: ', (c4 - c3), '\n')'''


	main(s1)
	dictionary.close()
	file1.close()
	file2.close()

'''print(os.path.dirname(args.y))'''
for file in os.listdir(args.y):
	'''print(file)'''
	spell_bee(args.x, file, args.z)	