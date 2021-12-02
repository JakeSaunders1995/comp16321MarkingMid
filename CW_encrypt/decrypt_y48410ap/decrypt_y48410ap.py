import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
parser = parser.parse_args()

input_folder = parser.input + '/'
output_folder = parser.output + '/'

def init_morse():
    alph = "etianmsurwdkgohvfüläpjbxcyzqöx54ŝ3é đ2 è+ σàĵ16=/ ç ĥ 7 ĝn8 90            ?_    “  .    @   `  -        ;! (     ,    :"
    morse_tree = Node('.')
    for c in alph:
        morse_tree = morse_tree.insert(c)
    return morse_tree      
                
class Node:
    def __init__(self, data):
        self.dot = None
        self.dash = None
        self.data = data
        
    def insert(self, data):
        if self == None:
            self = Node(data)
            return self
        q = []
        q.append(self)
        while len(q):
            curr = q.pop(0)
            
            if curr.dot != None:
                q.append(curr.dot)
            else:
                curr.dot = Node(data)
                return self
            if curr.dash != None:
                q.append(curr.dash)
            else:
                curr.dash = Node(data)
                return self

    def inorder(self):
        if not self:
            return
        if self.dot:
            self.dot.inorder()
        print(self.data)
        if self.dash:
            self.dash.inorder()

for input_file in os.scandir(input_folder):
    input_file = input_file.path
    
    output_file = open(output_folder + os.path.basename(input_file)[:-4] + "_y48410ap.txt", 'w')
    input_file = open(input_file, 'r')

    text = input_file.read()
    text = text.split(':')
    algorithm = text[0]
    text = text[1]

    if algorithm == 'Hex':
        byte_text = bytes.fromhex(text)
        ascii_string = byte_text.decode("ASCII")
        ascii_string = ascii_string.lower()
        output_file.write(ascii_string)
    elif algorithm == 'Caesar Cipher(+3)':
        result = ''
        alph = "xyzabcdefghijklmnopqrstuvwxyzabc"
        for c in text:
            i = alph[3:].find(c)
            if i != -1:
                result+=alph[i]
            else:
                result+=c
        output_file.write(result)
    elif algorithm == "Morse Code":
        result = ''
        words = text.split('/')
        morse_tree = init_morse()
        for word in words:
            letters = word.split(' ')
            for letter in letters:
                node = morse_tree
                for d in letter:
                    if d == '.':
                        node = node.dot
                    else: 
                        node = node.dash
                letter = node.data
                result += letter if letter != '.' else ''
            result+=' '
        result = result[:-1]
        output_file.write(result)
        
    output_file.close()
    input_file.close()
        