import pygame
from sys import exit

pygame.init()

clock_tick_rate=20

width = 800
height = 600
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

        
        pygame.draw.line(screen ,color_white ,(200,0) ,(200,600), 2)

        #draw chess board
        i=75
        while i <= 525:
                pygame.draw.line(screen, color_black, (300,i), (700,i) )
                i+=50
                
        pygame.draw.line(screen, color_black, (300,75), (300,525) )
        pygame.draw.line(screen, color_black, (700,75), (700,525) )
        
        j=300
        while j <= 700:
                pygame.draw.line(screen, color_black, (j,75), (j,275))
                pygame.draw.line(screen, color_black, (j,325), (j,525))
                j+=50


        pygame.display.flip()
