from database import Database


class CustomerService:
    def __init__(self):
        self.db = Database()

    def add_customer(self, cid, cname):
        existing = self.db.fetchone(
            "SELECT CID FROM Customer WHERE CID=?",
            (str(cid),)
        )

        if existing:
            raise Exception("Customer ID already exists.")

        self.db.execute(
            """
            INSERT INTO Customer (CID, CName)
            VALUES (?, ?)
            """,
            (
                str(cid),
                cname
            )
        )

    def get_all_customers(self):
        return self.db.fetchall(
            """
            SELECT CID, CName
            FROM Customer
            ORDER BY CName
            """
        )

    def get_customer_names(self):
        rows = self.db.fetchall(
            """
            SELECT CName
            FROM Customer
            ORDER BY CName
            """
        )

        return [row[0] for row in rows]

