#Program 1 - Rugby#
# # # # # # # # # #
# # # # # # # # # #
#Import the contents of the text into Python for subsequent operations
input_file_name = str (input("Please type the file name: "))
file = open ("./input_folder/" + input_file_name, "r")
scorerecord = file.read()

#set two team's starting total score and some other count variables
Team1total, Team2total = 0, 0

#while loop for the calculation
count = 0
i = 1
e = 2
while count < 5:
    if scorerecord[i] == "1": # if the value is 1 then do below
        if scorerecord[e] == "t": # to distinguish which strings in the file (t,c,p,d)
            Team1total = Team1total + 5
        elif scorerecord[e] == "c":
            Team1total = Team1total + 2
        elif scorerecord[e] == "p":
            Team1total = Team1total + 3
        elif scorerecord[e] == "d":
            Team1total = Team1total + 3
    elif scorerecord[i] == "2": #if the value is 2 then do below
        if scorerecord[e] == "t": # to distinguish which strings in the file (t,c,p,d)
            Team2total = Team2total + 5
        elif scorerecord[e] == "c":
            Team2total = Team2total + 2
        elif scorerecord[e] == "p":
            Team2total = Team2total + 3
        elif scorerecord[e] == "d":
            Team2total = Team2total + 3
    #end of loop, let count variables have increment
    i += 3
    e += 3
    count += 1

#here to compare two values to see which is larger and print out the winner
if Team1total > Team2total:
    print ("winner is T1")
elif Team1total < Team2total:
    print ("winner is T2")
elif Team1total == Team2total:
    print ("they are the same scores")

#print the final score directly
print (str(Team1total)+":"+str(Team2total))

#creat a txt document in the output folder to record the final scores
input_file_name = input_file_name.replace(".txt","") #at here I need to delete the string ".txt" which users typed in
filecreation = open ("./output_folder/" + input_file_name + "_s94292yy.txt", "a")
filecreation.write (str(Team1total)+":"+str(Team2total))
filecreation.close()
#close the file to do new loop
file.close()
