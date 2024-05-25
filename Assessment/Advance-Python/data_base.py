from form import Ui
import pymysql

v = Ui()

class Tables:
    def __init__(self):
        self.db = None
        self.cr = None
        self.connect_db()
    
    def connect_db(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='', database='product_management')
            print('Connection Established')
            self.cr = self.db.cursor()
        except Exception as e:
            print(e)
    
    def Database(self):
        # creating table for customer and manager registration
        try:
            tbl_customer = '''
                CREATE TABLE IF NOT EXISTS Customer (
                    id INT PRIMARY KEY AUTO_INCREMENT, 
                    Name VARCHAR(30), 
                    Contact_No VARCHAR(10), 
                    Email VARCHAR(50), 
                    Gender VARCHAR(7), 
                    City VARCHAR(20)
                )
            '''
            self.cr.execute(tbl_customer)
            self.db.commit()
        except Exception as e:
            print(e)

        try:
            tbl_pm = '''
                CREATE TABLE IF NOT EXISTS ProductManager (
                    id INT PRIMARY KEY AUTO_INCREMENT, 
                    Name VARCHAR(30), 
                    Contact_No VARCHAR(10), 
                    Email VARCHAR(50), 
                    City VARCHAR(20)
                )
            '''
            self.cr.execute(tbl_pm)
            self.db.commit()
        except Exception as e:
            print(e)
        
        # creating table for customer and manager's product buying and selling
        if v.role == 'Product Manager':
            try:
                items = '''
                    CREATE TABLE IF NOT EXISTS items (
                        id INT PRIMARY KEY AUTO_INCREMENT, 
                        productName VARCHAR(30), 
                        Price INT, 
                        Quantity INT
                    )
                '''
                self.cr.execute(items)
                self.db.commit()
            except Exception as e:
                print(e)
        elif v.role == 'Customer':
            try:
                buy = '''
                    CREATE TABLE IF NOT EXISTS buy (
                        id INT PRIMARY KEY AUTO_INCREMENT, 
                        ProductName VARCHAR(30), 
                        Quantity INT
                    )
                '''
                self.cr.execute(buy)
                self.db.commit()
            except Exception as e:
                print(e)

class Manager(Tables):
    def addItems(self):
        try:
            v.products()
            add_item = f"INSERT INTO items(productName, Price, Quantity) VALUES('{v.product_input}', {v.price_input}, {v.quantity_input})"
            self.cr.execute(add_item)
            self.db.commit()
        except Exception as e:
            print(e)
    
    def updateItem(self):
        try:
            v.update()
            update_item = f"UPDATE items SET productName = '{v.product_input}', Price = {v.price_input}, Quantity = {v.quantity_input} WHERE id = {v.update_id}"
            self.cr.execute(update_item)
            self.db.commit()
        except Exception as e:
            print(e)
    
    def deleteItem(self):
        try:
            v.delete_item()
            delete_item = f"DELETE FROM items WHERE id = {v.delete_id} AND productName = '{v.delete_item}'"
            self.cr.execute(delete_item)
            self.db.commit()
        except Exception as e:
            print(e)

class Customer(Manager):
    def showItems(self):
        try:
            view_item = "SELECT * FROM items"
            self.cr.execute(view_item)
            show = self.cr.fetchall()
            
            print('|\tID \t|\t  ITEM \t\t|\t  PRICE \t|\t QUANTITY \t|\n')
            for i in show:
                print(f'|\t {i[0]} \t|\t {i[1]} \t|\t {i[2]} \t\t|\t {i[3]} \t\t|')
        except Exception as e:
            print(e)

    def buyItems(self):
        try:
            self.showItems()
            v.buy()
            buy_item = f"INSERT INTO buy(ProductName, Quantity) VALUES('{v.buy_name}', {v.buy_quantity})"
            self.cr.execute(buy_item)
            self.db.commit()
            
            update = f"UPDATE items SET Quantity = Quantity - {v.buy_quantity} WHERE productName = '{v.buy_name}' AND Quantity >= {v.buy_quantity}"
            self.cr.execute(update)
            self.db.commit()
        except Exception as e:
            print(e)

tb = Customer()
tb.Database()

if v.role == 'Product Manager':
    try:
        p_info = f"INSERT INTO ProductManager(Name, Contact_No, Email, City) VALUES('{v.firstName_input}', '{v.contact_input}', '{v.email_input}', '{v.city_list}')"
        tb.cr.execute(p_info)
        tb.db.commit()
    except Exception as e:
        print(e)
elif v.role == 'Customer':
    try:
        c_info = f"INSERT INTO Customer(Name, Contact_No, Email, City) VALUES('{v.firstName_input}', '{v.contact_input}', '{v.email_input}', '{v.city_list}')"
        tb.cr.execute(c_info)
        tb.db.commit()
    except Exception as e:
        print(e)

def LOGIN():
    view_manager = "SELECT * FROM ProductManager"
    tb.cr.execute(view_manager)
    show_manager = tb.cr.fetchall()
    
    for i in show_manager:
        if v.login_name_input == i[1] and v.login_number_input == i[2]:
            p_c = 'y'
            while p_c.lower() == 'y':
                print("""
                      - Press 1 : Add Item 
                      - Press 2 : Update Item
                      - Press 3 : Remove Item
                      """)
                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    tb.addItems()
                elif choice == 2:
                    tb.updateItem()
                elif choice == 3:
                    tb.deleteItem()
                p_c = input('Want to perform more operations (y/n)? : ')
            return

    view_customer = "SELECT * FROM Customer"
    tb.cr.execute(view_customer)
    show_customer = tb.cr.fetchall()
    
    for i in show_customer:
        if v.login_name_input == i[1] and v.login_number_input == i[2]:
            c_c = 'y'
            while c_c.lower() == 'y':
                print("""
                        - Press 1 : Show Item
                        - Press 2 : Buy Item
                      """)
                c_choice = int(input("Enter Choice : "))

                if c_choice == 1:
                    tb.showItems()
                elif c_choice == 2:
                    tb.buyItems()
                c_c = input('Continue shopping (y/n)? : ')
            return
    print("User Name or Number is Wrong")

LOGIN()
