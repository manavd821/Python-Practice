import sqlite3, json

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        time VARCHAR(30) NOT NULL
    );
''')

def list_all_videos():
    for id, name, time in cursor.execute("SELECT * FROM videos"):
        print(f"{id}. {name}, duration: {time}.")
    # for row in cursor.execute("SELECT * FROM videos"):
    #     print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video():
    try:
        choose = int(input("Which video do you want to change(index): "))
        maxi = cursor.execute("SELECT COUNT(id) from videos").fetchone()[0]
        if choose < 1 or choose > maxi:
            print("Enter Correct value!")
            return
    except ValueError:
        print("Enter Correct value!")
        return
    new_name = input("Enter new Name: ")
    new_time = input("Enter duration: ")
    cursor.execute("UPDATE videos SET name = (?), time = (?) WHERE id = (?)",(new_name, new_time, choose))
    con.commit()
    print("Upadated successfully!")
def delete_video():
    try:
        choose = int(input("Which video do you want to delete(index): "))
        maxi = cursor.execute("SELECT COUNT(id) from videos").fetchone()[0]
        if choose < 1 or choose > maxi:
            print("Enter Correct value!")
            return
    except ValueError:
        print("Enter Correct value!")
        return   
    cursor.execute("DELETE FROM videos WHERE id = (?) ", (choose,))
    con.commit()
    print("Deleted successfully")

def main():     
    while True:
        print("\n Youtube Manager | Choose option")
        print("1. List all youtube videos")
        print("2. Add videos to list")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit video")

        choice = input("Choose: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Name: ")
                time = input("Duration: ")
                add_videos(name, time)
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice!")
                choice = input("\nChoose:")

    con.close()
    
if __name__ == '__main__':
    main()