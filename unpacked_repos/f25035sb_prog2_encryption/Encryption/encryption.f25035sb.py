a = input("enter the type of encryption is to be performed :") #CAESAR MORSE HEXADECIMAL
message = input("enter text")
text = ""
def Caesar():
  for i in text :
    if i.islower():
      index = ord(i) - ord("a")
      n_index = (index + Shift) % 26
      n_unicode = n_index + ord("a")
      char = chr(n_unicode)
      message = message + char
      

def Hexadecimal():
  text = bytes.fromhex(message)
  text = text.decode("ascii")
  

Code = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
          'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}
def Morse(morse):
    for i in morse.split(' '):
        yield code.get(i)

if (a == "Caesar"):
  Caesar(message)
  print(text,message)

if (a == "Hexadecimal"):
  Hexadecimal(message)
  print(text,message)


if (a == "Morse"):
  Morse(message)
  print(text,message)






  