import pgzrun
from pgzero.builtins import *
from pgzero.actor import Actor 
import pygame
from random import randint
import pgzero.screen
screen : pgzero.screen.Screen
pygame.font.init()

pygame.init()
WIDTH = 800
HEIGHT = 600 

space = Actor("space")
ring = Actor("ring")
ring.pos = [400, 300]


player = Actor("player")
player.pos = [400, 550]



spaceship = Actor("spaceship")
spaceship.pos = [125, 200]

startbar = Actor("startbar")
startbar.pos = [400, 440]


life_span = []
for x in range(0, 32, 32):
    for y in range(90, 32, 32):
        vie3 = Actor("life", anchor=["left", "top"])
        vie3.pos = [x,y]
        life_span.append(vie3)

for x in range(90, 32*2, 32):
    for y in range(0, 32, 32):
        vie2 = Actor("life", anchor=["left", "top"])
        vie2.pos = [x,y]
        life_span.append(vie2)

for x in range(0, 96, 32):
    for y in range(0,32, 32):
        vie = Actor("life", anchor=["left", "top"])
        vie.pos = [x,y]
        life_span.append(vie)

all_bricks = []

for x in range(0, 800, 100):
    for y in range(0,30*1, 30):
        brick = Actor("brick", anchor=["left", "top"])
        brick.pos = [x,y]
        all_bricks.append(brick)
for x in range(0, 800, 100):
    for y in range(0,30*1, 30):
        brickbluebrok = Actor("brickbluebrok", anchor = ["left", "top"])
        brickbluebrok.pos=[x,y]
        brickbluebrok.pos = [x,y]
        all_bricks.append(brickbluebrok) 
for x in range(0, 800, 100):
    for y in range(0,30*1, 30):
        brokbrick = Actor("brokbrick", anchor = ["left", "top"])
        brokbrick.pos=[x,y]
        brokbrick.pos = [x,y]
        all_bricks.append(brokbrick) 


player = Actor("player")
player.pos = [400, 550]

#player2 = Actor("petit")
#player.pos = [400, 550]

ball =Actor("ball")
ball.pos = [400, 500]
ball_speed = [5,-5]

background = Actor("back") #mettre une image en fond
planet = Actor("planet")



gameover = Actor("gameover")
gameover.pos = [400, 300]

game_state = "Start"

sound_can_play = True

def draw():


    screen.clear()
    if game_state == "Start":
        draw_start()
    if game_state == "Game":
        draw_game()
    if game_state == "Game Over":
        draw_gameover()
    if game_state == "You Win":
        draw_youwin()


def draw_start():
   
    intro_music()
    screen.clear()
    

    
    space.draw()
    ring.draw()
    startbar.draw()
   
    screen.draw.text("START", (280, 400), fontsize = 100, owidth=1.5, ocolor=(255,255,0), color = "purple")
    

def click():
    sounds.click.play()

def on_mouse_down(pos):
    global game_state
    global sound_can_play
    if startbar.collidepoint(pos):
        print("CIAO")
        click()
        game_state = "Game"
        sound_can_play = True



def intro_music():
    global sound_can_play
    if sound_can_play:
        sounds.atmo.play()
        sound_can_play = False
        #sound_can_play = True

def intro_stop():
    
    sounds.atmo.stop()
       
           
        





def soundtrack():
    global sound_can_play
    
    if sound_can_play:
        sounds.space.play()
        sound_can_play = False
       

def stop_soundtrack():
    sounds.space.stop()


def draw_game():
    global sound_can_play
    
    screen.clear()
    intro_stop()
    #sound_can_play == True
    soundtrack()
    background.draw()
    planet.draw()

    spaceship.draw()

    for brick in all_bricks:
        brick.draw()
       
    for vie in life_span:
        vie.draw()
    
    
    player.draw()
   
  
    ball.draw()

    
   




def update():
    global game_state
    global sound_can_play

    if game_state != "Game":
        return

    #if sound_can_play == False:
        #return
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()
        
    if ball.top <0 or ball.bottom > HEIGHT:
        invert_vertical_speed()

    life_loss = []

    if ball.bottom > HEIGHT:
        ball.pos = [400, 300]
        acceleration()

        for vie in reversed(life_span):
            life_loss.append(vie)
            if vie.image == "life":
                bruit_life()

            break


    for vie in life_loss:
        life_span.remove(vie)

    if len(life_span) == 0:
        global sound_can_play
        sound_can_play = True
        game_state = "Game Over"


    if ball.colliderect(player):
        invert_vertical_speed()
        bruit_bounce()

    to_delete = []
    for brick in reversed(all_bricks):
        if ball.colliderect(brick):
            to_delete.append(brick)
            invert_vertical_speed()
            if brick.image == "brick":
                bruit_brick()
                
            if brick.image == "brickbluebrok":
                bruit_blue()
               
            else:
                bruit_tuile()
            break   

    for brick in to_delete:
        all_bricks.remove(brick)        

    if len(all_bricks) ==0:
        game_state = "You Win"
        sound_can_play = True





def acceleration():
    ball_speed[0] = 6.5
    ball_speed[1] = 6.5

def bruit_blue():
    sounds.brickblue.play()   

def bruit_life():
    sounds.lose_life.play()

def life_stop():
    sounds.lose_life.stop()

def bruit_brick():
    sounds.explosion.play()

def bruit_lose():
    sounds.phaserdown.play()    

def bruit_bounce():
    sounds.phasejump.play()

def bruit_tuile():
    sounds.drop.play()     

def invert_horizontal_speed():
    ball_speed[0] *= -1

def invert_vertical_speed():
    ball_speed[1] *= -1

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]
    #player2.pos = [pos[0], player2.pos[1]]
 
#def remplacement():
    #if len(life_span) <= 1:   
        #player.image == player2

def draw_gameover():
    intro_stop() 
    stop_soundtrack()
    
    gameover.draw()
    
    demon()


def demon():
    global sound_can_play
    if sound_can_play:

        sounds.demonwav.play()
        sound_can_play = False


win = Actor("cat")
win.pos = [375, 400]

def youwin():
    global sound_can_play
    if sound_can_play:
        sounds.victory.play()
        sound_can_play = False
    
        
    
def draw_youwin():
    life_stop()
    stop_soundtrack()
    youwin()
    screen.clear()
    win.draw()

    screen.draw.text("YOU WIN !", (225, 10), fontsize = 100, owidth=1.5, ocolor=(255,255,0), color = "purple")
pgzrun.go()