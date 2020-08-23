import pygame
from sys import exit

pygame.init()

clock_tick_rate=20

width = 950
height = 825
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("chinese chess")


clock = pygame.time.Clock()
background_image=pygame.image.load("background.jpg").convert()

#color def
color_black=(0,0,0)
color_white=(255,255,255)
color_goldenrod=(218,165,32)
color_red=(255,0,0)
color_blue=(0, 0, 255)
color_navy=(97, 218, 252)

#define bottoms at left
class  bottom():
        def __init__(self, color, x, y, width, height, text=""):
                self.color=color
                self.x=x
                self.y=y
                self.width=width
                self.height=height
                self.text=text

        def draw(self, screen, outline=None): 
                 #Call this method to draw the button on the screen
                if outline:
                        pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
                        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
                if self.text != '':
                        font = pygame.font.SysFont('comicsans', 25)
                        text = font.render(self.text, 1, (0,0,0))
                        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, mouse_position):
                #Pos is the mouse position or a tuple of (x,y) coordinates
                if mouse_position[0] > self.x and mouse_position[0] < self.x + self.width:
                        if mouse_position[1] > self.y and mouse_position[1] < self.y + self.height:
                                return True
                return False

        
NewGameButtom = bottom ( (color_goldenrod), 50, 200, 100, 50, 'New Game')
WithdrawButtom = bottom ( (color_goldenrod), 50, 350, 100, 50, 'Withdraw')
QuitButtom = bottom( (color_goldenrod), 50, 500, 100, 50, 'Quit')

pygame.display.update()


while True:

        #Get mouse position
        mouse_position = pygame.mouse.get_pos()

        #events
        for event in pygame.event.get():
                
                #quit with X?
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
                #mouse button down?
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if NewGameButtom.isOver(mouse_position):
                                print("new game")
                        if WithdrawButtom.isOver(mouse_position):
                                print("withdraw")
                        if QuitButtom.isOver(mouse_position):
                                pygame.quit()
                                exit()
                        
        #set background image
        screen.blit(background_image, (0, 0))

        #set FPS
        clock.tick(clock_tick_rate)

        #draw buttoms
        NewGameButtom.draw(screen, color_black)
        WithdrawButtom.draw(screen,color_black)
        QuitButtom.draw(screen,color_black)

        #draw line between board and bottoms
        pygame.draw.line(screen ,color_white ,(200,0) ,(200,825), 2)
        
        #draw chess board
        i=75
        while i <= 750:
               pygame.draw.line(screen, color_black, (275,i), (875,i) )
               i+=75
               
        j=350
        while j <= 875:
                pygame.draw.line(screen, color_black, (j,75), (j,375))
                pygame.draw.line(screen, color_black, (j,450), (j,750))
                j+=75
        pygame.draw.line(screen, color_black, (275,75), (275,750) )
        pygame.draw.line(screen, color_black, (875,75), (875,750) )
        
        #bold line 
        pygame.draw.line(screen, color_black, (265,65), (265,760), 2)
        pygame.draw.line(screen, color_black, (265,760), (885,760), 2)
        pygame.draw.line(screen, color_black, (885,760), (885,65), 2)
        pygame.draw.line(screen, color_black, (885,65), (265,65), 2)
    


        #buttoms change color
        if NewGameButtom.isOver(mouse_position):
                NewGameButtom.color=(color_navy)
        else:
                NewGameButtom.color=(color_goldenrod)
                
        if WithdrawButtom.isOver(mouse_position):
                WithdrawButtom.color=(color_navy)
        else:
                WithdrawButtom.color=(color_goldenrod)
                
        if QuitButtom.isOver(mouse_position):
                QuitButtom.color=(color_navy)
        else:
                QuitButtom.color=(color_goldenrod)

        

        pygame.display.flip()
