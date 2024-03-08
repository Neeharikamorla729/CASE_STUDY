class CarNotFoundException(Exception):
    def __init__(self, VehicleID, message="Car not found"):
        self.VehicleID = VehicleID
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def isCarExists(VehicleID, conn, stmt):
        stmt.execute('SELECT 1 FROM Vehicle WHERE VehicleID = %s', (VehicleID,))
        return bool(stmt.fetchone())
