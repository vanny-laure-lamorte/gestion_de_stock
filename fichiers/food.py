from global_def import Global
from store_management import Store_Management

import mysql.connector

import pygame, sys

class Add_Food(Global):
    def __init__(self): 
            Global.__init__(self)
            self.store_m = Store_Management()
            self.count_info = 0
            self.products = self.store_m.display_product() 

            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VannyLamorte25!",
                database="store"
        )
            self.cursor = self.connection.cursor()
            pygame.init()

    def display_image(self):    
        self.img_back("bakground","images/food/image6.png")    
        self.image("damier1","images/food/image1.png",800,40,0,35) 
       
 
    def display_text(self): 
        self.text_c4(" served until 11:45 PM", self.red, 20, 10)
        self.text_c1(" — My Food List —", self.white, 180,515)

    def rectangle(self):                 
       
        # Rect hauts: nom du produits, prix
        self.rect_full(self.light_grey, 400, 160, 450, 270, 5) # Big rect gris
        self.rect_border(self.grey, 400, 160, 450, 270, 4, 5) # Big border gris

        self.rect_full(self.white, 400, 60, 300, 40, 5) # Name
        self.rect_full(self.white, 400, 140, 415, 60, 5) # Description
        self.rect_full(self.white, 480, 200, 260, 40, 5) # Price
        self.rect_full(self.white, 480, 250, 260, 40, 5) # Quantity
        
        # Rect bas: titre
        self.rect_full(self.brown, 400, 550, 450, 80, 5)
        self.rect_border(self.yellow, 400, 550, 450, 80, 4, 5)      
        self.image("fleche","images/food/image3.png",20,20,560,50) # Flèche droite
        self.image("fleche","images/food/image4.png",20,20,220,50) # Flèche gauche
      
    def button_menu(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)
        else:
            self.rect_radius(5, self.light_grey, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)

    def display_design(self):
        self.screen.fill(self.white)
        self.display_image()
        self.rectangle()
        self.display_text()
        self.display_item()
        self.button_menu()

    def display_item(self): 

        self.products
        # products = self.store_m.display_product() 

        for i, product in enumerate(self.products):

            if self.count_info == i:
                # id = product[0]
                name = product[1]
                description = product[2]
                price = str(product[3])
                quantity = str(product[4])
                # category = product[6]
                
                self.texte(30,name, self.orange, 400, 60)
                self.texte(18,description, self.orange, 400, 135)
                self.texte( 18, price, self.orange, 480, 200)
                self.texte( 18, quantity, self.orange, 480, 250)
                # self.texte( 18, id, self.orange, 400, 60)
                # self.texte( 18, category, self.orange, 400, 60)

                # Légende
                self.texte(20,"Price : ", self.orange, 315, 200)
                self.texte(20,"Quantity : ", self.orange, 310, 250)            
    
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def add_food_run(self): 
         self.run()
         
    def run(self):
        
        food_run = True
        while food_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    food_run = False

                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    # print (self.count_info)
                    if self.is_mouse_over_button(pygame.Rect(20,20,220,50)): 
                        if self.count_info == 0: 
                            self.count_info =  len(self.products)-1                     
                        else:
                            self.count_info = self.count_info - 1
                    elif self.is_mouse_over_button(pygame.Rect(20,20,560,50)):
                        if self.count_info == len(self.products)-1: 
                            self.count_info = 0                            
                        else:
                            self.count_info = self.count_info + 1
                    
                    elif self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        food_run = False

            self.display_design()
          
            pygame.display.flip()
            pygame.display.update()


add_food = Add_Food()
add_food.add_food_run()
    
