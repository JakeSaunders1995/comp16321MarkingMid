import argparse
import re
import argparse
import os

def decrypt_hex(cyphertext: str):
  hex_chars = cyphertext.split(" ")
  plaintext = ""
  for hex in hex_chars:
    decimal = int(hex, 16)
    letter = chr(decimal).lower()
    plaintext += letter
  return plaintext

def decrypt_caesar(cyphertext: str, shift: int):
  plaintext = ""
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  for char in cyphertext:
    char = char.lower()
    if char in alphabet:
      index = alphabet.index(char)
      index -= shift
      if index < 0:
        index += len(alphabet)
      elif index > len(alphabet):
        index -= len(alphabet)
      plaintext += alphabet[index]
    else:
      plaintext += char
  return plaintext

def decrypt_morse(cyphertext: str):
  morse_map = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h": "....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    ',':'--..--',
    '.':'.-.-.-',
    '?':'..--..',
    "!": "-.-.--",
    "'": ".----.",
    "&":".-...",
    ":":"---...",
    ";":"-.-.-.",
    "_":"..--.-",
    "=": "-...-",
    "+":".-.-.",
    "$": "...-..-",
    "@": ".--.-.",
    '/':'-..-.',
    '-':'-....-',
    '(':'-.--.',
    ')':'-.--.-'
    
  }
  morse_map = {v: k for k, v in morse_map.items()}
  morse_chars = cyphertext.split(" ")
  plaintext = ""
  for morse_char in morse_chars:
    if morse_char != "/":
      decoded = morse_map.get(morse_char)
      plaintext += decoded
    else:
      plaintext += " "
  return plaintext
  
def get_input_and_output_folder_paths():
  parser = argparse.ArgumentParser()
  parser.add_argument("input_folder_path")
  parser.add_argument("output_folder_path")
  args = parser.parse_args()
  input_folder_path = args.input_folder_path
  output_folder_path = args.output_folder_path
  return [input_folder_path, output_folder_path]

def main():
  temp = get_input_and_output_folder_paths()
  input_path = temp[0]
  output_path = temp[1]
  for filename in os.listdir(input_path):
    path = input_path + "/" + filename
    file = open(path, "r")
    line = file.read()
    line = line.replace("\n", "")
    file.close()
    re_match = re.fullmatch("(?P<algorithm>.*):(?P<cyphertext>.*)", line)
    algorithm = re_match.group("algorithm")
    cyphertext = re_match.group("cyphertext")
    plaintext = ""
    if algorithm == "Hex":
      plaintext = decrypt_hex(cyphertext)
    elif algorithm == "Caesar Cipher(+3)":
      plaintext = decrypt_caesar(cyphertext, 3)
    else:
      plaintext = decrypt_morse(cyphertext)
    name = "n25359ec"
    temp = filename.split(".")
    output_file_name = temp[0] + f"_{name}" + f".{temp[1]}"
    path = output_path + "/" + output_file_name
    if not os.path.isdir(output_path):
      cur = os.getcwd()
      os.mkdir(cur + "/" + output_path)
    file = open(path, "w")
    file.write(plaintext)
    file.close()
  


  

if __name__ == "__main__":
  main()