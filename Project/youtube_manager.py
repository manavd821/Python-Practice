def load_data():
    pass

def list_all_videos(videos):
    pass
def add_video(videos):
    pass
def update_video(videos):
    pass
def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose option")
        print("1. List all youtube videos")
        print("2. Add videos to list")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit video")

        choice = input("Choose: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!")
                choice = input("\nChoose:")

if __name__ == "__main__":
    main()