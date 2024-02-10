# from fichiers.global_def import Global
# from fichiers.store_management import Store_Management

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
            self.price_modified = "Click here to add a new price"
            self.quantity_modified = "Click here to add a new quantity"

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
       
        # Display product info window
        self.rect_full(self.light_grey, 400, 300, 450, 400, 5) # Big rect gris
        self.rect_border(self.brown, 400, 300, 450, 400, 4, 5) # Big border gris    
        self.rect_full(self.white, 400, 160, 300, 40, 5) # White Rect Name
        self.rect_full(self.white, 400, 240, 415, 60, 5) # White Rect Description
        self.rect_full(self.white, 480, 300, 260, 30, 5) # White Rect Price 
        self.rect_full(self.white, 480, 370, 260, 30, 5) # White Rect Quantity
        self.price_input_rect = self.rect_full(self.white, 480, 335, 260, 30, 5) # White Rect Price Modified
        self.quantity_input_rect = self.rect_full(self.white, 480, 405, 260, 30, 5) # White Rect Quantity Modified   
        
        # Display text
        self.texte(20,"Actual Price : ", self.orange, 260, 300)
        self.texte(20,"New Price : ", self.orange, 260, 335)
        self.texte(20,"Actual Quantity : ", self.orange, 260, 370)  
        self.texte(20,"New Quantity : ", self.orange, 260, 405) 

        # Display title
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
                name = product[1]
                description = product[2]
                price = str(product[3])
                quantity = str(product[4])
                
                self.texte(30, name, self.orange, 400, 160) # Display name text
                self.texte(18, description, self.orange, 400, 240) # Display description text
                self.texte( 18, price, self.orange, 480, 300) # Display price text
                self.texte( 18, quantity, self.orange, 480, 370) # Display quantity text

                self.texte( 18,self.price_modified, self.orange, 480, 335) # Display price modified text
                self.texte( 18, self.quantity_modified, self.orange, 480, 405) # Display quantity modified text

    
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def ArrowLeft(self): 
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
        self.bin_rect = pygame.Rect(550, 450, 30, 30)            
        if self.is_mouse_over_button(self.bin_rect):
            self.image("bin logo", "images/modify/modify1.png", 35, 35, 550, 450)
        else:
            self.image("bin logo", "images/modify/modify1.png", 30, 30, 550, 450)

    def input(self):

        # Price
        self.price_input_rect = pygame.Rect(480, 300, 260, 40)
        pygame.draw.rect(self.screen, self.white, self.price_input_rect)
        self.texte(18, self.price_modified, self.orange, 440, 300)

        # Quantity
        self.quantity_input_rect = pygame.Rect(480, 350, 260, 40)
        pygame.draw.rect(self.screen, self.white, self.quantity_input_rect)   
        self.texte(18, self.quantity_modified, self.orange, 540, 300)

    def ConfirmationModify(self): 
        self.texte(22,"Price and quantity modified", self.green, 340, 460) 
        self.image("Add_logo","images/add/add1.png",20,20, 460,450)  
        pygame.display.flip()
        pygame.time.delay(2000)

    def ConfirmationDelete(self): 
        self.texte(22,"Product removed from list", self.green, 340, 460)    
        self.image("Add_logo","images/add/add1.png",20,20, 450,450)  
        pygame.display.flip()
        pygame.time.delay(2000)

    def DisplayAll(self):
        self.background()        
        self.rectangle()
        self.display_item()
        self.button_menu()
        self.ArrowLeft()
        self.arrow_right()
        self.delete_logo()
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

                    elif self.price_input_rect.collidepoint(event.pos):
                        self.price_modified =""
                        self.entry = 6

                    elif self.quantity_input_rect.collidepoint(event.pos):
                        self.quantity_modified = ""
                        self.entry = 7   

                    # Delete a product
                    elif self.is_mouse_over_button(self.bin_rect):
                        self.store_m.delete_product(self.products[self.count_info][0])
                        self.products = self.store_m.display_product()
                        if self.count_info >= len(self.products):
                            self.count_info = 0
                        self.ConfirmationDelete()                          

                    # Edit price and quantity 
                    elif self.is_mouse_over_button(pygame.Rect(420, 522, 200, 45)):
                        if self.price_modified != "" or self.quantity_modified != "":
                            new_product = {}
                            if self.price_modified != "":
                                new_product['price'] = int(self.price_modified)
                            elif self.quantity_modified != "":
                                new_product['quantity'] = int(self.quantity_modified)

                            self.store_m.modify_product(self.products[self.count_info][0], new_product)  
                            self.ConfirmationModify()  
                            
                       

                    # Link back to the menu
                    elif self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        self.modify_product_running = False   

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry == 6: 
                            self.price_modified = self.price_modified[:-1]
                        elif self.entry == 7: 
                            self.quantity_modified= self.quantity_modified[:-1] 

                    else:
                        if self.entry == 6:
                            if event.unicode.isdigit():
                                self.price_modified = self.price_modified + event.unicode             
                    
                        elif self.entry == 7:
                            if event.unicode.isdigit():
                                self.quantity_modified = self.quantity_modified + event.unicode       
                  
            self.DisplayAll()       

            pygame.display.flip()
            pygame.display.update()

test = Modify_Product()
test.modify_product_run()
