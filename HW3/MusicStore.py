import sqlite3


def addTrack():
    print()
    print('Enter the needed data to add a new track')
    try:
        # inserts to the tracks table new row for the new song
        cursor.execute("INSERT INTO tracks (Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, "
                       "UnitPrice) VALUES(?,?,?,?,?,?,?,?)",
                       (input('Name: '), int(input('Album id: ')), int(input('Media type id: ')),
                        int(input('Genre id: ')),
                        input("Composer: "), int(input('Milliseconds: ')), int(input('Bytes: ')),
                        int(input('Unit price:')),))

        sqliteConnection.commit()  # to make changes persistent in the database.
        # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def getPlaylist():
    print()
    print('Enter the id of the playlist you want to show')
    try:
        cursor.execute("SELECT DISTINCT Name FROM tracks LEFT JOIN"
                       "(SELECT TrackId FROM playlist_track JOIN playlists ON "
                       "playlist_track.PlaylistId = playlists.PlaylistId "
                       "WHERE playlists.PlaylistId = ?) LIMIT ?",
                       (int(input('Playlist id:')), int(input('How many songs you want to get ? ')),)
                       )

        names = cursor.fetchall()
        for name in names:
            print(*name)
        print()
        sqliteConnection.commit()  # to make changes persistent in the database.
        # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def creatPlaylist():
    print()
    print('Enter the needed data to create new playlist')
    try:
        # inserts to the playlists table new row for the new playlist
        cursor.execute("INSERT INTO playlists (PlaylistId, Name) VALUES (?, ?)",
                       (int(input("PlaylistId: ")), input("Name: "),))
        sqliteConnection.commit()  # to make changes persistent in the database.
    # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def addSongs():
    print()
    print('Enter the needed data to add a song to a playlist')
    try:
        # inserts to the playlist_track table new row for the new track
        cursor.execute("INSERT INTO playlist_track (PlaylistId, TrackId) VALUES(?,?) ",
                       (int(input("Playlist Id: ")), input("Track Id: "),))

        sqliteConnection.commit()  # to make changes persistent in the database.
        # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def addEmployee():
    print()
    print('Enter the needed data to add a new employee')
    try:
        # inserts to the employees table new row for the new employee
        cursor.execute("INSERT INTO employees "
                       "(EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, "
                       "Country, PostalCode, Phone, Fax, Email) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (int(input("Employee Id: ")), input("Last Name: "), input("First Name: "), input("Title: "),
                        input("Reports To: "), input("Birth Date: "), input("Hire Date: "), input("Address: "),
                        input("City: "), input("State: "),
                        input("Country: "), int(input("Postal Code: ")), int(input("Phone: ")), int(input("Fax: ")),
                        input("Email: "),)
                       )
        sqliteConnection.commit()  # to make changes persistent in the database.
    # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def deleteEmployee():
    print()
    print('Enter the needed data to delete the wanted employee')
    try:
        # deletes from the employees table the unwanted employee
        cursor.execute("DELETE FROM employees Where EmployeeId = ?", ((int(input('Employee Id: '))),))
        sqliteConnection.commit()  # to make changes persistent in the database.
        # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def report():
    print()
    print('Enter the needed data to add information about a purchase to the DB')
    try:
        # inserts to the customers table new row for the new customer
        cursor.execute(
            "INSERT INTO customers (CustomerId, FirstName, LastName, Company, Address, City, State, Country, "
            "PostalCode, Phone, Fax, Email, SupportRepId)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (int(input("Customer Id: ")), input("First Name: "), input("Last Name: "), input("Company: "),
             input("Address: "), input("City: "), input("State: "), input("Country: "),
             int(input("Postal Code: ")), int(input("Phone: ")), int(input("Fax: ")), input("Email: "),
             int(input("SupportRep Id: ")),)
        )
        sqliteConnection.commit()  # to make changes persistent in the database.
    # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def printRevenues():
    pass


def Exit():
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()
    exit(0)


def doProcess(choice):
    if choice == 1:addTrack()
    elif choice == 2:
        getPlaylist()
    elif choice == 3:
        creatPlaylist()
    elif choice == 4:
        addSongs()
    elif choice == 5:
        addEmployee()
    elif choice == 6:
        deleteEmployee()
    elif choice == 7:
        report()
    elif choice == 8:
        printRevenues()
    elif choice == 9:
        Exit()
    else:
        print('Error: invalid input, try another one !')
        print()
        menu()


def menu():
    print("************MAIN MENU**************")

    choice = int(input("""1: Add a track\n2: Get a playlist
3: Create a playlist
4: Add a song to playlist
5: Add employee
6: Delete employee
7: Report on a purchase
8: Print revenues
9: Exit
Please enter your choice: """))

    while choice in range(1, 10):
        doProcess(choice)
        print("************MAIN MENU**************")

        choice = int(input("""1: Add a track\n2: Get a playlist
3: Create a playlist
4: Add a song to playlist
5: Add employee
6: Delete employee
7: Report on a purchase
8: Print revenues
9: Exit
Please enter your choice: """))
        doProcess(choice)
    if choice not in range(1, 10):
        print('Error: invalid input, try another one !')
        print()

        menu()


def connectSQL():
    # sets the sql connection variables as global so we can use them in any part of the code
    global sqliteConnection
    global cursor

    try:
        # open connection to db
        sqliteConnection = sqlite3.connect('chinook.db')  # open connection to db
        cursor = sqliteConnection.cursor()

    # catches errors if occurred
    except sqlite3.Error as error:
        print("Failed to update data to sqlite table", error)


def main():
    print('This program to manage a record store\n')
    connectSQL()
    menu()


if __name__ == '__main__':
    main()
