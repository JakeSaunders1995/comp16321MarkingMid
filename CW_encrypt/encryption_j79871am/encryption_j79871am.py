import filecmp
import os

f = 0

filepa = input("please input and output file path: ")
filepath = filepa.split()
filepath1 = filepath[0]
outputinp = filepath[1]

realdirect = os.listdir(filepath1)
coolerreal = (filepath1 + ("\\"))
coolerreal.strip()
coolerreal1 = coolerreal + realdirect[0]
reallen = len(realdirect)


while reallen != f:

    sickbeans = coolerreal + realdirect[f]
    newlist15 = []
    rfile = open(sickbeans, "r")
    for line in rfile:
        for character in line:
            newlist15.append(character)
    s = len(newlist15)
    crate = []
    cool = []
    o = 0

    while newlist15[o] != (":"):
        crate.append(newlist15[o])
        o = o + 1
    o = o + 1
    while s != o:
        cool.append(newlist15[o])
        o = o + 1

    states1 = ("  ").join(crate)
    coolest1 = states1.replace("  ", "")
    states2 = ("  ").join(cool)
    coolest2 = states2.replace("  ","")


    if coolest1 == ("Caesar Cipher(+3)"):

        alphabet = [["x", -3], ["y", -2], ["z", -1], ["a", 0], ["b", 1], ["c", 2], ["d", 3], ["e", 4], ["f", 5],
                    ["g", 6],
                    ["h", 7], ["i", 8], ["j", 9], ["k", 10], ["l", 11], ["m", 12], ["n", 13], ["o", 14], ["p", 15],
                    ["q", 16],
                    ["r", 17], ["s", 18], ["t", 19], ["u", 20], ["v", 21], ["w", 22]]
        newlist = cool
        newlist1 = []
        # for line in cool:
        # for character in line:
        # newlist.append(character)
        facts = len(cool)
        x = int(0)
        tool = ("bean")
        for x in range(x, facts):
            y = -3
            cray = newlist[x]

            for y in range(-3, 23):
                tool = alphabet[y][0]
                if cray == (" "):
                    newlist1.append(" ")
                    break
                elif tool == cray:
                    baked = alphabet[y][1]
                    if baked < 0:
                        baked = baked + 26
                    score = alphabet[baked][0]
                    newlist1.append(score)
                    break
                elif cray == (".") or cray == ("?") or cray == ("!") or cray == (",") or cray == (":") or cray == (
                        ";") or cray == ("-") or cray == ("–") or cray == ("—") or cray == ("(") or cray == (
                ")") or cray == (
                        "{") or cray == ("}") or cray == ("...") or cray == ("'") or cray == ('"') or cray == (
                "[") or cray == (
                        "]"):
                    newlist1.append(cray)
                    break
                else:

                    y = y + 1
            x = x + 1

        state = ("  ").join(newlist1)

        coolest = state.replace("  ", "")

        calc = f + 1
        otfilenam = (("test_file") + (str(calc)) + ("_j79871am.txt"))
        outp = os.path.join(outputinp, otfilenam)
        opres = open(outp, "w")
        opres.write(coolest)
        opres.close()


    elif coolest1 == ("Hex"):

        newlist = cool
        newlist1 = []

        facts = len(cool)
        x = int(0)
        tool = ("bean")
        for x in range(x, facts):
            y = -3
            cray = newlist[x]
        compound = ("  ").join(cool)

        coolest12 = compound.replace("  ", "")
        coolest122 = coolest12.replace(" ", "")

        r = len(coolest122)
        q = 2
        output = [coolest122[i:i + q] for i in range(0, r, q)]

        sicks = len(output)
        xss = 0
        nextlevel = []
        byte = bytes.fromhex(coolest122).decode("utf-8")

        calc = f + 1
        otfilenam = (("test_file") + (str(calc)) + ("_j79871am.txt"))
        outp = os.path.join(outputinp, otfilenam)
        opres = open(outp, "w")
        opres.write(byte)
        opres.close()


    elif coolest1 == ("Morse Code"):
        moese = [["A", ".-"], ["B", "-..."], ["C", "-.-."], ["D", "-.."], ["E", "."], ["F", "..-."], ["G", "--."],
                 ["H", "...."], ["I", ".."], ["J", ".---"], ["K", "-.-"], ["L", ".-.."], ["M", "--"], ["N", "-."],
                 ["O", "---"], ["P", ".--."], ["Q", "--.-"], ["R", ".-."], ["S", "..."], ["T", "-"], ["U", "..-"],
                 ["V", "...-"], ["W", ".--"], ["X", "-..-"], ["Y", "-.--"], ["Z", "--.."], ["1", ".----"],
                 ["2", "..---"], ["3", "...--"], ["4", "....-"], ["5", "....."], ["6", "-...."], ["7", "--..."],
                 ["8", "---.."], ["9", "----."], ["0", "-----"], [",", "--..--"], [".", ".-.-.-"], ["?", "..--.."],
                 ["/", "-..-."], ["-", "-....-"], ["(", "-.--."], [")", "-.--.-"],[" ","/"]]
        newlist = cool
        cool.append(" ")
        lest = len(moese)
        tine = len(cool)
        teen = []
        further = []
        k = 0
        p = 0
        while k != tine:
            teen.append(cool[k])
            if cool[k] == (" "):
                state2 = ("  ").join(teen)
                coolest14 = state2.replace("  ", "")
                coolest144 = coolest14.replace(" ", "")

                while p != lest:
                    ns = moese[p][1]
                    if coolest144 == ns:
                        further.append(moese[p][0])


                        teen = []
                    p = p + 1


            p = 0
            k = k + 1


        state = ("  ").join(further)

        coolest = state.replace("  ", "")
        calc = f + 1
        otfilenam = (("test_file") + (str(calc)) + ("_j79871am.txt"))
        outp = os.path.join(outputinp, otfilenam)
        opres = open(outp, "w")
        opres.write(coolest.lower())
        opres.close()


    f = f + 1
