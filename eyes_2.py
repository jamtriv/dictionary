import pgzrun  # importing pygame0 module
import pygame  # importing pygame module
import math  # importing math module
import random

random_eyes = random.randrange(0, 10)

random_coordinates = [(random.randrange(0, 800), random.randrange(0, 600)) for i in range(random_eyes)]

random_eye_outline_colour = [(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)) for i in
                             range(random_eyes)]
random_eye_pupil_colour = [(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)) for i in
                           range(random_eyes)]


#print(random_coordinates)
#print(random_eye_outline_colour)
#print(random_eye_pupil_colour)


def update():  # defining update
    pass  # used to add above function for syntax, for pygame


def draw():  # defining draw
    screen.fill((0, 0, 0))  # filling screen with black colour

    def draw_eye(coods, oc, pc):  # defining function to draw eyes

        eye_x, eye_y = coods

        #print(coods)
        #print(oc)
        #print(pc)

        mouse_x, mouse_y = pygame.mouse.get_pos()  # getting x and y from mouse position.

        distance_x = mouse_x - eye_x  # math to figure out the mouse is in relation to the eye
        distance_y = mouse_y - eye_y  # math to figure out the mouse is in relation to the eye

        distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2),
                       30)  # math to figure out the actual distance, and not moving the eye.
        angle = math.atan2(distance_y, distance_x)  # math to figure out the reserve tan of the x and y distance

        pupil_x = eye_x + (math.cos(angle) * distance)  # finding cos of angle and then multiplying by the distance
        pupil_y = eye_y + (math.sin(angle) * distance)  # finding sin of angle and then multiplying by the distance

        screen.draw.filled_circle(coods, 50, color=oc)  # drawing eye outline
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=pc)  # drawing eye pupil

        # pygame window, x= 800, y= 600

    for coordinates, outlineColour, pupilColour in zip(random_coordinates, random_eye_outline_colour, random_eye_pupil_colour):
        draw_eye(coordinates, outlineColour, pupilColour)



pgzrun.go()  # runs the game, looks for functions update and draw.
