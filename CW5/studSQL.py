import sqlite3


def connect_SQl():
    global sqliteConnection
    try:
        sqliteConnection = sqlite3.connect('office.sqlite')  # open connection to db
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        # inserts data to the db
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Salim', 'Math', '95')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Noor', 'History', '94')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Noor', 'Biology', '96')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Salah', 'Math', '80')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Salim', 'History', '67')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Maria', 'Biology', '73')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Noor', 'Math', '100')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Maria', 'Math', '50')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Salah', 'History', '98')")
        cursor.execute("INSERT INTO Students (Name, Subject, Grade) VALUES ('Salim', 'Biology', '85')")

        sqliteConnection.commit()  # to make changes persistent in the database.
        print("Record inserted successfully into Students table ")
        cursor.close()

    # checks for errors if occurred
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def main():
    connect_SQl()


if __name__ == '__main__':
    main()
