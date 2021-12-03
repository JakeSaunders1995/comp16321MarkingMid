#Imports
from tkinter import *
import random as rand


def start_game():
	global game_canvas
	global game_width
	global game_height
	global key_pressed
	global direction
	global player
	global player_size
	global y_velocity
	global can_jump
	global crates
	global falling_crates
	global crate_size
	global time
	
	main_menu_canvas.pack_forget()
	
	game_width = height
	game_height = height
	game_canvas = Canvas(root, bg="#CCCCCC", width=game_width, height=game_height)
	
	#Binding keys
	key_pressed = "" #Current key that is pressed
	direction = "" #Direction the player is moving
	game_canvas.bind("<Left>", left_key)
	game_canvas.bind("<Right>", right_key)
	game_canvas.bind("<KeyRelease-Left>", direction_key_released) #Checks when left key is released
	game_canvas.bind("<KeyRelease-Right>", direction_key_released) #Checks when right key is released
	game_canvas.bind("<Up>", up_key)
	game_canvas.focus_set()
	
	#Initialize game objects
	player_size = game_width/24
	player = game_canvas.create_rectangle(game_width-player_size, game_height-player_size, game_width, game_height, fill="black")
	y_velocity = 0 #Initial vertical speed
	can_jump = True #Boolean to check if the player can jump
	crates = []
	falling_crates = []
	crate_size = game_width/8
	time = 0
	
	
	game_canvas.pack()
	update_game()
	
	
def load_game():
	print("load game")
	

def leaderboard():
	print("leaderboard")


def settings():
	print("settings")


def main_menu():
	global main_menu_canvas
	
	#Create main menu
	main_menu_canvas = Canvas(root, bg="#CCCCCC", width=width, height=height)
	new_game_button = Button(main_menu_canvas, width=int(width*0.015), height=int(height*0.004), text="New Game", command=start_game)
	load_game_button = Button(main_menu_canvas, width=int(width*0.015), height=int(height*0.004), text="Load Game", command=load_game)
	leaderboard_button = Button(main_menu_canvas, width=int(width*0.015), height=int(height*0.004), text="Leaderboard", command=leaderboard)
	settings_button = Button(main_menu_canvas, width=int(width*0.015), height=int(height*0.004), text="Settings", command=settings)
	title_text = main_menu_canvas.create_text(width/2, height/8, fill="#333333" ,font="Times 60 bold", text="Crate Fall")
	
	new_game_button.place(x=(width/2)-(width*0.075), y=height/2)
	load_game_button.place(x=(width/2)-(width*0.075), y=(height/2)+(height*0.06))
	leaderboard_button.place(x=(width/2)-(width*0.075), y=(height/2)+(height*0.12))
	settings_button.place(x=(width/2)-(width*0.075), y=(height/2)+(height*0.18))
	main_menu_canvas.pack()


def left_key(event):
	global key_pressed
	global direction
	
	key_pressed = "left"
	direction = "left"


def right_key(event):
	global key_pressed
	global direction
	
	key_pressed = "right"
	direction = "right"


def direction_key_released(event):
	global key_pressed
	global direction
	
	direction = ""
	

def up_key(event):
	global key_pressed
	
	key_pressed = "up"


def move_crates():
	#Moves any crate that can fall downwards
	for crate in falling_crates:
		crate_pos = game_canvas.coords(crate)
		
		crate_pos[1] += game_width/80
		crate_pos[3] += game_width/80
		
		#Check collision with border
		if crate_pos[3] > game_height:
			crate_pos[1] = game_height-crate_size
			crate_pos[3] = game_height
			falling_crates.remove(crate)
		
		#Check collision with other crates
		check_collision_1 = check_crate_collision(crate_pos[0]+1, crate_pos[3])
		check_collision_2 = check_crate_collision(crate_pos[2]-1, crate_pos[3])
		if check_collision_1 != False:
			crate_pos[1] = check_collision_1[1] - crate_size
			crate_pos[3] = check_collision_1[1]
			falling_crates.remove(crate)
		elif check_collision_2 != False:
			crate_pos[1] = check_collision_2[1] - crate_size
			crate_pos[3] = check_collision_2[1]
			falling_crates.remove(crate)
			
		game_canvas.coords(crate, crate_pos[0], crate_pos[1], crate_pos[2], crate_pos[3])
		
	
def create_crate(tries):
	#Find a random position for the crate at the top of the screen
	x = (crate_size/3) * rand.randint(0, int((game_width/(crate_size/3)-3)))
	y = -crate_size
	
	#Check if there is a crate at the top already (crates have stacked to the top of the screen)
	check_collision_1 = check_crate_collision(x+1, y+1)
	check_collision_2 = check_crate_collision(x+crate_size-1, y+crate_size-1)
	if check_collision_1 == False and check_collision_2 == False:
		#Create crate
		crate = game_canvas.create_rectangle(game_width-crate_size, game_height-crate_size, game_width, game_height, fill="red")
		crates.append(crate)
		falling_crates.append(crate)
		game_canvas.coords(crates[len(crates)-1], x, y, x+crate_size, y+crate_size)
	else:
		#Try placing crate again up to 10 times (to avoid reaching recursion limit)
		if tries < 10:
			create_crate(tries+1)
	

def check_crate_collision(x, y):
	#Returns coords of the crate an object collides with
	for crate in crates:
		crate_pos = game_canvas.coords(crate)
		if x > crate_pos[0] and y > crate_pos[1] and x < crate_pos[2] and y < crate_pos[3]:
			return crate_pos
	return False

	
def calc_vertical_pos(velocity):
	result = [0,0] #[displacement, final velocity]
	gravity = 1
	
	#Displacement given as s = ut + 0.5gt^2 where here t=1, g>0
	result[0] = velocity + 0.5*gravity
	
	#Final velocity given as v = u + gt where here t=1, g>0
	result[1] = velocity + gravity
	
	return result


def move_player():
	global key_pressed
	global y_velocity
	global can_jump

	player_pos = game_canvas.coords(player)
	
	#Move player horizontally
	if direction == "left":
		player_pos[0] -= game_width/144
		player_pos[2] -= game_width/144
		#Check collision with border
		if  player_pos[0] < 0:
			player_pos[0] = 0
			player_pos[2] = player_size
		#Check collision with crates
		check_collision_1 = check_crate_collision(player_pos[0], player_pos[1])
		check_collision_2 = check_crate_collision(player_pos[0], player_pos[3])
		if check_collision_1 != False:
			player_pos[0] = check_collision_1[2]
			player_pos[2] = check_collision_1[2] + player_size
		elif check_collision_2 != False:
			player_pos[0] = check_collision_2[2]
			player_pos[2] = check_collision_2[2] + player_size
	
	elif direction == "right":
		player_pos[0] += game_width/144
		player_pos[2] += game_width/144
		#Check collision with border
		if player_pos[2] > game_width:
			player_pos[0] = game_width-player_size
			player_pos[2] = game_width
		#Check collision with crates
		check_collision_1 = check_crate_collision(player_pos[2], player_pos[1])
		check_collision_2 = check_crate_collision(player_pos[2], player_pos[3])
		if check_collision_1 != False:
			player_pos[0] = check_collision_1[0] - player_size
			player_pos[2] = check_collision_1[0]
		elif check_collision_2 != False:
			player_pos[0] = check_collision_2[0] - player_size
			player_pos[2] = check_collision_2[0]
		
	#Move player vertically and handle jumping
	if key_pressed == "up":
		key_pressed = ""
		if can_jump == True and y_velocity == 0:
			y_velocity = -game_height/36 #Initial jump speed
			can_jump = False
	
	vertical_calc = calc_vertical_pos(y_velocity)
	player_pos[1] += vertical_calc[0]
	player_pos[3] += vertical_calc[0]
	y_velocity = vertical_calc[1]
	
	#Check collision with border
	if player_pos[3] > game_height:
		player_pos[1] = game_height-player_size
		player_pos[3] = game_height
		#Since on the floor
		y_velocity = 0
		can_jump = True
		
	#Check collision with crates
	if y_velocity < 0: #Moving up so check ceilings
		check_collision_1 = check_crate_collision(player_pos[0], player_pos[1])
		check_collision_2 = check_crate_collision(player_pos[2], player_pos[1])
		if check_collision_1 != False:
			player_pos[1] = check_collision_1[3]
			player_pos[3] = check_collision_1[3] + player_size
			#Collided with ceiling so set y-velocity to 0
			y_velocity = 0
		elif check_collision_2 != False:
			player_pos[1] = check_collision_2[3]
			player_pos[3] = check_collision_2[3] + player_size
			#Collided with ceiling so set y-velocity to 0
			y_velocity = 0
	else: #Moving downwards so check floors
		check_collision_1 = check_crate_collision(player_pos[0], player_pos[3])
		check_collision_2 = check_crate_collision(player_pos[2], player_pos[3])
		if check_collision_1 != False:
			player_pos[1] = check_collision_1[1] - player_size
			player_pos[3] = check_collision_1[1]
			#Since on the floor
			y_velocity = 0
			can_jump = True
		elif check_collision_2 != False:
			player_pos[1] = check_collision_2[1] - player_size
			player_pos[3] = check_collision_2[1]
			#Since on the floor
			y_velocity = 0
			can_jump = True
	
	#Update player with new position
	game_canvas.coords(player, player_pos[0], player_pos[1], player_pos[2], player_pos[3])
	

def update_game():
	global time
	
	move_crates()
	move_player()
	
	if time % 60 == 0:
		create_crate(0)

	game_canvas.pack()
	time += 1
	#print(time)
	root.after(17, update_game) #Updates every frame at 60fps


def main():
	global root
	global width
	global height
	
	#Setting up the window
	width = 1280
	height = 720
	root = Tk()
	root.geometry(str(width)+"x"+str(height))
	root.title("My Game")

	main_menu()
	root.mainloop()
	
	
if __name__ == "__main__":
	main()


