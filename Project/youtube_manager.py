import json
ytFile = 'youtube.txt'
def load_data():
    try:
        with open(ytFile, 'r') as file:
            test = json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
            return []

def add_data_to_file(videos):
    with open(ytFile, 'w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('*' * 70)
    for idx, video in enumerate(videos, start = 1):
        print(f"{idx}. {video['name']}, duration: {video['time']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter duration: ")
    videos.append({'name':name, 'time':time})
    add_data_to_file(videos)

def update_video(videos):
    try:
        change = int(input("Which video do you want to change (index): "))
        if change < 1 and change > len(videos):
            print("Invalid index!")
            return
    except ValueError:
        print("Invalid index!")
        return
    
    choice = input("What do you want to change:\n1).name 2).duration 3).both\nchoose index: ")
    newName = None
    newTime = None

    if choice == '1':
        newName = input("Enter new name: ")
    elif choice == '2':
        newTime = input("Enter new duration: ")
    elif choice == '3':
        newName = input("Enter new name: ")
        newTime = input("Enter new duration: ")
    else:
        print("Enter correct option (1, 2, or 3)!")
        return
    
    # for idx, video in enumerate(videos, start=1):
    #     if idx == change:
    #         if newName:
    #             video['name'] = newName
    #         if newTime:
    #             video['time'] = newTime
    #         add_data_to_file(videos)
    #         return
    # print("Enter correct value:")

    # or methode: 2
    video = videos[change-1]
    if newName:
        video['name'] = newName
    if newTime:
        video['time'] = newTime

    add_data_to_file(videos)
    print("Video updated successfully.")


def delete_video(videos):
    try:
        change = int(input("Which video do you want to delete (index): "))
        if change < 1 and change > len(videos):
            print("Invalid index!")
            return
    except ValueError:
        print("Invalid index!")
        return
    # removed = videos.pop(change-1)
    # print(removed) # it will give you deleted video
    # add_data_to_file(videos)
    # print("Video deleted successfully.")

    # methode 2:
    del videos[change-1]
    add_data_to_file(videos)
    print("Video deleted successfully.")


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