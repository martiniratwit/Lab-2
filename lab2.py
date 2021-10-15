#Git repo (add prof.memo), add main function, picture of pong, requirments.txt
import pygame
WIDTH = 800
HEIGHT = 480

def main():
    pass

pygame.init()

pygame.display.set_caption("lab 2")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()

# define a variable to control the main loop
running = True
     
# main loop
while running:
    # event handling, gets all event from the event queue
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,0),(20,HEIGHT)))
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,0),(WIDTH,20)))
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,460),(WIDTH,20)))
    pygame.display.update()
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
    
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
# call the main function
    main()