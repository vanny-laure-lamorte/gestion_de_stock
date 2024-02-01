from global_def import Global
from store_management import Store_Management

import mysql.connector
import pygame

class Add_Food(Global):
    def __init__(self): 
            Global.__init__(self)
            self.store_management = Store_Management()
   
    pygame.init()

    def display_image(self):    
        self.img_back("bakground","images/food/image6.png")    
        self.image("damier1","images/food/image1.png",800,40,0,35)  
 
    def display_text(self): 
        self.text_c4(" served until 11:45 PM", self.red, 20, 10)
        self.text_c1(" — My Food List —", self.white, 180,515)

    def rectangle(self): 
        self.rect_full(self.brown, 400, 550, 450, 80, 5)
        self.rect_border(self.yellow, 400, 550, 450, 80, 4, 5)

     
    # def display_product(self):
        
    #     list_produit = self.store_management.display_product_in_category()

    #     for i in range (len(list_produit)): 
    #         product = list_produit[i]
    #         if i < len(list_produit) >=3:
    #             name= product[1]  
    #             description = product[2]
    #             price = product[3]
    #         self.text_c2(f"{name}\n", self.red, 40, 140 + i * 50)
    #         self.text_c3(f"{description}, {price} US$\n", self.black, 10, 170 + i * 50)
    #         self.text_c3(f"{price} US$\n", self.black, 10, 225 + i * 30)
       
    def add_food_run(self): 
         self.run()
         
    def run(self):
    # Définition de la taille de la fenêtre
        
           
        # Boucle principale
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            # Remplir la fenêtre avec la couleur gris
            self.screen.fill(self.white)
            self.display_image()
            self.rectangle()
            self.display_text()
          
            # self.display_product()
          
            # Mettre à jour l'affichage            
      
            pygame.display.flip()
            pygame.display.update()


add_food = Add_Food()
add_food.add_food_run()
    
