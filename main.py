from fichiers.global_def import Global
from fichiers.add_food import Food
from fichiers.food import Add_Food
from fichiers.store_management import Store_Management

import pygame, sys

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)
        self.food = Food()
        self.add_food = Add_Food()
        self.store_management = Store_Management()

    def menu_run(self): 
        self.options_menu()       

    # Afficher rectangles blancs et étoile         
    def  draw_menu_option(self, rect, text, pos):
        menu_text = self.police_p1.render(text, True, self.grey)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.white, rect.inflate(10, 10), border_radius=10)
            if pos==(710 - 100, 235 + 0 * 65, 200, 50):
                self.image("étoile",r"images/menu/image1.png",20,20,742,210)
            elif pos==(665 - 100, 235 + 1 * 65, 200, 50):
                self.image("étoile",r"images/menu/image1.png",20,20,742,275)
                
            elif pos==(730- 100, 235 + 2 * 65, 200, 50):
                self.image("étoile",r"images/menu/image1.png",20,20,742,345)
        else:
            pygame.draw.rect(self.screen, self.white, rect, border_radius=10)
        self.screen.blit(menu_text, pos) 

    # Afficher choix du menu
    def options_menu(self): 
        self.screen.fill(self.brown)
       
        self.running = True

        img_back = pygame.image.load(r"images/menu/image2.jpg").convert()

        option_rects = [
            pygame.Rect(650 - 100, 225 + i * 65, 200, 50) for i in range(4)
        ]
        option_texts = ["My Food", "Edit My Food List", "Quit"]

        while self.running:
            self.screen.blit(img_back, (0, 0))           

            for i, (rect, text) in enumerate(zip(option_rects, option_texts)):
                if text == "My Food":
                    position = (710 - 100, 235 + i * 65, 200, 50)
                elif text == "Edit My Food List":
                    position = (665 - 100, 235 + i * 65, 200, 50)
                else:
                    position = (730- 100, 235 + i * 65, 200, 50)

                self.draw_menu_option(rect, text, position)                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Liens vers autres pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, item in enumerate(option_texts):
                        rect = option_rects[i]
                        if rect.collidepoint(mouse_pos):
                            if item == "My Food":
                                self.food.food_run()                            
                            elif item == "Edit My Food List":
                                self.add_food.add_food_run()                    
                            elif item == "Quit":
                                pygame.quit()
                                sys.exit()  

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

menu = Menu()
menu.menu_run()

