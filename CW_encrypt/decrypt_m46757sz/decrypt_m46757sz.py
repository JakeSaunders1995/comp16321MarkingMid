import sys,os

MorseList = {
".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g",
"....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n",
"---":"o",".--．":"p","--.-":"q",".-.":"r","...":"s","-":"t",
"..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z",
"-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",
".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",
".-.-.-":".","---...":":","--..--":",","-.-.-.":";","..--..":"?",
"-...-":"=",".----.":"'","-..-.":"/","-.-.--":"!","-....-":"-",
"..--.-":"_",".-..-.":'"',"-.--.":"(","-.--.-":")","...-..-":"$",
".--.-.":"@",".-.-.":"+",
}

def mk_paths(inpath,outpath):
    global in_paths, out_paths
    in_paths = []
    out_paths = []
    for i in os.listdir(inpath):
        if i[-4:] == ".txt":
            in_paths.append(inpath + "/" +i)
            out_paths.append(outpath + "/" + i[:-4] + "_m46757sz" + i[-4:])
    return

def read_file(path):
    global type
    with open(path,'r') as f:
        ft = f.read()
        if ft[3] == ":":
            type = "hex"
            return ft[4:]
        if ft[17] == ":":
            type = "+3"
            return ft[18:]
        if ft[10] == ":":
            type = "morse"
            return ft[11:]

def decrypt(cipher):
    r = ""
    if type == "hex":
        for i in cipher.split(" "):
            r += chr(int(i,16))
        r = r.lower()
    elif type == "+3":
        cipher = cipher.lower()
        for i in cipher:
            i = ord(i)
            if 100 <= i <= 122:
                i -= 3
            elif 97 <= i < 100:
                i += 23
            r += chr(i)
    elif type == "morse":
        for i in cipher.split(r" / "):
            for z in i.split(" "):
                r += MorseList[z]
            r += " "
        r = r[:-1]
    return r

def output(path,text):
    with open(path,'w') as f:
        f.write(text)
          

def main(paths):
    mk_paths(paths[1],paths[2])
    for p in range(len(in_paths)):
        cipher_txt = read_file(in_paths[p])
        decrypted_txt = decrypt(cipher_txt)
        output(out_paths[p],decrypted_txt)

if __name__ == "__main__":
    main(sys.argv)
