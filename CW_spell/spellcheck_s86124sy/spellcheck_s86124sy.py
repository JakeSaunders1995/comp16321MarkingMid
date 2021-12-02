import os
import sys

with open(r"C:\Users\dell\Downloads\midterm_files(1) (1)\midterm_files\Example_inputs\Example_inputs_program3\test_file2.txt","r",encoding="utf8")as f:
  data = f.read()
with open(r"C:\Users\dell\Downloads\midterm_files(1) (1)\midterm_files\EnglishWords.txt","r",encoding="utf8")as f:
  dic = f.readlines()
  number = len(dic)
  print("Formatting ###################")
  for i in range(len(data)):
    s0 = ["A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"]
    upper = 0
    if data[i] in s0:
      upper += 1
      data[i] = data[i].lower()
      print("Number of upper case words transformed:",upper)

    s1=[",", ".", "!", "?", "...", "%", "<", ">", ":", ";"]
    punctuation = 0
    while data[i] in s1:
      data.remove(data[i])
      punctuation += 1
      print("Number of punctuation’s removed:",punctuation)

    nn = 0
    s2 = ["1,2,3,4,5,6,7,8,9,0"]
    while data[i] in s2:
      data.remove(data[i])
      nn += 1
      print("Number of punctuation’s removed:",nn)

  print("Spellchecking ###################")
  print("Number of words:",number)
  for i in data:
    n=0
    inn=0
    if i in dic:
      n+=1
    print("“Number of correct words in file:",n)
  else:
    inn+=1
    print("Number of incorrect words in file:",inn)
