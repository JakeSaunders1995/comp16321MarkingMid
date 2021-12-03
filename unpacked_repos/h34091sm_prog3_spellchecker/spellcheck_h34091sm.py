import re
import sys
import difflib

EnglishLang = sys.argv[1]
InFold = sys.argv[2] + "/test_file2.txt"
OutFold = sys.argv[3] + "/spell_check_result.txt"


readFile = open[InFold, "r"]
incorrect = readFile.read()


def convert(incorrect):
    return(incorrect[0].split())


def convert(EnglishDict):
    return(EnglishDict[0].split)    


englishtxt = open[EnglishLang, "r"]
EnglishDict = EnglishLang.read()
 

wrong = [incorrect]


def convert(wrong):
    return(wrong[0].split())





countw = 0 
countr = 0 

def spell_checker(wrong):
    for word in wrong.casefold().split():
        for word  in EnglishDict:
            countr += 1
            


writeFile = open(OutFold, "w")
writeFile.write(countr + countw)
writeFile.close


