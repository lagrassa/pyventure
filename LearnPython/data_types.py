import pygame
pygame.init()
screen = pygame.display.set_mode((600, 500), 0, 32)
mainClock = pygame.time.Clock()
class Bubble():
    def draw_bubble(self):
        circleRect = pygame.draw.circle(screen, (255, 255, 255), (100, 200), 40)

class Data_Displayer():
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        pygame.display.update()
    def draw_self(self):
        self.rect = pygame.draw.rect(screen, (50,50,50), (175, 75, 200, 100), 2)
    def addText(self):
        screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        pygame.display.update()
b = Bubble()
d= Data_Displayer()
while True:
    b.draw_bubble()
    d.draw_self()
    d.addText()
    pygame.display.update()
    mainClock.tick(40)
