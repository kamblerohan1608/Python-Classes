import mysql.connector as db

class connection:
    def __init__(self):

        #****************** Create Table ******************

        #Connection String

        mydb = db.connect(host = "localhost",user = "dbuser",passwd = "dbuser",database = "dbuser")

        # Cursor

        cur = mydb.cursor()
        query = ''' create table if not exists rohan(id int not null auto_increment,
        name varchar(100) not null,
        age int check(age>10),
        contact bigint unique,
        location varchar(100) default "Thane",
        primary key (id));'''
        cur.execute(query)

        mydb.close()

    def insert_info(self,name,age,contact,loc):
        mydb = db.connect(host = "localhost",user = "dbuser",passwd = "dbuser",database = 'dbuser')
        cur = mydb.cursor()

        query = f'''insert into rohan(name,age,contact,location) values("{name}",{age},{contact},"{loc}");'''
        cur.execute(query)
        cur.execute("commit;")    # when data in table has to be effected like inserting or updating
        mydb.close()

    def read_data(self):
        mydb = db.connect(host = "localhost",user = "dbuser",passwd = "dbuser",database = 'dbuser')
        cur = mydb.cursor()
        query = f'''select * from rohan;'''
        cur.execute(query)
        data = cur.fetchall()    # fetchone
        mydb.close()
        return data

app = connection()

# insert Information

# name  = input("Enter your Name : ")
# age = int(input("Enter Your Age : "))
# contact = int(input("Enter Your contact : "))
# loc = input("Enter Your Location : ")

# app.insert_info(name,age,contact,loc)


# fetch data 

# data = app.read_data()
# print(data)

