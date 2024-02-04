from global_def import Global
from store_management import Store_Management
import pygame
import mysql.connector

class Food(Global):
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

    def display_title(self):
        self.rect_full(self.brown, 400, 50, 450, 80, 5)
        self.rect_border(self.yellow, 400, 50, 450, 80, 5, 5)
        self.texte(40," — Add A New Product —", self.white, 400, 50) 

    def add_food_run(self): 
         self.run() 

    def input(self):  

        # Section Titre

        # Rect gris
        self.rect_full(self.light_grey, 250, 340, 450, 425, 5) 
        self.rect_border(self.grey, 250, 340, 450, 425, 4, 5) 

        # Section input
        # Name
        self.rect_full(self.white, 250, 180, 280, 60, 5)
        self.input_name = self.rect_border(self.grey, 250, 180, 280, 60, 2, 5)
        self.texte(20, self.name, self.black, 250, 180)
        self.texte(20, "Name : ", self.orange, 70, 180) 

        self.rect_full(self.white, 425, 180, 60, 60, 5)
        self.input_name_v = self.rect_border(self.grey,
        425, 180, 60, 60, 2, 5)

        # Price
        self.rect_full(self.white, 250, 260, 280, 60, 5)
        self.input_price = self.rect_border(self.grey, 250, 260, 280, 60, 2, 5)
        self.texte(20, self.price, self.black, 250, 260) 
        self.texte(20, "Price :", self.orange, 70, 260) 

        self.rect_full(self.white, 425, 260, 60, 60, 5) 
        self.input_price_v = self.rect_border(self.grey, 425, 260, 60, 60, 2, 5)
    
        # Quantity
        self.rect_full(self.white, 250, 340, 280, 60, 5)
        self.input_quantity = self.rect_border(self.grey, 250, 340, 280, 60, 2, 5)
        self.texte(20, self.quantity, self.black, 250, 340)
        self.texte(20, "Quantity:", self.orange, 70, 340) 

        self.rect_full(self.white, 425, 340, 60, 60, 5) 
        self.input_quantity_v= self.rect_border(self.grey, 425, 340, 60, 60, 2, 5)

        # Catégory
        self.rect_full(self.white, 250, 420, 280, 60, 5)
        self.input_id_category= self.rect_border(self.grey, 250, 420, 280, 60, 2, 5)
        self.texte(20, self.id_category, self.black, 250, 420)  
        self.texte(20,"Category:", self.orange, 70, 420) 

        self.rect_full(self.white, 425, 420,60, 60, 5) 
        self.input_id_category_v= self.rect_border(self.grey, 425, 420,60, 60, 2, 5) 

        #Description
        self.rect_full(self.white, 265, 500,250, 80, 5)
        self.input_description = self.rect_border(self.grey, 265, 500,250, 80, 2, 5)
        self.texte(20, self.description, self.black, 265, 500)
        self.texte(20, "Description :", self.orange, 85, 500) 
        
        self.rect_full(self.white, 425, 500, 60, 60, 5) 
        self.input_description_v = self.rect_border(self.grey, 425, 500, 60, 60, 2, 5)      

    def display_design(self):
        self.screen.fill(self.white) 
     
        self.input()
       
        self.display_title ()
       
    def run(self):

        add_food_run = True
        while add_food_run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    add_food_run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.name, self.description)
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
                    
                    elif self.check.collidepoint(event.pos):    
                        if self.name != "" and self.description != "" and self.price != "" and self.quantity != "" and                      self.id_category != "" :                  
                            self.sm.add_product(self.name, self.description, self.price, self.quantity, self.id_category)

                elif event.type == pygame.KEYDOWN:                    
                    if self.entry == 1:
                        if event.unicode.isalpha():
                            self.name = self.name + event.unicode
                            self.name = self.name.capitalize()                     
                    elif self.entry == 2:
                        if event.unicode.isalpha():
                            self.description = self.description + event.unicode
                            self.description = self.description.capitalize()
                    elif self.entry == 3:
                        if event.unicode.isdigit():
                            self.price = self.price + event.unicode
                    elif self.entry == 4:
                        if event.unicode.isdigit():
                            self.quantity = self.quantity + event.unicode    

            self.display_design()                         
            pygame.display.flip()
            pygame.display.update()
  
food = Food()
food.add_food_run()
    
