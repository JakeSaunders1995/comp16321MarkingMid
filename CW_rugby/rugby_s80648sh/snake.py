#Made with 1920x1080 resolution.
from tkinter import *
import random
def set_dimensions(width,height):
	game_window = Tk() #  Initialises new window
	game_window.title("Coursework Snake Game")

	screen_width = game_window.winfo_screenwidth()
	screen_height = game_window.winfo_screenheight() #  Gets computers screen-size

	#Calculates the center of the screen
	x = int((screen_width/2) - (width/2))
	y = int((screen_height/2) - (height/2))

	#game_window.geometry('%dx%d+%d+%d' %(width, height, x, y)) 
	game_window.geometry(f"{screen_width}x{screen_height}+{x}+{y}") 	
	return game_window

def set_arrow_bindings():
	canvas.bind("<Left>", left_key)
	canvas.bind("<Right>", right_key)
	canvas.bind("<Up>", up_key)
	canvas.bind("<Down>", down_key)
	canvas.focus_set()

def place_food():
	global food, food_x, food_y
	#  Rectangle = (x1,y1,x2,y2)
	food = canvas.create_rectangle(0,0, snakeSize, snakeSize,
		fill ="steel blue")
	
	food_x = random.randint(0, width-snakeSize)
	food_y = random.randint(0, height-snakeSize) #  Generates X and Y coordinates
	canvas.move(food, food_x, food_y)


# If choice == 0
def left_key(event):
	global direction
	direction = "left"

def right_key(event):
	global direction
	direction = "right"

def up_key(event):
	global direction
	direction = "up"

def down_key(event):
	global direction
	direction = "down"

def grow_snake():
	final_body = len(snake)-1
	final_body_pos = canvas.coords(snake[final_body]) #  Will be 2 coordinates (x1,y1)(x2,y2)

	snake.append(canvas.create_rectangle(0,0, 
						snakeSize,snakeSize,
						fill ="#FDF3F3")
				) #  Creates a new snake block (not placed on snake)

	if direction == "left": #Placed to right of last
		canvas.coords(snake[final_body+1], 
			final_body_pos[0]+ snakeSize,
			final_body_pos[1],
			final_body_pos[2] + snakeSize,
			final_body_pos[3])
	elif direction == "right": #Placed to left of last
		canvas.coords(snake[final_body+1], 
			final_body_pos[0] - snakeSize,
			final_body_pos[1],
			final_body_pos[2] - snakeSize,
			final_body_pos[3])
	elif direction == "up": #Placed to bottom of last
		canvas.coords(snake[final_body+1], 
			final_body_pos[0],
			final_body_pos[1] + snakeSize,
			final_body_pos[2],
			final_body_pos[3] + snakeSize)
	elif direction == "down": #Placed to top of last
		canvas.coords(snake[final_body+1], 
			final_body_pos[0],
			final_body_pos[1] - snakeSize,
			final_body_pos[2],
			final_body_pos[3] - snakeSize)
		
#The canvas works so tranlsation from (0,0) to (15,15)
#Involves moving 15 to the right and 15 downwards.

def move_food():
	global food,food_x,food_y
	canvas.move(food,food_x*(-1), food_y*(-1))
	food_x = random.randint(0,width-snakeSize)
	food_y = random.randint(0,height-snakeSize)
	canvas.move(food, food_x, food_y)

	#Incrementing Score:
	global score
	score += 1 
	txt = "score:" + str(score)
	canvas.itemconfigure(scoreText, text=txt) 

def overlapping(a,b): #  Collision Checking Positions[a] and Positions[b]
	if a[0] < b[2] and a[1] < b[3] and a[2] > b[0] and a[3] > b[1]:
	    return True
	return False

def move_snake():
	
	def follow_head(positions,snake):
		for i in range(1,len(snake)):
			positions.append(canvas.coords(snake[i])) #  Gets all element coordinates
	
		for i in range(len(snake) -1): #  Allows body to follow the head.
			canvas.coords(snake[i+1],
				positions[i][0],
				positions[i][1],
				positions[i][2],
				positions[i][3])

	def constant_movement():
		if direction == "left":
			canvas.move(snake[0],-snakeSize,0) 
		elif direction == "right":
			canvas.move(snake[0],snakeSize,0)
		elif direction == "up":
			canvas.move(snake[0],0,-snakeSize)
		elif direction =="down":
			canvas.move(snake[0],0,snakeSize)

	def check_boundary():
			if positions[0][0] < 0: # Left Wall			
				canvas.coords(snake[0],width,positions[0][1],
				    width-snakeSize, positions[0][3])

			elif positions[0][2] > width: #  Right Wall
				canvas.coords(snake[0],0-snakeSize,positions[0][1],
					0,positions[0][3]) 

			elif positions[0][3] > height: #  Top wall
				canvas.coords(snake[0],positions[0][0],0-snakeSize,
					positions[0][2], 0)

			elif positions[0][1] < 0: #  Bottom Wall
				canvas.coords(snake[0],positions[0][0],height,
					positions[0][2],height-snakeSize)

	game_over = False

	canvas.pack()
	positions = []
	positions.append(canvas.coords(snake[0])) #CurPos of Head (x1,y1) (x2,y2)

	
	check_boundary() 

	positions.clear()
	positions.append(canvas.coords(snake[0]))

	
	constant_movement()


	head_position = canvas.coords(snake[0])
	food_position = canvas.coords(food)

	if overlapping(head_position,food_position): #  == True
	   move_food()
	   grow_snake()

	for i in range(1,len(snake)):
		next_body = canvas.coords(snake[i])
		if overlapping(head_position,next_body): #  If head collides with body:
			game_over = True
			canvas.create_text(width/2,height/2,
				fill ="white",
				font ="Times 20 italic bold",
				text ="Game Over!"
				)

	follow_head(positions,snake)


	if game_over == False: 
		window.after(90,move_snake) #  Loops through, Parameter 1 controls speed



width = 1900 #  Dimensions of window.
height = 900
window = set_dimensions(width,height)

#Sets property width to variable width
canvas = Canvas(window, bg="black", 
	width=width,height=height) 
snake = []
snakeSize = 15

#Creates the head of the snake     Point (15,15) size (30,30)
snake.append(canvas.create_rectangle(snakeSize,snakeSize, 
	snakeSize *2 , snakeSize*2 , 
	fill = "white"))

# Score Text
score = 0
text = "Score:" + str(score)
scoreText = canvas.create_text(width/2 , 12,
 fill="white", font ="Times 20 italic bold", text = text)

set_arrow_bindings()

direction = "right" #  Initial Direction

place_food()
move_snake()

window.mainloop() #  Waits for events in window

