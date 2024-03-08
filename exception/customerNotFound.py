class CustomerNotFoundException(Exception):
    def __init__(self, CustomerID, message="Customer not found"):
        self.CustomerID = CustomerID
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def isCustomerExists(CustomerID, conn, stmt):
        stmt.execute('SELECT 1 FROM Customer WHERE CustomerID = %s', (CustomerID,))
        return bool(stmt.fetchone())