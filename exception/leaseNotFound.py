class LeaseNotFoundException(Exception):
    def __init__(self,LeaseID,message="Lease Not fund\n"):
        self.LeaseID=LeaseID
        self.message=message
        super().__init__(self.message)
    def isLeaseExists(LeaseID,conn,stmt):
        stmt.execute('SELECT 1 FROM Lease WHERE LeaseID = %s', (LeaseID,))
        return bool(stmt.fetchone())