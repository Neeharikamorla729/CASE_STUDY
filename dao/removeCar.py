from util.DBConnUtil import dbConnection
from exception.carNotFound import CarNotFoundException
def removeCar():
    VehicleID=int(input("Enter Vehicle ID: "))

    try:
        conn,stmt=dbConnection.open()
        if not CarNotFoundException.isCarExists(VehicleID, conn, stmt):
            raise CarNotFoundException(VehicleID)
        data=(VehicleID,)
        stmt.execute('''delete from Vehicle where VehicleID=%s''',data)
        conn.commit()
        print("Car Deleted")
    except CarNotFoundException as ce:
        print(f"ERROR: {ce}")
    except Exception as E:
        print(f"ERROR: {E}")
    finally:
        if conn:
            dbConnection.close(conn)
