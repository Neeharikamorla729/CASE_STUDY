from util.DBConnUtil import dbConnection


def addVehicle():
    vehicleID = int(input("Enter VehicleID: "))
    make = input("Enter make: ")
    model = input("Enter model")
    year = int(input("Enter year"))
    dailyRate = float(input("Enter daily Rate: "))
    status = input("Enter status: ")
    passengerCapacity = int(input("Enter passenger capacity: "))
    engineCapacity = int(input("Enter engine capacity: "))
    try:
        conn, stmt = dbConnection.open()
        data = [(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)]
        stmt.executemany('''insert into Vehicle(vehicleID,make,model,year,dailyRate,status,passengerCapacity,engineCapacity)
                            values(%s,%s,%s,%s,%s,%s,%s,%s)''', data)
        conn.commit()
        print("Data inserted sucessfully")

    except Exception as E:
        print(f"ERROR DURING INSERTION {E}")
    finally:
        if conn:
            dbConnection.close(conn)