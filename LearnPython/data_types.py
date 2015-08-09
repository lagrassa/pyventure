
#James Gu: 
#    Bubble movement allowing bubble to be clicked while moving
#    Fixed screen height and width bug
#    Implemented bubble bouncing perpendicularly off wall in the x direction
#Rohan Sharma
#    Made another bubble that displayed incorrect data types
#George Jiang
#    Added cooler font
#    Made the score increase by 1 upon clicking the correct bubble
#    Added diagonal movement
#Rachel Zhang
#    Made bubble shrink when the screen was clicked
#Trisha Ballakur
#    Fixed bug where window doesn't close upon clicking "x"
#    Defined colors for bubbles
#Rohit Chopra
#    Made one bubble grow while the other one shrinks

import pygame

pygame.init()
screen_height = 700
screen_width = 500

font = pygame.font.SysFont('Ubuntu', 25)
small_font = pygame.font.SysFont('Ubuntu',18)
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
screen.fill((255,255,255))
mainClock = pygame.time.Clock()
################Bubble class, contains data##############
#Contributions

class Bubble():
    def __init__(self, is_correct, data, center, color):
        self.data = data #:["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
        self.example_data_types = ["dictionary","list","float","int","string","tuple"]
        self.current_example_index = 0
        self.current_example = self.data[0]
        self.radius = 60
        self.center = center
        self.is_correct = is_correct
        self.color = color
    def draw_bubble(self):
        circleRect = pygame.draw.circle(screen, self.color, self.center, self.radius)
    def grow(self,amount_to_grow):
        self.radius = self.radius + amount_to_grow
    def change_displayed_data(self):
        self.current_example_index +=1
        if is_correct:
            self.current_example = correct_data[self.current_example_index]
        else:
            self.current_example = self.data[self.current_example_index]
    def addText(self):
        #offset the text from the center
        x = self.center[0]-50
        y= self.center[1]-10
        screen.blit(small_font.render(self.current_example, True, (255,0,0)), (x,y))
    def is_in_range(self,(x,y)):
        x_circle= self.center[0]
        y_circle= self.center[1]
        if ((x-x_circle)**2+(y-y_circle)**2)**0.5 < self.radius:
            return True
        return False
    def is_correct(self, data_data_type_displayer):
        return self.is_correct

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
        self.rect = pygame.draw.rect(screen, (25,25,25), (self.x, self.y, screen_width/3.0, screen_height/9.0), 2)
    def addText(self):
        screen.blit(font.render(self.current_data_type, True, (255,0,0)), (self.x+50, self.y +25))
        pygame.display.update()
    def change(self):
        self.current_data_type_index+=1
        self.current_data_type = self.data_types[self.current_data_type_index]
    def number_increase(self):
        self.number += 1
    def display_number(self):
        text_to_display = "Score: "+ str(self.number)
        screen.blit(font.render(text_to_display, True, (255,0,0)), (self.x+50, self.y +25))
        pygame.display.update()

# Main method of the program
correct_data = ["{'a':5, 'b':6}","[Jess, Alex]","3.0/2","3/2","'Hello'", "(1,5)"]
wrong_data = ["[sponge, bob]","2/3","4/5","'goodbye'", "(2,7)", "{a:3}"]
green = (10, 60, 30)
blue = (0,0,205) 
wrong_bubble_center = (230, 80)
bubble_center = (100,200) 
correct_bubble = Bubble(True, wrong_data,bubble_center, green)
wrong_bubble = Bubble(False, wrong_data, wrong_bubble_center, blue)
bubble_list = [correct_bubble, wrong_bubble]
movementAmount = 5
data_type_displayer_x =200
data_type_displayer_y =600
data_types= ["dictionary", "list", "float", "int", "string", "tuple"]
data_type_displayer= Data_Displayer(data_type_displayer_x, data_type_displayer_y, data_types)

score_display_x = (2/3.0)*screen_width 
score_display_y = 0
score_displayer = Data_Displayer(score_display_x, score_display_y, None) #None is the last parameter because scores don't store data types
################### Main Game Loop ########################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if correct_bubble.radius > 50 and wrong_bubble.radius < 100:
                correct_bubble.radius += -5
                wrong_bubble.radius += 5
            position = pygame.mouse.get_pos()
            for bubble in bubble_list:
                if bubble.is_in_range(position):
                    if bubble.is_correct:
                        #switch which bubble is correct
                        randomBubble = (0,len(bubble_list)-1)
                        randomBubble.is_correct = True
                        data_type_displayer.change()
                        correct_bubble.change_displayed_data()
                        wrong_bubble.change_displayed_data()
                        score_displayer.number_increase()
                
    if (correct_bubble.center[0] > screen_width-correct_bubble.radius) or (correct_bubble.center[0] < correct_bubble.radius):
        movementAmount = -movementAmount
    correct_bubble.center = ((correct_bubble.center[0] + movementAmount), correct_bubble.center[1] + movementAmount) 
    screen.fill((255,255,255))
    correct_bubble.draw_bubble()
    wrong_bubble.draw_bubble()
    #Do things related to the data type displayer
    data_type_displayer.draw_self()
    data_type_displayer.addText()
    #Update the bubble
    correct_bubble.addText()
    wrong_bubble.addText()
    #Update the score screen
    score_displayer.draw_self()
    score_displayer.display_number()
    pygame.display.update()
    mainClock.tick(40)
