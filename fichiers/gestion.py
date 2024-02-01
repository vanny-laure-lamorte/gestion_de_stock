
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
('Cheeseburger',"Classic All-American Cheeseburger with Cheddar Cheese and topped with burger sauce, lettuce, tomatoes, and onion", 14, 50, 1),

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

"""


