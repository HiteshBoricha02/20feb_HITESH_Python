
import pymysql

try:
    db = pymysql.connect(host="localhost",user="root",passwd="",database="stdata")

    cr = db.cursor()
    c_table = 'create table stud_info(id integer(10) primary key auto_increment,name varchar(25),city varchar(25))'
    cr.execute(c_table)
    print("Table has create successfully....")

    
except Exception as e:
    print(e)
    
    
# insert data
insert_data="insert into stud_info(name,city)values('HItesh','rajkot'),('Vijay','Morbi'),('Abhishek','Dwarka'),('Mihir','tops'),('harshil','Gondal'),('Piyush','rajkot')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
    
    
    