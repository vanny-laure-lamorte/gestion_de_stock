from fichiers.global_def import Global
from fichiers.food import Food
from fichiers.add_food import Add_Food
from fichiers.modify_product import Modify_Product
from fichiers.store_management import Store_Management

import pygame, sys

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)
        self.food = Food()
        self.add_food = Add_Food()
        self.modify_product = Modify_Product()
        self.store_management = Store_Management()

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos) 
    
    def options(self): 

        button_food = pygame.Rect(530, 195, 235, 60) # My food
        button_add = pygame.Rect(533, 270, 205, 60) # Add New Product
        button_modify = pygame.Rect(533, 345, 235, 60) # Edit Product Details
        button_quit = pygame.Rect(533, 420, 235, 60) # Quit

        # My Food
        if self.is_mouse_over_button(button_food):
            self.rect_full(self.white, 650, 225, 240, 65, 5)            
            self.image("étoile",r"images/menu/image1.png",20,20,760,185)
            self.text_c1("My Food", self.brown, 600, 210)
        else:
          
            self.rect_full(self.white, 650, 225, 235, 60, 5) 
            self.text_c1("My Food", self.brown, 600, 210)            

        # Add New Product
        if self.is_mouse_over_button(button_add):
            self.rect_full(self.white, 650, 300, 240, 65, 5)            
            self.text_c1("Add New Product", self.brown, 555, 285)
            self.image("étoile",r"images/menu/image1.png",20,20,760,260)
        else:
            self.rect_full(self.white, 650, 300, 235, 60, 5) 
            self.text_c1("Add New Product", self.brown, 555, 285)

        # Edit Product Details
        if self.is_mouse_over_button(button_modify):
            self.rect_full(self.white, 650, 375, 240, 65, 5)            
            self.text_c1("Edit Product Details", self.brown, 540, 360)
            self.image("étoile",r"images/menu/image1.png",20,20,760,335)
        else:
            self.rect_full(self.white, 650, 375, 235, 60, 5) 
            self.text_c1("Edit Product Details", self.brown, 540, 360)
        
        # Quit
        if self.is_mouse_over_button(button_quit):
            self.rect_full(self.white, 650, 450, 240, 65, 5)            
            self.text_c1("Quit", self.brown, 635, 435)
            self.image("étoile",r"images/menu/image1.png",20,20,760,410)
        else:
            self.rect_full(self.white, 650, 450, 235, 60, 5) 
            self.text_c1("Quit", self.brown, 635, 435)
       
 
    def display(self): 
        self.options()        

    # Afficher choix du menu
    def menu_run(self): 
        self.running = True
        img_back = pygame.image.load(r"images/menu/image2.jpg").convert()

        while self.running:
            self.screen.blit(img_back, (0, 0))                               

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Liens vers autres pages
                elif event.type == pygame.MOUSEBUTTONDOWN:                  
                        
                    if self.is_mouse_over_button(pygame.Rect( 530, 195, 235, 60)):
                        self.food.food_run()                     
                    elif self.is_mouse_over_button(pygame.Rect( 533, 270, 205, 60)): 
                        self.add_food.add_food_run() 
                  
                    elif self.is_mouse_over_button(pygame.Rect(533, 345, 235, 60)):                     
                        self.modify_product.modify_product_run()  
  
                    elif self.is_mouse_over_button(pygame.Rect(533, 420, 235, 60)):
                        pygame.quit()
                        sys.exit()  

            self.display()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

menu = Menu()
menu.menu_run()

