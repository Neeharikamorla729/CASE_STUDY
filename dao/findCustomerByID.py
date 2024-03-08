from util.DBConnUtil import dbConnection
from exception.customerNotFound import CustomerNotFoundException
def findCustomerByID():
    CustomerID=int(input("Enter Customer ID: "))
    try:
        conn,stmt=dbConnection.open()
        if not CustomerNotFoundException.isCustomerExists(CustomerID, conn, stmt):
            raise CustomerNotFoundException(CustomerID)
        data=(CustomerID,)
        stmt.execute('''select * from Customer where CustomerID=%s''',data)
        record=stmt.fetchall()
        for i in record:
            print(i)
    except CustomerNotFoundException as ce:
        print(f"ERROR: {ce}")
    except Exception as E:
        print(f"ERROR: {E}")
    finally:
        if conn:
            dbConnection.close(conn)
