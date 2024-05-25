import tkinter
from tkinter import ttk, messagebox

class Ui:
    
    def __init__(self):
        self.firstName_Label = None
        self.firstName_input = None
        self.contact_label = None
        self.contact_input = None
        self.email_label = None
        self.email_input = None
        self.gender = None
        self.gender_male_input = None
        self.city_label = None
        self.city_list = None
        self.role_label = None
        self.role = None
        self.tk = None

        self.product_input = None
        self.price_input = None
        self.quantity_input = None
        self.manager_id_input = None

        self.login_name_input = None
        self.login_number_input = None

        self.update_id = None

        self.delete_id = None
        self.delete_item = None  

        self.buy_name = None
        self.buy_quantity = None    

    # user/Admin Login form
    def login(self):
        lg = tkinter.Tk()
        lg.title('Login')
        lg.geometry('300x300')
        lg.config(bg='lightgray')

        user_label = tkinter.Label(lg, text='Enter User Name', bg='lightgray', fg='black', font='lucida 10')
        user_label.place(x=100, y=50)

        self.login_name_input = tkinter.Entry(lg)
        self.login_name_input.place(x=90, y=80)

        login_number_label = tkinter.Label(lg, text='Enter Phone Number', bg='lightgray', fg='black', font='lucida 10')
        login_number_label.place(x=90, y=130)

        self.login_number_input = tkinter.Entry(lg)
        self.login_number_input.place(x=90, y=160)

        def login_submit():
            login_name = self.login_name_input.get()
            login_number = self.login_number_input.get()
            # Perform login validation here
            messagebox.showinfo('Welcome', 'Login Successful')

        log_in_btn = tkinter.Button(lg, text='Log in', bg='orange', fg='black', font='Lucida 10', width=10, command=lambda: [login_submit(), lg.destroy()]) 
        log_in_btn.place(x=110, y=230)

        lg.mainloop()

    # user/admin Registration form
    def reform(self):
        self.tk = tkinter.Tk()
        self.tk.title('Register Form')
        self.tk.geometry('500x600')
        self.tk.config(bg='lightgray')

        tag = tkinter.Label(self.tk, text='Please Enter Details Below', bg='orange', fg='white', font='Lucida 10 bold', width=63)
        tag.grid(row=0, column=0)

        # Enter Name
        self.firstName_Label = tkinter.Label(self.tk, text='Name *', bg='lightgray', fg='black', font='Lucida 10') 
        self.firstName_Label.place(x=30, y=40)

        self.firstName_input = tkinter.Entry(self.tk)
        self.firstName_input.place(x=150, y=43)

        # Enter Contact Number
        self.contact_label = tkinter.Label(self.tk, text='Contact *', bg='lightgray', fg='black', font='Lucida 10')
        self.contact_label.place(x=30, y=70)

        self.contact_input = tkinter.Entry(self.tk)
        self.contact_input.place(x=150, y=73)

        # Enter Email Address
        self.email_label = tkinter.Label(self.tk, text='Email *', bg='lightgray', fg='black', font='Lucida 10') 
        self.email_label.place(x=30, y=100)

        self.email_input = tkinter.Entry(self.tk)
        self.email_input.place(x=150, y=103)

        # Gender
        gender_label = tkinter.Label(self.tk, text='Gender', bg='lightgray', fg='black', font='Lucida 10')
        gender_label.place(x=30, y=130)

        self.gender_male_input = tkinter.Radiobutton(self.tk, value=0, text='Male', bg='lightgray', fg='Black', font='Lucida 10')
        self.gender_male_input.place(x=150, y=133)

        gender_female_input = tkinter.Radiobutton(self.tk, value=1, text='Female', bg='lightgray', fg='black', font='Lucida 10')
        gender_female_input.place(x=250, y=133)

        # City
        self.city_label = tkinter.Label(self.tk, text='Select Your City', bg='lightgray', fg='black', font='Lucida 10')
        self.city_label.place(x=30, y=160)

        city = ['Rajkot', 'Ahmadabad', 'Baroda', 'Surat', 'Junagadh', 'Gandhinagar']
        self.city_list = ttk.Combobox(self.tk, values=city)
        self.city_list.place(x=150, y=163)

        # Role
        self.role_label = tkinter.Label(self.tk, text='Select Your Role *', bg='lightgray', fg='black', font='Lucida 10')
        self.role_label.place(x=30, y=190)

        role_list = ['Product Manager', 'Customer']
        self.role = ttk.Combobox(self.tk, values=role_list)
        self.role.place(x=150, y=193)

        def btn_click():
            if len(self.firstName_input.get()) == 0:
                error = tkinter.Label(self.tk, text='Fill the details where *', bg='lightgray', fg='red', font='Lucida 10')
                error.place(x=190, y=250)
            else:
                messagebox.showinfo('Welcome', 'Your information has been registered')
                first_name = self.firstName_input.get()
                contact = self.contact_input.get()
                email = self.email_input.get()
                city = self.city_list.get() 
                role = self.role.get()
                # Save the user information

        reg_btn = tkinter.Button(self.tk, text='Register', bg='Orange', fg='black', font='Lucida 10', width=20, command=lambda: [btn_click(), self.tk.destroy()])
        reg_btn.place(x=170, y=300)

        login_btn = tkinter.Button(self.tk, text='Login', bg='Orange', fg='black', font='Lucida 10', width=20, command=lambda: [self.tk.destroy(), self.login()])
        login_btn.place(x=170, y=350)

        self.tk.mainloop()

    # product add form
    def products(self):
        pr = tkinter.Tk()
        pr.title('Add Product')
        pr.geometry('300x200')
        pr.config(bg='lightgray')

        product_label = tkinter.Label(pr, text='Product Name:', bg='lightgray', fg='black', font='Lucida 10')
        product_label.place(x=25, y=30)

        self.product_input = tkinter.Entry(pr)
        self.product_input.place(x=140, y=33) 

        price_label = tkinter.Label(pr, text='Product Price:', bg='lightgray', fg='black', font='Lucida 10')
        price_label.place(x=25, y=60)

        self.price_input = tkinter.Entry(pr)
        self.price_input.place(x=140, y=63)      

        quantity_label = tkinter.Label(pr, text='Product Quantity:', bg='lightgray', fg='black', font='Lucida 10')
        quantity_label.place(x=25, y=90)

        self.quantity_input = tkinter.Entry(pr)
        self.quantity_input.place(x=140, y=93)    

        def add_item():
            product_name = self.product_input.get()
            price = self.price_input.get()
            quantity = self.quantity_input.get()
            # Save the product information
            messagebox.showinfo('Welcome', 'Item has been added') 

        reg_btn = tkinter.Button(pr, text='Add Item', bg='Orange', fg='black', font='Lucida 10', width=15, command=lambda: [add_item(), pr.destroy()])
        reg_btn.place(x=85, y=140)

        pr.mainloop()

    # update product form
    def update(self):
        up = tkinter.Tk()
        up.title('Update Item')
        up.geometry('300x200')
        up.config(bg='lightgray')

        product_label = tkinter.Label(up, text='Product Name:', bg='lightgray', fg='black', font='Lucida 10')
        product_label.place(x=25, y=30)

        self.product_input = tkinter.Entry(up)
        self.product_input.place(x=140, y=33) 

        price_label = tkinter.Label(up, text='Product Price:', bg='lightgray', fg='black', font='Lucida 10')
        price_label.place(x=25, y=60)

        self.price_input = tkinter.Entry(up)
        self.price_input.place(x=140, y=63)      

        quantity_label = tkinter.Label(up, text='Product Quantity:', bg='lightgray', fg='black', font='Lucida 10')
        quantity_label.place(x=25, y=90)

        self.quantity_input = tkinter.Entry(up)
        self.quantity_input.place(x=140, y=93)    

        update_id_label = tkinter.Label(up, text='Your Id:', bg='lightgray', fg='black', font='Lucida 10')  
        update_id_label.place(x=25, y=120)

        self.update_id = tkinter.Entry(up)
        self.update_id.place(x=140, y=123)

        def update_item():
            product_name = self.product_input.get()
            price = self.price_input.get()
            quantity = self.quantity_input.get()
            update_id = self.update_id.get()
            # Update the product information
            messagebox.showinfo('Welcome', 'Item has been UPDATED') 

        reg_btn = tkinter.Button(up, text='Update Item', bg='Orange', fg='black', font='Lucida 10', width=15, command=lambda: [update_item(), up.destroy()])
        reg_btn.place(x=85, y=160)

        up.mainloop()

    # delete item form
    def delete(self):
        dl = tkinter.Tk()
        dl.title('Delete Item')
        dl.geometry('250x200')
        dl.config(bg='lightgray')

        delete_id_label = tkinter.Label(dl, text='Your Id:', bg='lightgray', fg='black', font='Lucida 10')
        delete_id_label.place(x=20, y=50)

        self.delete_id = tkinter.Entry(dl)
        self.delete_id.place(x=100, y=50)

        delete_item_label = tkinter.Label(dl, text='Item Name:', bg='lightgray', fg='black', font='Lucida 10')
        delete_item_label.place(x=20, y=80)

        self.delete_item = tkinter.Entry(dl)
        self.delete_item.place(x=100, y=80)

        def confirm():
            delete_id = self.delete_id.get()
            delete_item = self.delete_item.get()
            # Delete the item
            messagebox.showinfo('Warning', 'Item Has Been Deleted')

        del_button = tkinter.Button(dl, text='Delete', bg='orange', fg='black', font='Lucida 10', width=10, command=lambda: [confirm(), dl.destroy()])
        del_button.place(x=80, y=140)

        dl.mainloop()

    def buy(self):
        by = tkinter.Tk()
        by.title('Shop')
        by.geometry('300x400')
        by.config(bg='lightgray')

        buy_name_label = tkinter.Label(by, text='Item Name:', bg='lightgray', fg='black', font='Lucida 10')
        buy_name_label.place(x=30, y=30)         
        self.buy_name = tkinter.Entry(by)       
        self.buy_name.place(x=130, y=33)

        buy_quantity_label = tkinter.Label(by, text='Quantity:', bg='lightgray', fg='black', font='Lucida 10')
        buy_quantity_label.place(x=30, y=60) 
        self.buy_quantity = tkinter.Entry(by)
        self.buy_quantity.place(x=130, y=63)

        def buy_btn():
            buy_name = self.buy_name.get()
            buy_quantity = self.buy_quantity.get()
            # Process the purchase
            messagebox.showinfo('Welcome', 'Order has been placed')

        order_btn = tkinter.Button(by, text='Order', bg='orange', fg='black', command=lambda: [buy_btn(), by.destroy()], width=15)
        order_btn.place(x=90, y=100) 

        by.mainloop()

call = Ui()
call.reform()  # Example of calling a form
