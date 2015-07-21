from pygame.locals import *
import pygame, sys, eztext

def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((2*640,2*240))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = eztext.Input(maxlength=45, color=(0,0,0), prompt='Write code here to modify pylist: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!
    pylist = [1,2,3,4,5]
    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            if event.type==KEYDOWN and event.key==K_RETURN:
                if execute_and_check(txtbx.value, pylist):
                    print "EXCELLENT!"
                txtbx.value = ''
            # close it x button si pressed
            if event.type == QUIT: return

        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()
    
def execute_and_check(executable_code, pylist):
    exec executable_code
    if pylist == [1,2,3,4]:
        print "EXCELLENT"
if __name__ == '__main__': main()
