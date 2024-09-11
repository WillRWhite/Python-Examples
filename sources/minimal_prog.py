#!/usr/bin/env python
#
#
#
#
#

# documentation string of this module
"""
Minimal pygame program.
"""
# some informational variables
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 109 $"
__date__      = "$Date: 2007-04-03 18:00:40 +0200 (Di, 03 Apr 2007) $"
__license__   = ''
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"

#----------------------------- actual code --------------------------------

# import the pygame module, so you can use it
import pygame

# define a main function
def window():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((320,240))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if (event.type == pygame.QUIT):
                # change the value of "running" to False, to exit the main loop
                running = False
            elif (event.type == pygame.KEYDOWN):
                if event.key == ord("x"):
                    running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    window()
