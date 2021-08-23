import pgzrun                                                                #importing pygame0 module
import pygame                                                                #importing pygame module
import math                                                                  #importing math moduke


def update():                                                                 #defining update
    pass                                                                      #used to add above function for syntax

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

        screen.draw.filled_circle((eye_x, eye_y), 50, color=(255, 255, 255))  #drawing eye1
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))  #drawing eye2


    draw_eye(200, 200)                                                        #ACTUALLY drawing the eye1, but calling the function to draw the eye
    draw_eye(330, 200)                                                        #ACTUALLY drawing the eye2, but calling the function to draw the eye



pgzrun.go()                                                                   #placeholder so game runs properly