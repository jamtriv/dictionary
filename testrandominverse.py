import random

random_colour = (234, 45, 189)

print(random_colour)

def invertColour(colour):
    inversedcolour = tuple(255 - x for x in colour)
    return inversedcolour

returnedIvertedColour = invertColour(random_colour)


invertColour(random_colour)
print(returnedIvertedColour)






#print(pupilColour)

