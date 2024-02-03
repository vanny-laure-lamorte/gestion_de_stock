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
            
            self.connection = mysql.connector(
            host="localhost",
            user="root",
            password="VannyLamorte25!",
            database="store"
        )
            self.cursor = self.connection.cursor()
           

    pygame.init()

    def food_run(self): 
         self.run() 

    def input(self):  
        self.input_name = self.rect_border(self.yellow, 250, 180, 280, 60, 5, 5)
        self.input_description = self.rect_border(self.yellow, 250, 260, 280, 60, 5, 5)
        self.input_price = self.rect_border(self.yellow, 250, 340, 280, 60, 5, 5)
        self.input_quantity = self.rect_border(self.yellow, 250, 420, 280, 60, 5, 5)
        self.input_id_category= self.rect_border(self.yellow, 250, 500,280, 60, 5, 5)

        self.input_name_v = self.rect_border(self.green, 420, 180, 60, 60, 5, 5)
        self.input_description_v = self.rect_border(self.green, 420, 260, 60, 60, 5, 5)
        self.input_price_v = self.rect_border(self.green, 420, 340, 60, 60, 5, 5)
        self.input_quantity_v= self.rect_border(self.green, 420, 420, 60, 60, 5, 5)
        self.input_id_category_v= self.rect_border(self.green, 420, 500,60, 60, 5, 5)

    def text(self): 
        self.texte(12, self.name, self.black, 350, 180)
        self.texte(12, self.description, self.black, 400, 340)

            #def
    # def texte(self, texte_size, texte_content, color, x, y):
    #     pygame.font.init()   # modifier police
    #     Texte = pygame.font.Font("AirstreamNF.ttf", texte_size).render(texte_content, True, color)
    #     Texte_rect = Texte.get_rect(center=(x, y))
    #     self.screen.blit(Texte, Texte_rect)

    def rectangle(self):
        self.check = self.rect_border(self.orange, 400, 40,700, 60, 5, 5)

    def display_design(self):
        self.screen.fill(self.white)           
        self.input()
        self.rectangle()
        self.text()
       
    def run(self):

        en_cours = True
        while en_cours:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    en_cours = False

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
                        if self.name != "" and self.description != "" and self.price != "" and self.quantity != "" and                        self.id_category != "" :                  
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
                            price = price + event.unicode
                    elif self.entry == 4:
                        if event.unicode.isdigit():
                            quantity = quantity + event.unicode    

            self.display_design()                         
            pygame.display.flip()
            pygame.display.update()
  
food = Food()
food.food_run()
    
