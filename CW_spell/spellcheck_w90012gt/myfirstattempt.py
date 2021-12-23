
import time, os

print ("Loading. . . .")
time.sleep(1)

playerSettings=list()
with open ("settings.txt") as file:
	playerSettings = file.readlines()


playerSettings = [line.rstrip('\n') for line in open("settings.txt")]

print (" Welcome to my game " + playerSettings[0] + "\nPlease choose a hero" )
heroList = ["StormTrooper", "Battle Droid", "Bounty Hunter level 1"]

for idx, val in enumerate (heroList, start = 1):
	print(str(idx) + ". " + val)

YourHero= int (input("Type in your hero number: "))



playerSettings[1]= heroList[YourHero-1]


print("You choose: " + playerSettings[1])

# settingsMenu = ['PlayerName', 'characterName', 'characterAge', 
# 'View Current Settings']


while True:
	menu =  input("Would you like to start the game (Type 1)" 
		", change settings (type 2)" + ", view the settings (Type 3)"
		+ " or save game (Type 4) ")




	if (menu=="1"):
		move = input ("\n" + playerSettings[1] + ", Do you want to move? ")
		print (move)
		count = 0
		while move in ('Yes', 'yes', 'YES', 'y', 'Y'):
			print("You moved 1 space!")
			move = input ("Keep moving? ")
			count +=1
		else:
			print("You moved " + str(count) + " times. Nice!")
			playerSettings[3] = int (playerSettings[3]) + count
			with open ("settings.txt", "w") as file:
				for item in playerSettings:
					file.write("%s\n" % item)
			

	elif (menu == "2"):
		
		
		

		settingChange = int (input("What do you want to change? "))
		newValue = input ("What is the new setting? ")
		playerSettings[settingChange-1] = newValue

	elif (menu == "3"):
		
		print("Name: %s \nHero name: %s \nHero Age: %s" % 
			(playerSettings[0], playerSettings[1], playerSettings[2]))

	elif (menu == "4"):
		
		with open ("settings.txt", "w") as file:
			for item in playerSettings:
				file.write("%s\n" % item)
		time.sleep(2)
		print("Game saved... \n")

	else:
		print("Not a valid input! Try again")