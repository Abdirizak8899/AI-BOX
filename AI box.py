import pygame as pyg ,random as rand ,time , sys , datetime
from pygame.locals import *
# screen peparation
check_errs = pyg.init()#initializig the game screen
sw,sh = 600,400 #screen width and screen hight  
screen = pyg.display.set_mode([sw,sh])
pyg.display.set_caption('Ai boxes')

# pygame init look like this [5,0]  
# if digit one greater than 0 that means there is error else gonna initializing successfull
if check_errs[1] > 0:
	print('{check_errs[1]} Error accured game not initialized successfully!')
else:
	print('[+1] Game initialized successfully! with {check_errs[1]} Zero error')
# GAME VARIABLES
fps = pyg.time.Clock()#frame per second
obstacle_poss = [[0,-10],[200,200]]
score = 0
value = 0
speed = 5
pyg.font.init()

obstacle1 = False
obstacle2 = False
obstacle3 = False


# functions

# player functions
def player_variables():
	global player_pos 
	global right 
	global left
	global up 
	global down 
	global player_speed 
	global player_width
	global player_hight
	player_pos = [sw//2,sh//2-10]
	right = False
	left =False
	up =False
	down =False
	player_speed = 10
	player_width,player_hight = 20,20
player_variables()
def draw_player(screen):
	pyg.draw.rect(screen,"tomato",[player_pos[0],player_pos[1],20,20])
def move_player(key_pressed):
	if key_pressed[K_RIGHT] and player_pos[0] <= sw-player_width-10:
		player_pos[0] += player_speed
	elif key_pressed[K_LEFT] and player_pos[0] >=0+10:
		player_pos[0] -= player_speed
	elif key_pressed[K_UP] and player_pos[1] >=0+10:
		player_pos[1] -= player_speed
	elif key_pressed[K_DOWN] and player_pos[1] <= sh-player_hight-10:
		player_pos[1] += player_speed
# enemy functions
def obstacle_variable():
	global obstacle_pos
	global obstacle_width
	global obstacle_hight
	global obstacle_speed
	obstacle_pos = [100,200]
	obstacle_width = 20
	obstacle_hight = 20
	obstacle_speed = 1
obstacle_variable()
def draw_obstacle(screen):
	pyg.draw.rect(screen,"red",[obstacle_pos[0],obstacle_pos[1],obstacle_width,obstacle_hight])
def move_obstacles():
	if obstacle_pos[0] > player_pos[0]:
		obstacle_pos[0] -= obstacle_speed
	elif obstacle_pos[0] < player_pos[0]:
		obstacle_pos[0] += obstacle_speed
	elif obstacle_pos[1] > player_pos[1]:
		obstacle_pos[1] -= obstacle_speed
	elif obstacle_pos[1] < player_pos[1]:
		obstacle_pos[1]+=obstacle_speed

# new obstacle
def new_obstacle1():
	global obstacle_poss
	for  i in range(1):
		pos = obstacle_poss[0]
		x = pos[0]
		y = pos[1]
		pyg.draw.rect(screen,"green",[x,y,obstacle_width,obstacle_hight])

def new_obstacle2():
	global obstacle_poss
	for  i in range(1):
		pos = obstacle_poss[1]
		x = pos[0]
		y = pos[1]
		pyg.draw.rect(screen,"white",[x,y,obstacle_width,obstacle_hight])


def score_count(score):
	myFont = pyg.font.SysFont("monospace", 16)
	text = "Score:" + str(score)
	label = myFont.render(text, 1, "YELLOW")
	screen.blit(label, (30,5))

def outomove_obstacle1():
	global speed
	position = obstacle_poss[0]
	if position[0] > player_pos[0]:
		position[0] -= speed-3
	elif position[0] < player_pos[0]:
		position[0] += speed-3
	elif position[1] > player_pos[1]:
		position[1] -= speed-3
	elif position[1] < player_pos[1]:
		position[1] += speed-3

def outomove_obstacle2():
	global speed
	position = obstacle_poss[1]
	if position[0] > player_pos[0]:
		position[0] -= speed
	elif position[0] < player_pos[0]:
		position[0] += speed
	elif position[1] > player_pos[1]:
		position[1] -= speed
	elif position[1] < player_pos[1]:
		position[1] += speed


def detect_collision(player_pos,obstacle_poss):
	for pos in obstacle_poss:
		if pos == player_pos or obstacle_pos == player_pos:
			return True
		return False


gameover = False
while not gameover:
	screen.fill("black")
	fps.tick(120)
	player = draw_player(screen)
	obstacle = draw_obstacle(screen)
	#event handling 
	for event in pyg.event.get():
		if event.type == QUIT:
			gameover = True
	key_pressed = pyg.key.get_pressed()
	move_player(key_pressed)
	move_obstacles()
	if detect_collision(player_pos,obstacle_poss):
		gameover = True
	#------------------------- 
	score_count(score)
	value +=1
	if value ==70:
		score +=1
		value = 0
# -----------------------
	if score >20:
		new_obstacle1()
		outomove_obstacle1()
	if score > 50:
		new_obstacle2()
		outomove_obstacle2()
	pyg.display.flip()