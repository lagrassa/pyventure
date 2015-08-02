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
    def __init__(self, data, center):
        self.data = data #:["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
        self.example_data_types = ["dictionary","list","float","int","string","tuple"]
        self.current_example_index = 0
        self.current_example = self.data[0]
        self.radius = 60
        self.center = center
    def draw_bubble(self):
        circleRect = pygame.draw.circle(screen, (10, 60, 30), self.center, self.radius)
    def grow(self,amount_to_grow):
        self.radius = self.radius + amount_to_grow
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
    def is_correct(self, data_data_type_displayer):
        bubble_type = self.example_data_types[self.current_example_index]
        correct_type = data_data_type_displayer.current_data_type
        if bubble_type == correct_type:
            return True
        return False

class Data_Displayer():
    def __init__(self, x, y, data_types):
        pygame.display.set_caption('Data Types')
        pygame.display.update()
        self.data_types = data_types
        self.current_data_type_index = 0
        self.current_data_type = "dictionary"
        self.x = x
        self.y = y
        self.number = 0
    def draw_self(self):
        self.rect = pygame.draw.rect(screen, (25,25,25), (self.x, self.y, screen_width/2.0, screen_height/5.0), 2)
    def addText(self):
        screen.blit(font.render(self.current_data_type, True, (255,0,0)), (self.x+50, self.y +25))
        pygame.display.update()
    def change(self):
        self.current_data_type_index+=1
        self.current_data_type = self.data_types[self.current_data_type_index]
    def number_increase(self):
        pass
    def display_number(self):
        text_to_display = "Score: "+ str(self.number)
        screen.blit(font.render(text_to_display, True, (255,0,0)), (self.x+50, self.y +25))
        pygame.display.update()

# Main method of the program
data = ["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
bubble_center = (100,200) 
correct_bubble = Bubble(data, bubble_center)

data_type_displayer_x =200
data_type_displayer_y =350
data_types= ["dictionary", "list", "float", "int", "string", "tuple"]
data_type_displayer= Data_Displayer(data_type_displayer_x, data_type_displayer_y, data_types)

score_display_x = 300 
score_display_y = 100
score_displayer = Data_Displayer(score_display_x, score_display_y, None) #None is the last parameter because scores don't store data types
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if correct_bubble.is_in_range(position):
                if correct_bubble.is_correct(data_type_displayer):
                    data_type_displayer.change()
                    correct_bubble.change_displayed_data()
                    score_displayer.number_increase()
    
    screen.fill((255,255,255))
    correct_bubble.draw_bubble()
    #Do things related to the data type displayer
    data_type_displayer.draw_self()
    data_type_displayer.addText()
    #Update the bubble
    correct_bubble.addText()
    #Update the score screen
    score_displayer.draw_self()
    score_displayer.display_number()
    pygame.display.update()
    mainClock.tick(40)
