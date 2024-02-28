import pygame
import random 
pygame.init()
# hit = pygame.mixer.Sound('boom.mp3')
class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250),random.randrange(100, 250),random.randrange(100, 250))
        self.isdead = False
    def draw(self):
        if not self.isdead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50)) #end of class brick
    def collide(self, ball_x, ball_y):
            if not self.isdead:
#                 pygame.mixer.Sound.play(hit)
                if (ball_x + 20 > self.xpos and
                    ball_x < self.xpos + 100 and
                    ball_y + 20 > self.ypos and
                    ball_y < self.ypos + 50):
                    self.isdead = True
                    return True
            return False
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("worlds easyest breakout")

doExit = False


clock = pygame.time.Clock()

p1x = 400

p1y = 400


bx = 350
by = 250
bVx = 5 
bVy = 5

bx += bVx
by += bVy

b1 = brick(50, 50)
b2 = brick(190, 50)
b3 = brick(323, 50)
b4 = brick(449, 50)
b5 = brick(569, 50)
b6 = brick(50, 140)
b7 = brick(190, 140)
b8 = brick(323, 140)
b9 = brick(449, 140)
b10= brick(569, 140)

music = pygame.mixer.music.load('Giant Socks Record.mp3')
pygame.mixer.music.set_volume(0.85)
pygame.mixer.music.play(-1)
while not doExit: #game loop 
    
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              doExit = True
            
    #game logic will go here------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1x-=5
    if keys[pygame.K_d]:
        p1x+=5
        
    if keys[pygame.K_l]:
        p2y+=5
    if keys[pygame.K_o]:
        p2y-=5
    bx += bVx
    by += bVy
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
    if by < 0 or by + 20 > 500:
        bVy *= -1    
    if bx < p1x + 100 and bx > p1x and by + 20 > p1y and by < p1y + 20: 
        bVy *= -1
        
    
    #y = 2(x + 2)
            
            
            
    if b1.collide(bx, by):
        bVy *= -1
    if b2.collide(bx, by):
        bVy *= -1
    if b3.collide(bx, by):
        bVy *= -1
    if b4.collide(bx, by):
        bVy *= -1
    if b5.collide(bx, by):
        bVy *= -1  
    if b6.collide(bx, by):
        bVy *= -1
    if b7.collide(bx, by):
        bVy *= -1
    if b8.collide(bx, by):
        bVy *= -1
    if b9.collide(bx, by):
        bVy *= -1
    if b10.collide(bx, by):
        bVy *= -1

    #render section will go here----------------------------       
    screen.fill((0,0,0))
     
     
    
    
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 100, 20), 10)
    
   
    
    pygame.draw.circle(screen, (155, 255, 255), (bx, by), 10)
    
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    

    

     
    pygame.display.flip()
            
            
            
#end game loop-------------------------------------

pygame.quit()

