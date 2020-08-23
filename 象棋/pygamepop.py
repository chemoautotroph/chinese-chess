import pygame
from sys import exit

pygame.init()

clock_tick_rate=20

width = 1100
height = 825
#board_width = 200
#board_height = 400
screen = pygame.display.set_mode((width,height))
#board = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("象棋")


clock = pygame.time.Clock()
background_image=pygame.image.load("background.jpg").convert()
#background_color=board.fill(color_goldenrod)

#color def
color_black=(0,0,0)
color_white=(255,255,255)
color_goldenrod=(218,165,32)




while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

        screen.blit(background_image, (0, 0))
        clock.tick(clock_tick_rate)

        
        pygame.draw.line(screen ,color_white ,(200,0) ,(200,825), 2)

        #draw chess board
        i=75
        while i <= 750:
               pygame.draw.line(screen, color_black, (275,i), (1025,i) )
               i+=75
                
        pygame.draw.line(screen, color_black, (275,75), (275,750) )
        pygame.draw.line(screen, color_black, (1025,75), (1025,750) )
        
        pygame.draw.line(screen, color_black, (265,65), (265,760), 2)
        pygame.draw.line(screen, color_black, (265,760), (1035,760), 2)
        pygame.draw.line(screen, color_black, (1035,760), (1035,65), 2)
        pygame.draw.line(screen, color_black, (1035,65), (265,65), 2)

        
        j=350
        while j <= 1025:
                pygame.draw.line(screen, color_black, (j,75), (j,375))
                pygame.draw.line(screen, color_black, (j,450), (j,750))
                j+=75


        pygame.display.flip()
