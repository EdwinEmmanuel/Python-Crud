from tabulate import tabulate
import mysql.connector
Con=mysql.connector.connect(host="localhost",user="root",password="accord",database="medical")

def insert(medname,mobile,quantity,price):
    res=Con.cursor()
    sql="insert into medbill (medname,mobile,quantity,price) values (%s,%s,%s,%s)"
    mname = (medname,mobile,quantity,price)
    res.execute(sql,mname)
    Con.commit()
    print("Data Inserted Successfully")

def update(medname,mobile,quantity,price,medcode):
    res = Con.cursor()
    sql = "update medbill set medname=%s,mobile=%s,quantity=%s,price=%s where medcode=%s"
    mname = (medname, mobile, quantity, price, medcode)
    res.execute(sql, mname)
    Con.commit()
    print("Data Updated Successfully")


def select():
    res = Con.cursor()
    sql = "SELECT Medcode,Medname,Mobile,Quantity,Price from medbill"
    res.execute(sql)
    #result = res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result,headers=["MEDCODE","MEDNAME","MOBILE","QUANTITY","PRICE"]))



def delete(medcode):
    res = Con.cursor()
    sql = "delete from medbill where medcode=%s"
    mname = (medcode,)
    res.execute(sql, mname)
    Con.commit()
    print("Data Deleted Successfully")

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        medname = input("Enter Medname: ")
        mobile = int(input("Enter Mobile Number: "))
        quantity = int(input("Enter Quantity: "))
        price = int(input("Enter Price: "))
        insert(medname,mobile,quantity,price)
    elif  choice==2:
           medcode=input("Enter Medcode: ")
           medname = input("Enter Medname: ")
           mobile = int(input("Enter Mobile Number: "))
           quantity = int(input("Enter Quantity: "))
           price = int(input("Enter Price: "))
           update(medname,mobile,quantity,price,medcode)
    elif choice==3:
          select()
    elif choice==4:
          medcode = input("Enter medcode to Delete: ")
          delete(medcode)
    elif choice==5:
          quit()
    else:
        print("Invalid Selection . Please Try Again !")





