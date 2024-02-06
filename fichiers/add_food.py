from fichiers.global_def import Global
from fichiers.store_management import Store_Management
import pygame
import mysql.connector

class Add_Food(Global):
    def __init__(self): 
            Global.__init__(self)
            self.sm = Store_Management()
            self.name = ""
            self.description = ""
            self.price = "" 
            self.quantity = "" 
            self.id_category = "" 
                       
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VannyLamorte25!",
                database="store"
        )
            self.cursor = self.connection.cursor()
            pygame.init()

    def background(self):
            self.image("food_pic","images/add/add2.png",400, 800, 400, 90)
            self.image("food_pic","images/add/add3.png",110, 110, 20, 7)

    def display_title(self):
        self.rect_full(self.brown, 400, 50, 450, 80, 5)
        self.rect_border(self.yellow, 400, 50, 450, 80, 5, 5)
        self.texte(40,"— Add A New Product —", self.white, 400, 50) 
        

    def button_menu(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)
        else:
            self.rect_radius(5, self.light_grey, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)  


    def add_food_run(self): 
        self.add_food_running = True
        self.run() 

    def input(self):  

        # Section Titre
        self.rect_full(self.brown, 250, 320, 450, 425, 5) 
        self.rect_border(self.yellow, 250, 320, 450, 425, 2, 5) 

        # Section input
        # Name
        self.rect_full(self.white, 250, 160, 280, 60, 5)
        self.input_name = self.rect_border(self.grey, 250, 160, 280, 60, 2, 5)
        self.texte(20, self.name, self.black, 250, 160)
        self.texte(20, "Name : ", self.white, 70, 160) 

        self.rect_full(self.white, 425, 160, 60, 60, 5)
        self.input_name_v = self.rect_border(self.grey,
        425, 160, 60, 60, 2, 5)

        # Price
        self.rect_full(self.white, 250, 240, 280, 60, 5)
        self.input_price = self.rect_border(self.grey, 250, 240, 280, 60, 2, 5)
        self.texte(20, self.price, self.black, 250, 240) 
        self.texte(20, "Price :", self.white, 70, 240) 

        self.rect_full(self.white, 425, 240, 60, 60, 5) 
        self.input_price_v = self.rect_border(self.grey, 425, 240, 60, 60, 2, 5)
    
        # Quantity
        self.rect_full(self.white, 250, 320, 280, 60, 5)
        self.input_quantity = self.rect_border(self.grey, 250, 320, 280, 60, 2, 5)
        self.texte(20, self.quantity, self.black, 250, 320)
        self.texte(20, "Quantity :", self.white, 70, 320) 

        self.rect_full(self.white, 425, 320, 60, 60, 5) 
        self.input_quantity_v= self.rect_border(self.grey, 425, 320, 60, 60, 2, 5)

             #Description
        self.rect_full(self.white, 265, 400,240, 60, 5)
        self.input_description = self.rect_border(self.grey, 265, 400, 240, 60, 2, 5)
        self.texte(20, self.description, self.black, 265, 400)
        self.texte(20, "Description :", self.white, 85, 400) 

        self.rect_full(self.white, 425, 400, 60, 60, 5) 
        self.input_description_v = self.rect_border(self.grey, 425, 400, 60, 60, 2, 5)   

        # Catégory
        self.rect_full(self.white, 360, 480, 60, 60, 5)
        self.input_id_category= self.rect_border(self.grey, 360, 480, 60, 60, 2, 5)
        self.texte(20, self.id_category, self.black, 360, 480)  
        self.texte(20,"Category :", self.white, 70, 460)
        self.texte(20, "Enter   1 for meat", self.white, 190, 460)
        self.texte(20, "2 for vegetarian", self.white, 240, 480)
        self.texte(20, "3 for a side", self.white, 225, 500)

        self.rect_full(self.white, 425, 480, 60, 60, 5) 
        self.input_id_category_v= self.rect_border(self.grey, 425, 480,60, 60, 2, 5)  

    def check_button(self):
        check_rect = pygame.Rect(330, 550, 150, 40)
        if self.is_mouse_over_button(check_rect):
            self.rect_radius(5, self.yellow,  320, 545, 155, 45)
            self.text_c4("ADD TO THE LIST", self.black,337, 560)
        else:
            self.rect_radius(5, self.yellow, 320, 545, 150, 40)
            self.text_c4("ADD TO THE LIST", self.black,337, 560)      
       
    def message_box(self):            
            self.text_c5("Added to the list", self.green, 70, 560)
            self.image("Add_logo","images/add/add1.png",25,25, 280,553)  
            pygame.display.flip()
            pygame.time.delay(2000)

    def display_design(self):
        self.screen.fill(self.light_brown)   
        self.background()   
        self.input()       
        self.display_title()
        self.button_menu() 
        self.check_button()  
       
    def run(self):

        while self.add_food_running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.add_food_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_name.collidepoint(event.pos): 
                        self.entry = 1
                    elif self.input_description.collidepoint(event.pos): 
                        self.entry = 2
                    elif self.input_price.collidepoint(event.pos):  
                        self.entry = 3
                    elif self.input_quantity.collidepoint(event.pos): 
                        self.entry = 4
                    elif self.input_id_category.collidepoint(event.pos):                   
                        self.entry = 5
                   
                    elif self.is_mouse_over_button(pygame.Rect(330, 550, 150, 40)):
                        if self.name != "" and self.description != "" and self.price != "" and self.quantity != "" and self.id_category != "" and int(self.id_category) in (1, 2,3):                  
                            self.sm.add_product(self.name, self.description, float(self.price), int(self.quantity), int(self.id_category)) 
                            self.message_box()                                                
            
                    elif self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        self.add_food_running = False

                elif event.type == pygame.KEYDOWN:                    
                    if self.entry == 1:
                        if event.unicode.isalpha():
                            self.name = self.name + event.unicode
                            self.name = self.name.capitalize() 
                        elif event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                    elif self.entry == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.description = self.description[:-1]
                        elif event.unicode:
                            self.description = self.description + event.unicode
                            self.description = self.description.capitalize()
                    elif self.entry == 3:
                        if event.unicode.isdigit():
                            self.price = self.price + event.unicode
                        elif event.key == pygame.K_BACKSPACE:
                            self.price = self.price[:-1]
                    elif self.entry == 4:
                        if event.unicode.isdigit():
                            self.quantity = self.quantity + event.unicode 
                        elif event.key == pygame.K_BACKSPACE:
                            self.quantity = self.quantity[:-1]                            
                    elif self.entry == 5:
                        if event.unicode.isdigit():
                            self.id_category= self.id_category + event.unicode 
                        elif event.key == pygame.K_BACKSPACE:
                            self.id_category = self.id_category[:-1]                        
            
            self.display_design()                         
            pygame.display.flip()
            pygame.display.update()
  
# add_food = Add_Food()
# add_food.add_food_run()
    
