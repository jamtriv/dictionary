import pgzrun  # importing pygame0 module
import pygame  # importing pygame module
import math  # importing math module
import random


def update():  # defining update
    pass  # used to add above function for syntax, for pygame


def draw(coods):  # defining draw
    screen.fill((0, 0, 0))  # filling screen with black colour

    def draw_eye(coordinates):  # defining function to draw eyes
        eye_x, eye_y = coordinates

        mouse_x, mouse_y = pygame.mouse.get_pos()  # getting x and y from mouse position.

        distance_x = mouse_x - eye_x  # math to figure out the mouse is in relation to the eye
        distance_y = mouse_y - eye_y  # math to figure out the mouse is in relation to the eye

        distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2),
                       30)  # math to figure out the actual distance, and not moving the eye.
        angle = math.atan2(distance_y, distance_x)  # math to figure out the reserve tan of the x and y distance

        pupil_x = eye_x + (math.cos(angle) * distance)  # finding cos of angle and then multiplying by the distance
        pupil_y = eye_y + (math.sin(angle) * distance)  # finding sin of angle and then multiplying by the distance

        screen.draw.filled_circle((coordinates), 50, color=(255, 255, 255))  # drawing eye outline
        screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))  # drawing eye pupil

        # pygame window, x= 800, y= 600

    coordinates = coods
    draw_eye(coordinates)

    """eye_coordinates = [(100, 367),
                       (487, 54),
                       (321, 287),
                       (145, 491),
                       (800, 300),
                       (500, 234),
                       (0, 45)
                       ]"""


random_coordinates = [(random.randrange(100, 600), random.randrange(100, 600)) for i in range(1)]

for eyes in random_coordinates:
    draw(eyes)

pgzrun.go()  # runs the game, looks for functions update and draw.
