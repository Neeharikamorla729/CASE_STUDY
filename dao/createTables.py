from util.DBConnUtil import dbConnection


def createTables():
    conn = None
    try:
        conn, stmt = dbConnection.open()
        if conn:
            stmt.execute('''create table if not exists Vehicle(vehicleID int primary key,
                                make varchar(20), model varchar(30), year int, dailyRate decimal(10,2),
                                status char(1), passengerCapacity int, engineCapacity int) ''')

            stmt.execute('''create table Customer(customerID int primary key,
                                firstName varchar(30), lastName varchar(30),
                                email varchar(30),phoneNumber char(10))''')

            stmt.execute('''create table Lease(leaseID int primary key,
                                vehicleID int,
                                customerID int,
                                startDate date,
                                endDate date,
                                types varchar(20),
                                foreign key (vehicleID) references Vehicle (vehicleID),
                                foreign key (customerID) references Customer (customerID))''')

            stmt.execute('''create table Payment(paymentID int primary key,
                                leaseID int,
                                paymentDate date,
                                Amount decimal(10,2),
                                foreign key (leaseID) references Lease (leaseID))''')
    except Exception as E:
        print(f"Error during database initialization: {E}")


    finally:
        if conn:
            dbConnection.close(conn)