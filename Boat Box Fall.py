#Made by Vilhelm Prytz 2016.
#Just testing, before my real deal game comes out!

#init pygame
import pygame
import sys
import time
import random
pygame.init()

display_width = 1280
display_height = 720

display_width_s = 1280
display_height_s = 720

file_res_height = open("res_height.txt", "r")
display_height_s = file_res_height.read()
file_res_height.close()
#file_res_height = 
#file_res_height.close()

file_res_width = open("res_width.txt", "r")
display_width_s = file_res_width.read()
file_res_width.close()
#file_res_width = 
#file_res_width.close()

display_height = int(display_height_s)
display_width = int(display_width_s)

#vars
#display_width = 1280
#display_height = 720
car_width = 100
version = "1.2"

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

green2 = (0,200,0)
red2 = (200,0,0)

print("Hello!")
print("setting up window")
print("To change resolution, please change the res_height.txt and res_width.txt files!")

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Boat Box Fall")

clock = pygame.time.Clock()

boatImg = pygame.image.load("img/img.png")


def objects_dodged(count):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Dodged: " + str(count), True, black)
        gameDisplay.blit(text, (0, 50))
def quitGame():
        pygame.quit()
        quit(0)

def object(objectX, objectY, objectW, objectH, color):
        pygame.draw.rect(gameDisplay, color, [objectX, objectY, objectW, objectH])

def boat(x,y):
        gameDisplay.blit(boatImg, (x,y))

def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

def message_display(text, size):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

def message_display_corner(text, size):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (130,15)
        gameDisplay.blit(TextSurf, TextRect)
def message_display_cornerd(text, size):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (50,35)
        gameDisplay.blit(TextSurf, TextRect)
        
def crash():
        message_display_corner("Made by Vilhelm Prytz.", 20)
        message_display_cornerd("Deaths: " + str(deaths), 20)
        message_display("You crashed! :(", 115)
        game_loop()
def button(msg, x, y, w, h, iColor, aColor, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, aColor, (x,y,w,h))
                if click[0] == 1 and action != None:
                        #sloopy, not good :/
                        action()
                                
        else:
                pygame.draw.rect(gameDisplay, iColor, (x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)

def game_intro():
        intro = True
        while intro:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit(0)
                                
                gameDisplay.fill(white)
                largeText = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("Boat Box Fall", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)

                button("PLAY", display_width/2-100,display_height/2+100,100,50, green, green2, game_loop)
                button("QUIT", display_width/2+150,display_height/2+100,100,50, red, red2, quitGame)
                
                pygame.display.update()
                clock.tick(120)

def game_loop():
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        
        x_change = 0

        global deaths
        
        object_width = 100
        object_height = 100
        object_startX = random.randrange(0, display_width - object_width)
        object_startY = -600
        object_speed = 5

        object_inner_width = 60
        object_inner_height = 60

        dodged = 0


        gameExit = False

        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                                pygame.quit()
                                quit(0)
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        print("left key pressed")
                                        x_change = -5
                                if event.key == pygame.K_RIGHT:
                                        print("right key pressed")
                                        x_change = 5
                                if event.key == pygame.K_UP:
                                        print("up key pressed")
                                if event.key == pygame.K_DOWN:
                                        print("down key pressed")
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        x_change = 0
                                        print("key released")
                x += x_change
                
                gameDisplay.fill(white)
                
                #object(objectX, objectY, objectW, objectH, color)
                object(object_startX, object_startY, object_width, object_height, red)
                object(object_startX + 20, object_startY + 20, object_inner_width, object_inner_height, green)
                object_startY += object_speed
                boat(x,y)
                objects_dodged(dodged)

                if x > display_width - car_width or x < 0:
                        deaths = deaths+1
                        print("Deaths: " + str(deaths))
                        crash()
                        

                if object_startY > display_height:
                        object_startY = 0 - object_height
                        object_startX = random.randrange(0,display_width - int(object_width))
                        dodged += 1
                        object_speed += 1
                        object_width += (dodged * 1.2)
                        object_inner_width += (dodged * 1.2)
                        print("Dodged: " + str(dodged))
                        
                        
                #crash in objects detect
                if y < object_startY+object_height:
                        print("Y crossover")
                        if x > object_startX and x < object_startX + object_width or x+car_width > object_startX and x + car_width < object_startX+object_width:
                                print("x crossover")
                                deaths = deaths+1
                                print("Deaths: " + str(deaths))
                                crash()

                message_display_corner("Made by Vilhelm Prytz " + version, 20)
                message_display_cornerd("Deaths: " + str(deaths), 20)
                
                pygame.display.update()
                clock.tick(60)
deaths = 0
game_intro()
game_loop()
pygame.quit()
quit(0)
