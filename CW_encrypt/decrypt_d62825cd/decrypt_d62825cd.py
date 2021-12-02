import sys
print(sys.argv)
test = open(sys.argv[1] , "r")
oku = test.readline()
oku = oku.split(":")
print(oku)
typeStr =oku[0]
oku = oku[1].split()



Mdic = { 
	
	"20" :" " ,
	"41" :"A" ,
	"42" :"B" ,
	"43" :"C",
	"44" :"D" ,
	"45" :"E" ,
	"46" :"F" ,
	"47" :"G" ,
	"48" :"H" ,
	"49" :"I" ,
	"4a" :"J" ,
	"4b" :"K" ,
	"4c" :"L" ,
	"4d" :"M" ,
	"4e" :"N" ,
	"4f" :"O" ,
	"50" :"P" ,
	"51" :"Q" ,
	"52" :"R" ,
	"53" :"S",
	"54" :"T" ,
	"55" :"U" ,
	"56" :"V" ,
	"57" :"W" ,
	"58" :"X" ,
	"59" :"Y" ,
	"5a" :"Z",
	"61" :"a" ,
	"62" :"b" ,
	"63" :"c",
	"64" :"d" ,
	"65" :"e" ,
	"66" :"f" ,
	"67" :"g" ,
	"68" :"h" ,
	"69" :"i" ,
	"6a" :"j" ,
	"6b" :"k" ,
	"6c" :"l" ,
	"6d" :"m" ,
	"6e" :"n" ,
	"6f" :"o",
	"70" :"p" ,
	"71" :"q" ,
	"72" :"r" ,
	"73" :"s",
	"74" :"t" ,
	"75" :"u" ,
	"76" :"v" ,
	"77" :"w" ,
	"78" :"x" ,
	"79" :"y" ,
	"7a" :"z" 


}



M3dic = {

	"/":" ",
	".-" :"a" ,
	"-...":"b" ,
	"-.-.":"c" ,
	"-..":"d" ,
	".":"e" ,
	"..-.":"f" ,
	"--.":"g" ,
	"...."	:"h" ,
	"..":"i" ,
	".---":"j" ,
	"-.-":"k" ,
	".-..":"l" ,
	"--" :"m" ,	
	"-.":"n" ,	
	"---":"o" ,
	".--.":"p" ,
	"--.-":"q" ,
	".-.":"r" ,
	"...":"s" ,
	"-"	:"t" ,
	"..-":"u" ,
	"...-":"v" ,	
	".--":"w" ,
	"-..-":"x" ,
	"-.--":"y" ,
	"--..":"z" 

}



f = open(sys.argv[2],"a")

alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"

if typeStr=="Hex":
	for a in oku:
		f.write(Mdic[a])
elif typeStr=="Caesar Cipher(+3)":
	for text in oku:
		cipherTextPosition = 0
		while cipherTextPosition < len(text):
		    cipherTextChar = text[cipherTextPosition]
		    alphabetPosition = 3
		    while cipherTextChar != alphabet[alphabetPosition]:
		        alphabetPosition = alphabetPosition + 1
		    alphabetPosition = alphabetPosition - 3
		    f.write(alphabet[alphabetPosition])
		    cipherTextPosition = cipherTextPosition + 1
		f.write(" ")
elif typeStr=="Morse Code":
	for a in oku:
		f.write(M3dic[a])
f.close()


