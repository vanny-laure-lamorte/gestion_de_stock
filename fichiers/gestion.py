
"""
CREATE DATABASE store;
SHOW Databases;

USE store;

CREATE TABLE product(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT,
    price INT,
    quantity INT,
    id_category INT 
    );

SHOW COLUMNS
FROM product;

CREATE TABLE category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
    ); 

SHOW COLUMNS
FROM category;

INSERT INTO product(name, description, price, quantity, id_category) VALUES
('Cheeseburger',"Classic All-American Cheeseburger with Cheddar Cheese and topped with burger sauce, lettuce, tomatoes, and onion", 14, 50, 1),
('Cowboy Burger',"Thick-cut Hamburger that is served on a toasted bun with onions, cheese, bacon, optional jalapeños and BBQ sauce", 16, 40, 2),
('Veggie Burger',"A meatless Hamburger patty made from vegetables for a hearty alternative to beef. Served with lettuce, tomato, and onion, and your choice of mayonnaise or dressing on a Hawaiian roll", 13, 20, 3),
('Hot Dog Classic'," Simple but magnifique hot dog with crispy onions toppings, ketchup and mustard", 8, 10, 4),
('Buffalo Chiken Wings',"6 pcs of chicken wings coated in our flour mix and Southern fried. Crispy and juicy", 9, 60, 5),
('Fries', "Skins left on the fries and seasonedwith Rosemary and Cajun", 3, 60, 6);

SELECT *
FROM product;


INSERT INTO product(name, description, price, quantity, id_category) VALUES
('Cheeseburger',"Classic All-American Cheeseburger with Cheddar Cheese and topped with burger sauce, lettuce, tomatoes, and onion", 14, 50, 1);

SELECT *
FROM product;

INSERT INTO category(name) VALUES
('Hot Food'),
('Treats'), 
('Drinks'); 

SELECT *
FROM category; 

SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service
FROM employe
JOIN service ON employe.id_service = service.id


INSERT INTO product(name, description, price, quantity, id_category) VALUES
  ('Halloumi Wrap',"Halloumi, Salad, falafel", 13,25, 2),
  ('Veggie Hot Dog',"Plant Made Hot Dog", 11, 15, 2),
  ('Soup',"Soup Butternut Squash", 10, 15, 2),
  ('Cheesy Fries',"Fries with Cheese", 5, 50, 3),
  ('Curly Fries',"Fries with Cajun",7, 50, 3),
  ('Cheesy bread',"Bread with Cheese",5, 50, 3);
  

"""

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


