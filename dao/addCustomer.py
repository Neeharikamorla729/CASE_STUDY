from util.DBConnUtil import dbConnection
def addCustomer():
    customerID=int(input("Enter Customer ID: "))
    firstName=input("Enter First Name: ")
    lastName=input("Enter Last Name: ")
    email=input("Enter email: ")
    phoneNumber=input("Enter Phone number: ")
    try:
        conn,stmt=dbConnection.open()
        data=[(customerID,firstName,lastName,email,phoneNumber)]
        stmt.executemany('''insert into Customer(customerID,firstName,lastName,email,phoneNumber)
                            values(%s,%s,%s,%s,%s)''',data)
        conn.commit()
        print("Data inserted Sucessfully")
    except Exception as E:
        print(f"ERROR DURING INSERTION {E}")
    finally:
        if conn:
            dbConnection.close(conn)
