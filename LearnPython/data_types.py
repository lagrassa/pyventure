import pygame
pygame.init()
screen_height = 700
screen_width = 500

font = pygame.font.SysFont('Arial', 25)
small_font = pygame.font.SysFont('Arial',18)
screen = pygame.display.set_mode((screen_height, screen_width), 0, 32)
screen.fill((255,255,255))
mainClock = pygame.time.Clock()
class Bubble():
    def __init__(self, data):
        self.data = data #:["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
        self.example_data_types = ["dictionary","list","float","int","string","tuple"]
        self.current_example_index = 0
        self.current_example = self.data[0]
        self.radius = 60
        self.center = (100,200)
    def draw_bubble(self):
        circleRect = pygame.draw.circle(screen, (10, 60, 30), self.center, self.radius)
    def change_displayed_data(self):
        self.current_example_index +=1
        self.current_example = self.data[self.current_example_index]
    def addText(self):
        #offset the text from the center
        x = self.center[0]-50
        y= self.center[1]-10
        screen.blit(small_font.render(self.current_example, True, (255,0,0)), (x,y))
    def is_in_range(self,(x,y)):
        x_circle= 100
        y_circle= 200
        if ((x-x_circle)**2+(y-y_circle)**2)**0.5 < self.radius:
            return True
        return False
    def is_correct(self, data_displayer):
        bubble_type = self.example_data_types[self.current_example_index]
        correct_type = data_displayer.current_data_type
        if bubble_type == correct_type:
            return True
        return False

class Data_Displayer():
    def __init__(self):
        pygame.display.set_caption('Data Types')
        pygame.display.update()
        self.data_types= ["dictionary", "list", "float", "int", "string", "tuple"]
        self.current_data_type_index = 0
        self.current_data_type = "dictionary"
    def draw_self(self):
        self.rect = pygame.draw.rect(screen, (25,25,25), (200, 350, screen_width/2.0, screen_height/5.0), 2)
    def addText(self):
        screen.blit(font.render(self.current_data_type, True, (255,0,0)), (250, 375))
        pygame.display.update()
    def change(self):
        self.current_data_type_index+=1
        self.current_data_type = self.data_types[self.current_data_type_index]
# Main method of the program
data = ["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
correct_bubble = Bubble(data)
displayer= Data_Displayer()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if correct_bubble.is_in_range(position):
                if correct_bubble.is_correct(displayer):
                    displayer.change()
                    correct_bubble.change_displayed_data()
    
    screen.fill((255,255,255))
    correct_bubble.draw_bubble()
    displayer.draw_self()
    displayer.addText()
    correct_bubble.addText()
    pygame.display.update()
    mainClock.tick(40)
