import pgzrun                                                                 #importing pygame0 module
import pygame                                                                 #importing pygame module
import math                                                                   #importing math module
import random


def update():                                                                 #defining update
    pass                                                                      #used to add above function for syntax, for pygame

def draw():                                                                   #defining draw
    screen.fill((0, 0, 0))                                                    #filling screen with black colour

    def draw_eye(eye_x, eye_y):                                               #defining function to draw eyes
        mouse_x, mouse_y = pygame.mouse.get_pos()                             #getting x and y from mouse position.


        distance_x = mouse_x - eye_x                                          #math to figure out the mouse is in relation to the eye
        distance_y = mouse_y - eye_y                                          #math to figure out the mouse is in relation to the eye

        distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2), 30)      #math to figure out the actual distance, and not mnoving the eye.
        angle = math.atan2(distance_y, distance_x)                            #math to figure out the reserve tan of the x and y distance

        pupil_x = eye_x + (math.cos(angle) * distance)                        #finding cos of angle and then mutiplying by the distance
        pupil_y = eye_y + (math.sin(angle) * distance)                        #finding sin of angle and then mutiplying by the distance

        screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))  #drawing eye outline
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))  #drawing eye pupil

    eye1_x = 100
    eye1_y = 367
    eye2_x = 487
    eye2_y = 54
    eye3_x = 321
    eye3_y = 287
    eye4_x = 145
    eye4_y = 491

    #list_of_pairs = [
        #(100, 200),
        #(200, 300),
        #(300, 400),
        #(400, 500),
    #]

    #random_coordinates = random.choice(list_of_pairs)
    #print (random_coordinates)

    draw_eye(eye1_x, eye1_y)                                                        #ACTUALLY drawing the eye1, but calling the function to draw the eye
    draw_eye(eye2_x, eye2_y)                                                        #ACTUALLY drawing the eye2, but calling the function to draw the eye
    draw_eye(eye3_x, eye3_y)
    draw_eye(eye4_x, eye4_y)




pgzrun.go()                                                                   #runs the game, looks for functions update and draw.