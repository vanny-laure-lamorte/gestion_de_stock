from global_def import Global
from store_management import Store_Management

import mysql.connector

import pygame, sys

class Add_Food(Global):
    def __init__(self): 
            Global.__init__(self)
            self.store_m = Store_Management()
            self.rect_width = 300
            self.rect_height = 150
            self.height = 370
            self.rect_speed = 300 # Déclage 
            self.rectangles_position = 10 # position

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
        self.rect_full(self.light_grey, 400, 140, 450, 240, 5)
        self.rect_border(self.grey, 400, 140, 450, 240, 4, 5)   
        self.rect_full(self.white, 400, 60, 300, 40, 5) # Name
        self.rect_full(self.white, 400, 170, 400, 150, 5) # Description
        
        # Rect bas: titre
        self.rect_full(self.brown, 400, 550, 450, 80, 5)
        self.rect_border(self.yellow, 400, 550, 450, 80, 4, 5)      
        self.image("fleche","images/food/image3.png",20,20,560,50) # Flèche
      
    def button_menu(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c4("QUIT", self.black, 733, 13)
        else:
            self.rect_radius(5, self.light_grey, 720, 10, 70, 25)
            self.text_c4("QUIT", self.black, 733, 13)

    def display_design(self):
        self.screen.fill(self.white)
        self.display_image()
        self.rectangle()
        self.display_text()
        self.display_item()
        # self.draw_rectangles(self.rectangles_position)  
        self.button_menu()

    def display_item(self): 
        products = self.store_m.display_product() 
        
        for i in products: 
            print(i)

        # count_info = 0

        # product = 1

        # for product in products:
        #     product = product + 1             
        #     print(product)


     # count_info = count_info + 1



    
    # def draw_rectangles(self, x_pos):  
    #     nb = self.store_m.count_product()
    #     name_product = self.store_m.name_product()
    #     description_product = self.store_m.description_product()

    #     images = {
    #         0: pygame.image.load("images/food/image20.jpg"),
    #         1: pygame.image.load("images/food/image20.jpg"), 
    #         2: pygame.image.load("images/food/image20.jpg"), 
    #         3: pygame.image.load("images/food/image20.jpg"), 
    #         4: pygame.image.load("images/food/image20.jpg"), 
    #     }

    #     if nb:
    #         nb = nb[0]
    #         for i in range(nb): 
    #             rect = pygame.Rect(x_pos + i * (self.rect_width + 10), self.height // 2 - self.rect_height // 2, self.rect_width, self.rect_height)
    #             pygame.draw.rect(self.screen, self.orange, rect)
    #             pygame.draw.rect(self.screen, self.yellow, rect, 5)    

    #             str_name = name_product[i][0]
    #             result1 = str_name + ' '

    #             rect2 = pygame.Rect(rect.x, rect.y + rect.height, rect.width, 20)  # Rectangle pour la description sous le nom
    #             str_name = description_product[i][0]
    #             result2 = str_name + ' '

    #             if rect.collidepoint(pygame.mouse.get_pos()):
    #                 pygame.draw.rect(self.screen, self.black, rect, 5)
    #                 if i in images:
    #                     image = images[i]
    #                     image = pygame.transform.scale(image, (110, 119))
    #                     self.screen.blit(image, (400, 120))

    #             self.text_center2(result1, self.black, rect, 0)
    #             self.text_center2(result2, self.black, rect2, 0)


     
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

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   
    
    def add_food_run(self): 
         self.run()
         
    def run(self):
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.MOUSEBUTTONDOWN: 
                   if self.is_mouse_over_button(pygame.Rect(20,20,560,50)):
                       pass
                        
                        

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.rectangles_position += self.rect_speed
                    elif event.key == pygame.K_LEFT:
                        self.rectangles_position -= self.rect_speed                        
  
            self.display_design()
          
            pygame.display.flip()
            pygame.display.update()

add_food = Add_Food()
add_food.add_food_run()
    
