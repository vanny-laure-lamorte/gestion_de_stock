from files.global_def import Global
from files.store_management import Store_Management

import mysql.connector
import pygame, sys

class Food(Global):
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

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def DisplayImage(self):    
        self.img_back("bakground","img/food/image6.png")    
        self.image("damier1","img/food/image1.png",800,40,0,35)
        
    def DisplayText(self): 
        self.texte(16," served until 11:45 PM", self.red, 80, 25)
        self.text_c2(" — My Food List —", self.white, 180,515)

    def rectangle(self):                 
       
        self.rect_full(self.light_grey, 400, 160, 450, 270, 5) # Big rect light grey
        self.rect_border(self.grey, 400, 160, 450, 270, 4, 5) # Big border dark grey

        self.rect_full(self.white, 400, 60, 300, 40, 5) # Rect Name
        self.rect_full(self.white, 400, 140, 415, 60, 5) # Rect Description
        self.rect_full(self.white, 480, 200, 260, 40, 5) # Rect Price
        self.rect_full(self.white, 480, 250, 260, 40, 5) # Rect Quantity
        
        self.rect_full(self.brown, 400, 550, 450, 80, 5) # Rect title
        self.rect_border(self.yellow, 400, 550, 450, 80, 4, 5) # Border Rect title     

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def ArrowLeft(self): 
        arrow_l = pygame.Rect(20,20,220,50)  
        if self.is_mouse_over_button(arrow_l):        
            self.image("arrow logo","img/food/image4.png",25,25,220,50)
        else: 
            self.image("arrow logo","img/food/image4.png",20,20,220,50)

    def ArrowRight(self):
        arrow_r = pygame.Rect(560, 50, 20, 20) 
        if self.is_mouse_over_button(arrow_r): 
            self.image("arrow logo","img/food/image3.png",25,25,560,50) 
        else:
            self.image("arrow logo","img/food/image3.png",20,20,560,50)  
      
    def ButtonMenu(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)
        else:
            self.rect_radius(5, self.light_grey, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)

    def DisplayAll(self):
        self.screen.fill(self.white)
        self.DisplayImage()
        self.rectangle()
        self.DisplayText()
        self.DisplayItem()
        self.ArrowRight()
        self.ArrowLeft()
        self.ButtonMenu()

    def DisplayItem(self): 
        self.products       
        for i, product in enumerate(self.products):
            if self.count_info == i:        
                name = product[1]
                description = product[2]
                price = str(product[3])
                quantity = str(product[4])
                # category = str(product[6])
                
                self.texte(30,name, self.orange, 400, 60)
                self.texte(18,description, self.orange, 400, 135)
                self.texte( 18, price, self.orange, 480, 200)
                self.texte( 18, quantity, self.orange, 480, 250)
                # self.texte(18, category, self.orange, 400, 60)

                # Légende
                self.texte(20,"Price : ", self.orange, 315, 200)
                self.texte(20,"Quantity : ", self.orange, 310, 250)            
    
    def food_run(self): 
        self.food_running = True
        self.run()
         
    def run(self):
        
        while self.food_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN: 
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
                        self.food_running = False

            self.DisplayAll()
          
            pygame.display.flip()
            pygame.display.update()
