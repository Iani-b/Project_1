import time  #library to add a timer so text is not instantly skipped
import random

def title_func(song):                                   #this is essentialy a function that will be used to sort the dictionaries within the list. The inputs are the dicts...
    return song["title"]                                #...and the outputs are the titles of the songs for each dict

def convert_length_s(items):                                             #function to add song times and return back a string, a LIST of STRINGS is needed
    total_seconds = 0                                                    #counter is set to 0
    for string in items:
        minutes, seconds = string.split(":")                             #the minutes and seconds are split at the : and placed into the corresponding variable (unpacking)
        total_seconds = total_seconds + int(seconds) + int(minutes)*60   #total seconds are added for each song length that is went through
    return total_seconds                                                 #total seconds are returned

def main_menu():   #------------------------------
    print("\n-- OCRTunes --")
    print("\n1 : View Profile")
    print("2 : Edit Profile")
    print("3 : View Song Library")
    print("4 : Create A Playlist")
    print("5 : View And Edit Playlists")
    print("6 : Save Songs")
    print("E : Exit")
    choice = input("\nChoice --> ")
    return choice

def view_profile():   #------------------------------
    print("\n-- Profile --")
    print(f"\nUsername: {username}")
    print(f"Date of birth: {date_of_birth}")
    print(f"Favourite artist: {favourite_artist}")
    print(f"Favourite genre: {favourite_genre}")
    print("\nE : Exit")
    choice = input("\nChoice --> ")
    if choice.lower() == "e":
        return
    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)
        view_profile()

def edit_profile():   #------------------------------
    global favourite_artist, favourite_genre
    print("\n-- Edit Profile --")
    print("\nWhat would you like to change?")
    print("\n1 : Favourite artist")
    print("2 : Favourite genre")
    print("\nE : Exit")
    choice = input("\nChoice --> ")
    if choice == "1":
        favourite_artist = input("\nWho is your new favourite artist?: ")
        print("Changed Successfully")
        time.sleep(1.5)
        edit_profile()
    elif choice == "2":
        favourite_genre = input("\nWhat is your new favourite genre?: ")
        print("Changed Successfully")
        time.sleep(1.5)
        edit_profile()
    elif choice.lower() == "e":          
        return    
    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)
        edit_profile()

def view_song_library():   #------------------------------
    print("\n-- Song Library --")
    print("")
    sorted_songs = sorted(song_library, key = title_func)                    #key requires a function which I defined before. Every dictionary in song_library (input) is sorted using the titles of the songs (output) for which the key states (so song_library[0 to 19] are sorted in alphabetical order of song_library[0 to 19]["title"] hence the function). Found on https://www.w3schools.com/python/ref_func_sorted.asp very helpful.
    for song in sorted_songs:                                                #this for statement will then go through every dictionary within the sorted list in order...
        print(f"{song['title']} by {song['artist']} - {song['length']}")     #...and print the relevant information using f statements for each loop (dictionary)
        time.sleep(0.1)
    print("\nE : Exit")
    choice = input("\nChoice --> ")
    if choice.lower() == "e":
        return
    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)
        view_song_library()

def create_playlist():   #------------------------------
    global playlists
    print("\n-- Create A Playlist --")
    print("\n1 : Create Via Time Limit")
    print("2 : Create Via Genre")
    print("3 : Create Via Added Songs")
    print("\nE : Exit")
    choice = input("\nChoice --> ")
    
    if choice == "1":

        print("\n-- Create Playlist With Time Limit --")
        playlist_name = input("\nName of the playlist: ")
        while playlist_name in playlists.keys():
            print("\nThis Playlist Already exists...")
            time.sleep(1.5)
            playlist_name = input("\nName of the playlist: ")
        playlist_time_limit_s = int(input("Length of the playlist in minutes: ")) * 60
        min_length = min(convert_length_s([song["length"]]) for song in song_library)
        max_length = max(convert_length_s([song["length"]]) for song in song_library)
        while playlist_time_limit_s <= min_length or playlist_time_limit_s >= max_length * len(song_library):
            print("\nPlaylist cannot be made...")
            time.sleep(1.5)
            playlist_time_limit_s = int(input("\nLength of the playlist in minutes: ")) * 60
        playlist_songs = []
        playlist_length_s = 0
        while playlist_length_s < playlist_time_limit_s:
            temp_song = random.choice(song_library)
            if temp_song not in playlist_songs:
                temp_length = playlist_length_s + convert_length_s([temp_song["length"]])
                if temp_length <= playlist_time_limit_s:
                    playlist_songs.append(temp_song)
                    playlist_length_s = temp_length
                else:
                    break
        song_times = [times["length"] for times in playlist_songs]
        playlist_length_s = convert_length_s(song_times)
        playlists.update({playlist_name : {"songs" : playlist_songs , "length" : f"{playlist_length_s // 60}:{playlist_length_s % 60:02d}" , "num_songs" : int(len(playlist_songs))}})     #updates the playlists dictionary with a new playlist with the key for it being its name
        print("\nCreated Successfully")
        time.sleep(1.5)
        create_playlist()

    elif choice == "2":
        print()
        create_playlist()

    elif choice == "3":
        print()
        create_playlist()

    elif choice.lower() == "e":
        return

def view_delete_playlists():   #------------------------------
    global playlists
    print("\n-- View And Edit Playlists --")
    if not playlists:                                       #checks if there are any playlists
        print("\nYou have no playlists!")
    else:
        print("\nHere are all your playlists")
        print("Type it's name if you wish to view it")
        print("")
        for playlist in playlists:
            print(f"{playlist} : View Or Edit")
    print("\nE : Exit")
    choice = input("\nChoice --> ")
    playlist_title = choice

    if playlist_title in playlists.keys():

        print(f"\n-- {playlist_title} --")
        time.sleep(0.5)
        print(f"\nLength: {playlists[playlist_title]['length']} minutes")          #prints the length
        print(f"Number Of Songs: {playlists[playlist_title]['num_songs']}")        #prints the number of songs
        time.sleep(0.5)
        print("\nSongs:")
        time.sleep(0.5)
        print("")
        for song in playlists[playlist_title]['songs']:                            #a loop to list all the songs that are in the playlist
            print(f"{song['title']} by {song['artist']} - {song['length']}")
            time.sleep(0.1)
        print("\n1 : Delete This Playlist")
        print("\nE : Exit")
        choice = input("\nChoice --> ")

        if choice == "1":                                    #option to delete a playlist

            print("\n-- Deleting A Playlist --")
            print("\nAre You Sure?")                         #double checks
            print("\n1 : Yes")
            print("2 : No")
            choice = input("\nChoice --> ")
            if choice == "1":
                playlists.pop(playlist_title)                #deletes that playlist
                print("\nDeletion Succcessful")              #goes to the previous menu as that playlist does not exist anymore
                time.sleep(1.5)
                view_delete_playlists()
            elif choice == "2":                              #cancels the deletion
                print("\nDeletion Aborted")
                time.sleep(1.5)
                view_delete_playlists()
            else:                                                                #brings the user back to  the playlist menu to make sure no accidents happen
                print("\nThat's not one of the options... Deletion Aborted")
                time.sleep(1.5)
                view_delete_playlists()

        elif choice.lower() == "e":                        #exit the playlist menu
            return

        else:
            print("\nThat's not one of the options...")
            time.sleep(1.5)
            view_delete_playlists()

    elif choice.lower() == "e":                             #exit  
        return 

def save_songs():   #------------------------------
    return

def exit_program():   #------------------------------
    print(f"\nBuh Bye {username}!\n")     #says bye to the user
    return



song_library = [   #Song library in a dictionary in a list, took a fair bit to write
    {"title": "Tears", "artist": "Skrillex", "genre": "Electronic", "length": "3:45"},            #1st song
    {"title": "Dope", "artist": "Skrillex", "genre": "Electronic", "length": "3:35"},             #2nd
    {"title": "Bangarang", "artist": "Skrillex", "genre": "Electronic", "length": "3:35"},        #3rd
    {"title": "MOONSPELL", "artist": "Skrillex", "genre": "Electronic", "length": "4:00"},        #4th
    {"title": "Back In Black", "artist": "AC/DC", "genre": "Rock", "length": "4:15"},             #5th
    {"title": "Highway to Hell", "artist": "AC/DC", "genre": "Rock", "length": "3:28"},           #6th
    {"title": "Thunderstruck", "artist": "AC/DC", "genre": "Rock", "length": "4:52"},             #...
    {"title": "Hells Bells", "artist": "AC/DC", "genre": "Rock", "length": "5:12"},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": "Hip Hop", "length": "5:20"},
    {"title": "The Real Slim Shady", "artist": "Eminem", "genre": "Hip Hop", "length": "4:44"},
    {"title": "Without Me", "artist": "Eminem", "genre": "Hip Hop", "length": "4:50"},
    {"title": "Rap God", "artist": "Eminem", "genre": "Hip Hop", "length": "6:04"},
    {"title": "Brighter Days Ahead", "artist": "Ariana Grande", "genre": "Pop", "length": "4:00"},
    {"title": "Sports Car", "artist": "Ariana Grande", "genre": "Pop", "length": "3:25"},
    {"title": "DAISIES", "artist": "Ariana Grande", "genre": "Pop", "length": "3:05"},
    {"title": "Just Keep Watching", "artist": "Ariana Grande", "genre": "Pop", "length": "3:30"},
    {"title": "So What", "artist": "Miles Davis", "genre": "Jazz", "length": "9:05"},
    {"title": "Freddie Freeloader", "artist": "Miles Davis", "genre": "Jazz", "length": "9:46"},
    {"title": "Blue in Green", "artist": "Miles Davis", "genre": "Jazz", "length": "5:37"},
    {"title": "All Blues", "artist": "Miles Davis", "genre": "Jazz", "length": "11:33"}          #20th song and its details
]

playlists = {}  #dictionary that will contain all created playlists

print("\nWelcome to OCRTunes")
username = input("What will be your username?: ")
while username == "":
    print("\nIt can't be blank...")
    username = input("What will be your username?: ")
date_of_birth = input("What is your date of birth?: ")
while date_of_birth == "":
    print("\nIt can't be blank...")
    date_of_birth = input("What is your date of birth?: ")
favourite_artist = input("Who is your favourite artist?: ")
favourite_genre = input("What is your favourite genre?: ")

choice = main_menu()
while choice.lower() != "e":
    if choice == "1":

        view_profile()
        choice = main_menu()

    elif choice == "2":

        edit_profile()
        choice = main_menu()

    elif choice == "3":

        view_song_library()
        choice = main_menu()

    elif choice == "4":

        create_playlist()
        choice = main_menu()

    elif choice == "5":

        view_delete_playlists()
        choice = main_menu()

    elif choice == "6":

        save_songs()
        choice = main_menu()
        
    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)
        choice = main_menu()