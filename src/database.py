import sqlite3


class Notepad:
    # initilize database (connecting)
    def __init__(self):
        self.conn = sqlite3.connect('trainingdb.db')
        self.c = self.conn.cursor()
        self.create_table_user()
        self.create_table_training()

    # create a table
    def create_table_user(self):
        # Uncomment to delete table
        # self.c.execute("""DROP TABLE users""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        goal TEXT,
        form TEXT,
        date DATE
        )""")
        self.conn.commit()

    # create a table
    def create_table_training(self):
        # Uncomment to delete table
        # self.c.execute("""DROP TABLE training""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS training (
        training_id INTEGER PRIMARY KEY AUTOINCREMENT,
        training_type TEXT,
        todays_goal TEXT,
        form TEXT,
        result TEXT,
        food_before_training TEXT,
        stomich_state TEXT,
        user_id INTEGER,
        date DATE,
        FOREIGN KEY(user_id) REFERENCES user(user_id)
        )""")
        self.conn.commit()

    # Insert data into table
    def insert_user(self, user):
        self.c.execute(
            """INSERT INTO user VALUES (NULL,?,?,?,?)""", user)
        self.conn.commit()

    # Insert data into table
    def insert_workout(self, workout):
        self.c.execute(
            """INSERT INTO training VALUES (NULL,?,?,?,?,?,?,?,?)""", workout)
        self.conn.commit()

    # print out all data
    def show_all_users(self):
        self.c.execute("SELECT * FROM user")
        items = self.c.fetchall()

        for item in items:
            print(item)
        self.conn.commit()

    # print out all data
    def show_all_workouts(self):
        self.c.execute("SELECT * FROM training")
        items = self.c.fetchall()

        for item in items:
            print(item)
        self.conn.commit()

    # This func will delete one entry
    def delete_one(self, id):
        self.c.execute("DELETE FROM user WHERE rowid = (?)", id)
        self.conn.commit()

    # Edit a entry in table.
    def edit_post(self, column, changed_data, id):
        self.c.execute(f"""UPDATE user SET '{column}' = '{changed_data}'
            WHERE rowid = {id}
            """)
        self.conn.commit()
