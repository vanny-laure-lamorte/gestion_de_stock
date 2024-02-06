from global_def import Global
from store_management import Store_Management

import mysql.connector
import pygame

class Modify_Product(Global):
    def __init__(self): 
            Global.__init__(self)
            self.store_m = Store_Management()
            self.count_info = 0
            self.products = self.store_m.display_product() 
            self.price = "" 
            self.quantity = "" 

            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VannyLamorte25!",
                database="store"
        )
            self.cursor = self.connection.cursor()
            pygame.init()        

    def background(self): 
        self.image("background","images/modify/modify4.jpeg",800, 600,0, 0)

    def rectangle(self):                 
       
        # Rect hauts: nom du produits, prix
        self.rect_full(self.light_grey, 400, 300, 450, 400, 5) # Big rect gris
        self.rect_border(self.brown, 400, 300, 450, 400, 4, 5) # Big border gris      

        self.rect_full(self.white, 400, 160, 300, 40, 5) # Name
        self.rect_full(self.white, 400, 240, 415, 60, 5) # Description
        self.rect_full(self.white, 480, 300, 260, 40, 5) # Price
        self.rect_full(self.white, 480, 350, 260, 40, 5) # Quantity
        
        # Rect bas: titre
        self.rect_full(self.brown, 400, 50, 450, 80, 5)
        self.rect_border(self.yellow, 400, 50, 450, 80, 5, 5)
        self.texte(40,"— Modify My Product —", self.white, 400, 50)       
      
    def button_menu(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)
        else:
            self.rect_radius(5, self.light_grey, 720, 10, 70, 25)
            self.text_c4("MENU", self.black, 733, 16)
 
    def button_save(self): 
        save_rect = pygame.Rect(420, 522, 200, 45)
        if self.is_mouse_over_button(save_rect):
            self.rect_full(self.yellow, 520, 540, 200, 45, 5)
            self.rect_border(self.yellow, 520, 540, 200, 45, 3, 5)  
            self.text_c4("SAVE CHANGES", self.black, 470, 535)  
        else:
            self.rect_full(self.light_grey, 520, 540, 200, 45, 5)
            self.rect_border(self.brown, 520, 540, 200, 45, 3, 5)
            self.text_c4("SAVE CHANGES", self.black, 470, 535)

    def display_item(self): 

        self.products        

        for i, product in enumerate(self.products):

            if self.count_info == i:
                # id = product[0]
                name = product[1]
                description = product[2]
                price = str(product[3])
                quantity = str(product[4])
                # category = product[6]
                
                self.texte(30,name, self.orange, 400, 160)
                self.texte(18,description, self.orange, 400, 240)
                self.texte( 18, price, self.orange, 480, 300)
                self.texte( 18, quantity, self.orange, 480, 350)
                # self.texte( 18, id, self.orange, 400, 60)
                # self.texte( 18, category, self.orange, 400, 60)

                # Légende
                self.texte(20,"Price : ", self.orange, 315, 300)
                self.texte(20,"Quantity : ", self.orange, 310, 350)            
    
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def arrow_left(self): 
        arrow_l = pygame.Rect(35,35,100,255)  
        if self.is_mouse_over_button(arrow_l):        
            self.image("arrow logo","images/food/image4.png",40,40,100,250)
        else: 
            self.image("arrow logo","images/food/image4.png",35,35,100,255)

    def arrow_right(self):
        arrow_r = pygame.Rect(670, 250, 35, 35) 
        if self.is_mouse_over_button(arrow_r): 
            self.image("arrow logo","images/food/image3.png",40,40,660,250) 
        else:
            self.image("arrow logo","images/food/image3.png",35,35,660,250)   
    
    def delete_logo(self): 
        bin_rect = pygame.Rect(500, 430, 50, 50)            
        if self.is_mouse_over_button(bin_rect):
            self.image("bin logo", "images/modify/modify1.png", 55, 55, 500, 430)
        else:
            self.image("bin logo", "images/modify/modify1.png", 50, 50, 500, 430)

    def modify_logo(self): 
        modify_rect = pygame.Rect(430, 420, 50, 50)        
        if self.is_mouse_over_button(modify_rect):
            self.image("modify logo", "images/modify/modify2.png", 55, 55, 430, 430)
        else:
            self.image("modify logo", "images/modify/modify2.png", 50, 50, 430, 430)

    def input(self):

        # Price
        self.price_input_rect = pygame.Rect(480, 300, 260, 40)
        pygame.draw.rect(self.screen, self.white, self.price_input_rect)

        # Quantity
        self.quantity_input_rect = pygame.Rect(480, 350, 260, 40)
        pygame.draw.rect(self.screen, self.white, self.quantity_input_rect)      

    def display_design(self):
        self.screen.fill(self.light_brown)
        self.background()        
        self.rectangle()
        self.display_item()
        self.button_menu()
        self.arrow_left()
        self.arrow_right()
        self.delete_logo()
        self.modify_logo() 
        self.button_save()

    def modify_product_run(self): 
        self.modify_product_running = True
        self.run()
         
    def run(self):
        
        while self.modify_product_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.modify_product_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.is_mouse_over_button(pygame.Rect(670, 250, 35, 35)): 
                        if self.count_info == 0: 
                            self.count_info =  len(self.products)-1                     
                        else:
                            self.count_info = self.count_info - 1
                    elif self.is_mouse_over_button(pygame.Rect(35,35,100,255)):
                        if self.count_info == len(self.products)-1: 
                            self.count_info = 0                            
                        else:
                            self.count_info = self.count_info + 1    

                    # elif self.button_save(event.pos): 
                    #     if self.price != "" and self.quantity != "": 
                    #         self.store_m.modify_product(self.name, self.description, self.price, self.quantity, self.id_category)

                    # Supprimer un produit
                    elif self.is_mouse_over_button(pygame.Rect(500, 430, 50, 50)):
                        # self.product_id = self.count_info
                        self.store_m.delete_product(self.products[self.count_info][0])
                        # Mettre a jour la nouvelle liste
                        # self.products = self.store_m.delete_product()

                    # Retour au Menu
                    elif self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        self.modify_product_running = False

                    # elif self.price_input_rect.collidepoint(event.pos):
                    #     new_price = input("Enter the new price: ")
                    #     self.products[self.count_info][3] = float(new_price)

                    # elif self.quantity_input_rect.collidepoint(event.pos):  
                    #     new_quantity = input("Enter the new quantity: ")
                    #     self.products[self.count_info][4] = int(new_quantity)
                  
            self.display_design()       

            pygame.display.flip()
            pygame.display.update()

modify_product = Modify_Product()
modify_product.modify_product_run()
    
