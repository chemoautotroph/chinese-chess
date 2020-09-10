import pygame
from sys import exit

pygame.init()

clock_tick_rate=20

width = 950
height = 825
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("chinese chess")
pick = False

clock = pygame.time.Clock()
background_image=pygame.image.load("background.jpg").convert()

#color def
color_black=(0,0,0)
color_white=(255,255,255)
color_goldenrod=(218,165,32)
color_red=(255,0,0)
color_blue=(0, 0, 255)
color_navy=(97, 218, 252)

#get all the points corrdinate
all_corrdinate=[]
j=0
for  i in range (1,10):
        for j in range (1,11):
                a=[i*75+200, j*75]
                all_corrdinate.append(a)


#define bottom class
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
                        font = pygame.font.SysFont('Cyberbit.ttf', 25)
                        text = font.render(self.text, 1, (0,0,0))
                        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, mouse_position):
                #Pos is the mouse position or a tuple of (x,y) coordinates
                if mouse_position[0] > self.x and mouse_position[0] < self.x + self.width:
                        if mouse_position[1] > self.y and mouse_position[1] < self.y + self.height:
                                return True
                return False

#define buttoms       
NewGameButtom = bottom ( (color_goldenrod), 50, 200, 100, 50, 'New Game')
WithdrawButtom = bottom ( (color_goldenrod), 50, 350, 100, 50, 'Withdraw')
QuitButtom = bottom( (color_goldenrod), 50, 500, 100, 50, 'Quit')
pygame.display.update()

#define rules
class rules():
        def __init__(self, move_color, name_coordinates,user_mouse_pos):
                self.move_color=move_color
                self.name_coordinates=name_coordinates
                self.user_mouse_input=user_mouse_input
        
        #define 
        # move_color=1 black should go; 
        # move_color=0 red should go;
        def rule_move(self, move_color, name_coordinates, user_mouse_pos):
                for i in name_coordinates:
                        if i[1] == user_mouse_pos:
                                name = i[0]
                                x=name_coordinates[i][1][0]
                                y=name_coordinates[i][1][1]

                        #determine who goes first
                        if move_color == 0:

                                #determine role 
                                if name == 'bing_qizi':


                                        """
                                        #cross river?
                                        if y>375:

                                                #pygame.draw.circle(screen, color_blue, [x,y+75], 5)


                                        elif x == 275:
                                                #pygame.draw.circle(screen, color_blue, [x+75, y], 5)
                                                #pygame.draw.circle(screen, color_blue, [x, y+75], 5)

                                        elif x == 875:
                                                #pygame.draw.circle(screen, color_blue, [x-75, y], 5)
                                                #pygame.draw.circle(screen, color_blue, [x, y+75], 5)
                                        
                                        elif y == 75:
                                                #pygame.draw.circle(screen, color_blue, [x+75, y], 5)
                                                #pygame.draw.circle(screen, color_blue, [x-75, y], 5)
                                                
                                        else: 
                                                #pygame.draw.circle(screen, color_blue, [x+75, y], 5)
                                                #pygame.draw.circle(screen, color_blue, [x-75, y], 5)
                                                #pygame.draw.circle(screen, color_blue, [x, y+75], 5)
                                                



                                #if name == pao_qizi:

                                #if name == che_qizi:

                                #if name == xiang_qizi:
                                
                                #if name == shi_qizi:

                                #if name == ma_qizi:

                                #if name == jiang_qizi:
                                                return
        def draw()"""

                                


                        

#draw the cross line
def shizi(a,b):
        l = 12
        d = [5,-5]
        for c in [0,1]:
                if a == 275:
                        c = 0
                elif a == 875:
                        c = 1
                for e in [0,1]:
                        p = [a+d[c],b+d[e]]
                        if e == 0:
                                pygame.draw.line(screen,color_black,(p[0],p[1]),(p[0],p[1]+l))
                        else:
                                pygame.draw.line(screen,color_black,(p[0],p[1]),(p[0],p[1]-l))
                        if c == 0:
                                pygame.draw.line(screen,color_black,(p[0],p[1]),(p[0]+l,p[1]))
                        else:
                                pygame.draw.line(screen,color_black,(p[0],p[1]),(p[0]-l,p[1]))

        return

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
                        if pick == True and ChessButtom.isOver(mouse_position):
                                pick = False

                        elif pick == False :
                                pick = True
                                

                        if NewGameButtom.isOver(mouse_position):
                                print('Newgame')
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
        
        #draw cross lines
        shizi(350,225)
        shizi(800,225)
        shizi(350,600)
        shizi(800,600)
        dd = 275
        while dd >= 275 and dd <= 875:
                shizi(dd,300)
                shizi(dd,525)
                dd += 150
        
        #draw chess board
        #horizontal line
        i=75
        while i <= 750:
               pygame.draw.line(screen, color_black, (275,i), (875,i) )
               i+=75
               
        #vertical line
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
