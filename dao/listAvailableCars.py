from util.DBConnUtil import dbConnection
def listAvailableCars():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''select * from vehicle where status='available' ''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR: {E}")
    finally:
        if conn:
            dbConnection.close(conn)
