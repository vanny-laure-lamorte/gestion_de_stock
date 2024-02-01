import mysql.connector

class Store_Management:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="VannyLamorte25!",
            database="store"
        )
        self.cursor = self.connection.cursor()

    def add_product(self, name, description, price, quantity, id_category):
        sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, id_category)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_product(self, product_id):
        sql = "DELETE FROM product WHERE id = %s"
        values = (product_id,)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def modify_product(self, product_id, new_product):
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in new_product.items()])
        sql = f"UPDATE product SET {set_clause} WHERE id = %s" # VERIFIER
        self.cursor.execute(sql, (product_id,))
        self.connection.commit()

    def display_product(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        for product in products:
            print(product)
            
    def display_product_in_category(self):
        sql = "SELECT product.id, product.name, product.description, product.price, product.quantity, product.id_category FROM product LEFT JOIN category ON category.id = product.id_category"
        self.cursor.execute(sql)
        self.produit_available = self.cursor.fetchall()
        return self.produit_available       
        
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

food_manager = Store_Management() # MODIFIER
# food_manager.add_product("Pizza", "Pizza with pineapple", 15, 30, 1)
# food_manager.modify_product(8, {'name': 'Tortilla'}) #MODIFIER
# food_manager.delete_product(7)
food_manager.display_product()
food_manager.display_product_in_category()
# food_manager.close_connection()