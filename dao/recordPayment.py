from util.DBConnUtil import dbConnection
def recordPayment():
    paymentID=int(input("Enter Payment ID: "))
    leaseID=int(input("Enter Lease ID: "))
    paymentDate=input("Enter payment Date")
    Amount=float(input("Enter amount: "))
    try:
        conn,stmt=dbConnection.open()
        data=[(paymentID,leaseID,paymentDate,Amount)]
        stmt.executemany('''insert into Payment(paymentID,leaseID,paymentDate,Amount)
                            values(%s,%s,%s,%s)''',data)
        conn.commit()
        print("Data inserted Successfully")
    except Exception as E:
        print(f"ERROR DURING INSERTION {E}")
    finally:
        if conn:
            dbConnection.close(conn)
