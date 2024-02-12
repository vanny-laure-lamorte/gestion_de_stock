import pygame

class Global:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Store")
        self.clock = pygame.time.Clock()

        self.black = "#0e0f10"
        self.white = "#ffffff"
        self.brown = "#502c1e"
        self.light_brown = "#9f6736"
        self.orange = "#f26b33"
        self.beige = "#f2dec2"
        self.yellow = "#f6be2a"
        self.light_grey = "#f2f2f2"
        self.grey = "#868686"   
        self.green = "#488030"        
        self.red = "#d80001"    

        self.police_c1 = pygame.font.Font("AirstreamNF.ttf",30) # Titre main

        self.police_c2 = pygame.font.Font("AirstreamNF.ttf",60) # Titre food

        self.police_c3 = pygame.font.Font("AirstreamNF.ttf",18)
        self.police_c4 = pygame.font.Font(None,20)  
        self.police_c5 = pygame.font.Font("AirstreamNF.ttf",25)    
     
# Def text  
        
    
    def texte(self, texte_size, texte_content, color, x, y):
        pygame.font.init()
        Texte = pygame.font.Font("AirstreamNF.ttf", texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.screen.blit(Texte, Texte_rect)
    
    def texte_not_align(self, texte_size, texte_content, color, x, y):
        Texte = pygame.font.Font('files/font/metrophobic.ttf', texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(topleft=(x, y))
        self.screen.blit(Texte, Texte_rect)

    def text_c1(self,text, color, x, y):
        text_surface = self.police_c1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c2(self,text, color, x, y):
        text_surface = self.police_c2.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c4(self,text, color, x, y):
        text_surface = self.police_c4.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
  
# Def image
    def image(self,name,path,a,b,x,y):
        name = pygame.image.load(path)
        name = name.convert_alpha()
        name = pygame.transform.scale(name,(a,b))        
        self.screen.blit(name,(x,y))
        
    def img_back(self,name,path):
        name =  pygame.image.load(path).convert_alpha()
        L_name, H_name = name.get_size()
        name = pygame.transform.scale(name, (L_name,H_name))
        x =(self.screen_width - L_name)//2
        y = (self.screen_height - H_name)//2
        self.screen.blit(name, (x, y))
    
# Def rectangle   

    def rect_radius(self,radius,color,x1,y1,x2,y2):
        r = radius
        pygame.draw.rect(self.screen,color,(x1,y1,x2,y2),border_radius = r)  

    def rect_full(self, color, x, y, largeur, hauteur, arrondi):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - largeur//2, y - hauteur//2, largeur, hauteur),0, arrondi)
        return button

    def rect_border(self, color, x, y, largeur, longueur, epaisseur, arrondi):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, arrondi)
        return button
    
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.screen.fill((0, 0, 0))

    
