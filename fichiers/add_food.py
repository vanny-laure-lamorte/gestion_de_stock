from global_def import Global
import pygame

class Food(Global):
    def __init__(self): 
            Global.__init__(self)
            self.name = ""
            self.description = ""
            self.price = "" 
            self.quantity = "" 
            self.id_category = "" 

    pygame.init()

    def food_run(self): 
         self.run() 

    def input(self):  
        self.input_name = self.rect_border(self.yellow, 400, 300, 200, 60, 5, 5)
        self.input_description = self.rect_border(self.yellow, 400, 350, 200, 60, 5, 5)
        self.input_price = self.rect_border(self.yellow, 400, 400,200, 60, 5, 5)
        self.input_quantity = self.rect_border(self.yellow, 400, 450, 200, 60, 5, 5)
        self.input_id_category= self.rect_border(self.yellow, 400, 500,200, 60, 5, 5)

    def text(self): 
        self.texte(12, self.name, self.black, 400, 300)
        self.texte(12, self.description, self.black, 400, 350)

    def rectangle(self):
        self.check = self.rect_border(self.orange, 400, 10,200, 60, 5, 5)

    def display_design(self):
        self.screen.fill(self.white)           
        self.input()
        self.rectangle()
        self.text()

       
    def run(self):

        # Boucle principale
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
                        pass
                    
                        # if self.name != "" and self.description != "" and self.price != "" and self.quantity != "" and                        self.id_category != "" :                  
                            # self.add_product(self.name, self.description, self.price, self.quantity, self.id_category)


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
                        if event.unicode.isalpha():
                            price = price + event.unicode
                    elif self.entry == 4:
                        if event.unicode.isalpha():
                            quantity = quantity + event.unicode
                               
                # Remplir la fenêtre avec la couleur gris
              
            pygame.display.flip()
            pygame.display.update()
  
food = Food()
food.food_run()
    
