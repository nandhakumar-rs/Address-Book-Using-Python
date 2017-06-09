import sqlite3


class Database:
    def __init__(self):
        self.connect, self.cursor = initiate()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS addresss(ID INTEGER  PRIMARY KEY ,names TEXT,email TEXT,mobile INTEGER,city TEXT,pincode INTEGER)")

    def insert(self, name, email, mobile, city, pincode):
        self.connect, self.cursor = initiate()
        self.cursor.execute("INSERT INTO addresss VALUES(NULL,?,?,?,?,?)", (name, email, mobile, city, pincode))
        self.connect.commit()

    def update(self, name, email, mobile, city, pincode, id):
        self.connect, self.cursor = initiate()
        self.cursor.execute(" UPDATE addresss SET names=? ,email =?,mobile=?,city=?,pincode=? WHERE id =?",
                            (name, email, mobile, city, pincode, id))
        self.connect.commit()

    def view(self):
        self.connect, self.cursor = initiate()
        self.cursor.execute("SELECT * FROM addresss")
        records = self.cursor.fetchall()
        return records

    def search(self, name="", email="", mobile="", city="", pincode=""):
        self.connect, self.cursor = initiate()
        self.cursor.execute("SELECT * FROM addresss WHERE names=? OR email=? OR mobile=? OR city=? OR pincode=?",
                            (name, email, mobile, city, pincode))
        records = self.cursor.fetchall()
        return records

    def delete(self, id):
        self.connect, self.cursor = initiate()
        self.cursor.execute("DELETE FROM addresss WHERE id=?", (id,))
        self.connect.commit()

    def __del__(self):
        self.connect.close()


def initiate():
    connect = sqlite3.connect("address.db")
    cursor = connect.cursor()
    return connect, cursor

# # insert("name", "email", 9994396987, "city", 641029)
# insert("nam"," email",987456123,"city",647523)
# insert("raj","remail",987456123,"city",647523)
# #  delete(2)
# print(view())
# print(search(email="remail"))
