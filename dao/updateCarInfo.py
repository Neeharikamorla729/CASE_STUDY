from util.DBConnUtil import dbConnection
from exception.carNotFound import CarNotFoundException
def UpdateCarAvailability():
    VehicleID=int(input("Enter vehicle ID: "))
    status=input("Enter Updated Status: ")
    try:
        conn,stmt=dbConnection.open()
        if not CarNotFoundException.isCarExists(VehicleID, conn, stmt):
            raise CarNotFoundException(VehicleID)
        data=(status,VehicleID)
        stmt.execute('''update Vehicle set status=%s where VehicleID=%s''',data)
        conn.commit()
        print("Data updated Successfully")
    except CarNotFoundException as ce:
        print(f"ERROR: {ce}")
    except Exception as E:
        print(E)
    finally:
        if conn:
            dbConnection.close(conn)