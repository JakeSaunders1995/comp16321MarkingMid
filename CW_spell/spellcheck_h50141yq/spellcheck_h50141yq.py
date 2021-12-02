import sys, os
Englishlist = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]
numtable = "1234567890"
cap_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz "
for input_file in os.listdir(input_path):
    os.chdir(input_path)
    total = 0
    capital = 0
    num = 0
    wrong = 0
    right = 0
    pun = 0
    with open(input_file, encoding='utf-8') as f:
        text = f.read()
        for i in text:
            if i not in alphabet:
                if i not in cap_alp:
                    text = text.replace(i, '')
                    total += 1
                else:
                    capital += 1
            if i in numtable:
                num+=1
        pun = total - num
        text = text.lower()
        text = text.split(" ")
        while text.count(''):
            text.remove('')
        words = len(text)
        with open(Englishlist, encoding='utf-8') as e:
            lines = e.read()
            lines = lines.split("\n")
            for a in text:
                for i in lines:
                    if i == a:
                        right+=1
        wrong = words - right
        name = str(f.name)
        file_list = name.split('.')
        os.chdir(output_path)
        output_file = file_list[0] + "_h50141yq." + file_list[1]
        new = open(output_file, 'w')
        new.write("Formatting ###################\n"
        'Number of upper case letters changed: '+str(capital)+'\n'
        'Number of punctuations removed: '+str(pun)+'\n'
        "Number of numbers removed: "+str(num)+'\n'
        "Spellchecking ###################\n"
        "Number of words: "+str(words)+'\n'
        "Number of correct words: "+str(right)+'\n'
        "Number of incorrect words: "+str(wrong)+'\n')
        new.close()
