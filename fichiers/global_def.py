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
        self.orange = "#f26b33"
        self.beige = "#f2dec2"
        self.yellow = "#f6be2a"

        self.grey = "#3c3c3c"   
        
       
        self.blue = "#375daa"
        
        self.green = "#488030"
        
        self.pink = "#f8a8b0"
        self.red = "#d80001"
        self.green2 = "#61e002"

        self.police_c1 = pygame.font.Font("AirstreamNF.ttf",60)
        self.police_c2 = pygame.font.Font("AirstreamNF.ttf",30)  
        self.police_c3 = pygame.font.Font("AirstreamNF.ttf",18)

        self.police_c4 = pygame.font.Font("AirstreamNF.ttf",18)  
        self.police_c5 = pygame.font.Font("AirstreamNF.ttf",15)    
        self.police_c6 = pygame.font.Font("AirstreamNF.ttf", 12)    
        self.police_p1 = pygame.font.Font("AirstreamNF.ttf", 25)
        self.lst_name = []
        
#def text  
        
    #L 
    def texte(self, texte_size, texte_content, color, x, y):
        pygame.font.init()
        Texte = pygame.font.Font("AirstreamNF.ttf", texte_size).render(texte_content, True, color)
        Texte_rect = Texte.get_rect(center=(x, y))
        self.screen.blit(Texte, Texte_rect)
    #L
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

    def text_c3(self,text, color, x, y):
        text_surface = self.police_c3.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c4(self,text, color, x, y):
        text_surface = self.police_c4.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def text_c5(self,text, color, x, y):
        text_surface = self.police_c5.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
    
    def text_c6(self,text, color, x, y):
        text_surface = self.police_c6.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_p1(self,text, color, x, y):
        text_surface = self.police_p1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

#def image
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
    
# def rectangle   
             
        # Rectangle 
    def rect(self,nom, x1,y1,x2,y2):   
        nom = pygame.Rect(x1,y1,x2,y2)

            # Rectangle Radius
    def rect_radius(self,radius,color,x1,y1,x2,y2):
        r = radius
        pygame.draw.rect(self.screen,color,(x1,y1,x2,y2),border_radius = r)  

    def rect_full(self, color, x, y, largeur, hauteur, arrondi):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - largeur//2, y - hauteur//2, largeur, hauteur),0, arrondi)
        return button

    def rect_border(self, color, x, y, largeur, longueur, epaisseur, arrondi):
        button = pygame.draw.rect(self.screen, color, pygame.Rect(x - largeur //2, y - longueur //2, largeur, longueur),  epaisseur, arrondi)
        return button