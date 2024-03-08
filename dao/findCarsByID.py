from util.DBConnUtil import dbConnection
from exception.carNotFound import CarNotFoundException
def findCarsByID():
    VehicleID=int(input("Enter Vehicle ID: "))
    try:
        conn,stmt=dbConnection.open()
        if not CarNotFoundException.isCarExists(VehicleID, conn, stmt):
            raise CarNotFoundException(VehicleID)
        data=(VehicleID,)
        stmt.execute('''select * from Vehicle where VehicleID=%s''',data)
        record=stmt.fetchall()
        for i in record:
            print(i)
    except CarNotFoundException as ce:
        print(f"ERROR: {ce}")
    except Exception as E:
        print(f"ERROR: {E}")
    finally:
        if conn:
            dbConnection.close(conn)