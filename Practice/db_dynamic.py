# Crete program to connect to Database and enter name and city dynamic

import  sqlite3

connect = sqlite3.connect("st_data.db")

# create table


try:
    c_table = 'create table stud_info(id integer(10),name varchar(25))'
    connect.execute(c_table)
    print("Table has create successfully....")
except Exception as s:
    print(s)
    
# insert id and name 

id = int(input("Enter Your id :"))
name = input("Enter Your Name :")

in_data = "insert into stud_info"
    
