from util.DBConnUtil import dbConnection
def listRentedCars():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''select V.VehicleID,V.make from Vehicle as V
                        join Lease as L on L.VehicleID=V.VehicleID''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR: {E}")
    finally:
        if conn:
            dbConnection.close(conn)
