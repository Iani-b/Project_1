import json           #library to read and write json files
import time           #library to add a timer so text is not instantly skipped
import random         #library to randomly select songs for playlist creation

def title_func(song):               #this is essentialy a function that will be used to sort the dictionaries within the list. The inputs are the dicts...
    return song["title"]            #...and the outputs are the titles of the songs for each dict

def convert_length_s(items):                    #function to add song times and return back a string, a LIST of STRINGS is needed
    total_seconds = 0                           #counter is set to 0
    for string in items:
        minutes, seconds = string.split(":")                             #the minutes and seconds are split at the : and placed into the corresponding variable (unpacking)
        total_seconds = total_seconds + int(seconds) + int(minutes)*60   #total seconds are added for each song length that is went through
    return total_seconds                                                 #total seconds are returned

def startup():   #------------------------------ Startup --------------------------

    global username, favourite_artist, favourite_genre, date_of_birth, playlists   #these variables are global so they can be changed
    print("\n-- Welcome to OCRTunes --")
    while True:
        print("\nLogin or Sign Up?")                
        print("\n1 : Sign Up")
        print("2 : Login")
        choice = input("\nChoice --> ")                   
        while choice != "1" and choice != "2":               #input validation
            print("\nThat's not one of the options...")
            time.sleep(1.5)
            choice = input("\nChoice --> ")
        if choice == "1":                                    #option to sign up
            
            try:
                with open("users.json", "r") as users_json:              #tries to open the json file to read the existing users
                    users = json.load(users_json)                        #loads the json file into a dictionary
            except (FileNotFoundError, json.decoder.JSONDecodeError):    #if the file does not exist or is empty it creates an empty json file and an empty dictionary
                with open("users.json", "w") as users_json:
                    pass
                users = {}                                               #empty dictionary

            username = input("\nEnter Your Username: ")
            while username == "" or username in users:                   #checks if the username is valid and does not already exist
                print("\nUsername is invalid or already exists...")
                time.sleep(1.5)
                username = input("\nEnter Your Username: ")
            password = input("Enter Your Password: ")
            while password == "":                                        #checks if the password is valid
                print("\nPassword is invalid...")
                password = input("\nEnter Your Password: ")
            date_of_birth = input("What is your date of birth (DD/MM/YYYY): ")
            favourite_artist = input("Who is your favourite artist?: ")
            favourite_genre = input("What is your favourite genre?: ")

            users.update({username : {"password" : password , "date_of_birth" : date_of_birth , "artist" : favourite_artist , "genre" : favourite_genre , "playlists" : {}}})  #updates the users dictionary with a new user, with the key for it being their username

            with open("users.json", "w") as users_json:        #opens the json file in write mode to overwrite it with the new users dictionary   
                json.dump(users, users_json, indent = 4)       #dumps the users dictionary into the json file with 4 spaces for readability
            break

        elif choice == "2":                  #option to log in

            try:
                with open("users.json", "r") as users_json:               #tries to open the json file to read the existing users
                    users = json.load(users_json)
            except (FileNotFoundError, json.decoder.JSONDecodeError):     #if the file does not exist it creates an empty dictionary and tells them to sign up
                print("\nPlease Create an account...")
                users = {}
                time.sleep(1.5)
                continue              #goes back to the start of the login/signup loop

            username = input("\nEnter Your Username: ")
            if username not in users:                               #if the username does not exist in the users dictionary
                print("\nThis account does not exist...")
                time.sleep(1.5)
                continue                                   #goes back to the start of the login/signup loop
            password = input("Enter Your Password: ")
            try_count = 0
            while password != users[username]["password"]:          #if the password is incorrect
                print("\nIncorrect Password...")
                time.sleep(1.5)
                try_count += 1                                                       #counter to limit the number of tries
                if try_count == 3:                                                   #after 3 failed attempts the login is aborted
                    print("\nToo many failed attempts. Returning to main menu...")
                    time.sleep(1.5)
                    break                                                           #breaks out of the password while loop and goes back to the start of the login/signup loop
                password = input("\nEnter Your Password: ")
            if password == users[username]["password"]:             #if the password is correct
                print("\nWelcome Back!")
                time.sleep(1.5)
                print("Loading Data...")
                date_of_birth = users[username]["date_of_birth"]      #loads the user date of birth
                favourite_artist = users[username].get("artist", "")  #loads the user's fav artist, if it does not exist it creates an empty string
                favourite_genre = users[username].get("genre", "")    #loads the user's fav genre, if it does not exist it creates an empty string
                playlists = users[username].get("playlists", {})      #gets the playlists dictionary for that user, if it does not exist it creates an empty one
                time.sleep(1.5)
                break

def main_menu():   #------------------------------ Main Menu --------------------------

    print("\n-- OCRTunes --")
    print("\n1 : View Profile")
    print("2 : Edit Profile")
    print("3 : View Song Library")
    print("4 : Create A Playlist")
    print("5 : View And Edit Playlists")
    print("6 : Save Songs")
    print("E : Exit")
    choice = input("\nChoice --> ")               #main menu function that prints the options and takes the input
    return choice                                 #returns the choice to be used in the main program

def view_profile():   #------------------------------ View Profile --------------------------

    while True:
        print("\n-- Profile --")
        print(f"\nUsername: {username}")
        print(f"Date of birth: {date_of_birth}")
        print(f"Favourite artist: {favourite_artist}")
        print(f"Favourite genre: {favourite_genre}")
        print("\nE : Exit")
        choice = input("\nChoice --> ")
        if choice.lower() == "e":
            return                          #returns back outside the function, where it was called
        else:
            print("\nThat's not one of the options...")
            time.sleep(1.5)
            continue                        #if input is not e the function is called again

def edit_profile():   #------------------------------ Edit Profile --------------------------

    while True:
        global favourite_artist, favourite_genre                                #these variables are global so they can be changed in the function
        print("\n-- Edit Profile --")
        print("\nWhat would you like to change?")
        print("\n1 : Favourite artist")
        print("2 : Favourite genre")
        print("\nE : Exit")
        choice = input("\nChoice --> ")
        if choice == "1":                                                       #if the user wants to change their favourite artist
            favourite_artist = input("\nWho is your new favourite artist?: ")
            with open("users.json", "r") as users_json:
                users = json.load(users_json)                         #opens the json file in read mode and loads it into a dictionary
            
            users[username]["artist"] = favourite_artist              #updates the users dictionary with the new favourite artist
            
            with open("users.json", "w") as users_json:
                json.dump(users, users_json, indent = 4)              #opens the json file in write mode and dumps the updated users dictionary into it
            print("Changed Successfully")
            time.sleep(1.5)
            continue                                                            #Goes back to the start of the function
        elif choice == "2":                                                     #if the user wants to change their favourite genre
            favourite_genre = input("\nWhat is your new favourite genre?: ")
            with open("users.json", "r") as users_json:
                users = json.load(users_json)                    #opens the json file in read mode and loads it into a dictionary
            
            users[username]["genre"] = favourite_genre           #updates the users dictionary with the new favourite genre
            
            with open("users.json", "w") as users_json:         #opens the json file in write mode and dumps the updated users dictionary into it
                json.dump(users, users_json, indent = 4)            
            print("Changed Successfully")
            time.sleep(1.5)
            continue
        elif choice.lower() == "e":          
            return
        else:
            print("\nThat's not one of the options...")
            time.sleep(1.5)
            continue

def view_song_library():   #------------------------------ View Song Library --------------------------

    while True:    
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
            continue                                                  #if input is not e the function goes back to the start

def create_playlist():   #------------------------------ Create A Playlist --------------------------

    while True:
        global playlists
        print("\n-- Create A Playlist --")
        print("\n1 : Create Via Time Limit")
        print("2 : Create Via Genre")
        print("3 : Create Via Added Songs")
        print("\nE : Exit")
        choice = input("\nChoice --> ")
        
        if choice == "1":                                              #option to create a playlist via time limit

            print("\n-- Create Playlist With Time Limit --")
            playlist_name = input("\nName of the playlist: ")          #takes the name of the playlist
            while playlist_name in playlists.keys():                   #checks if that name already exists in the playlists dictionary
                print("\nThis Playlist Already exists...")
                time.sleep(1.5)
                playlist_name = input("\nName of the playlist: ")
            
            while True:
                try:
                    playlist_time_limit_s = int(input("Length of the playlist in minutes: ")) * 60
                    break
                except ValueError:
                    print("\nPlease enter a valid number...")
                    time.sleep(1.5)

            min_length = min(convert_length_s([song["length"]]) for song in song_library)               #finds the shortest song in the library and converts it to seconds
            max_length = convert_length_s([song["length"] for song in song_library])                    #finds the total length of all songs in the library and converts it to seconds
            while playlist_time_limit_s <= min_length or playlist_time_limit_s > max_length:           #checks if the input works
                print("\nPlaylist cannot be made...")
                time.sleep(1.5)

                while True:
                    try:
                        playlist_time_limit_s = int(input("Length of the playlist in minutes: ")) * 60
                        break
                    except ValueError:
                        print("\nPlease enter a valid number...")
                        time.sleep(1.5)

            playlist_songs = []                                                                     #creates an empty list to store the songs that will be in the playlist
            playlist_length_s = 0                                                                   #counter for the length of the playlist in seconds
            while playlist_length_s < playlist_time_limit_s:                                        #while the length of the playlist is less than the time limit
                temp_song = random.choice(song_library)                                             #randomly selects a song from the library
                if temp_song not in playlist_songs:                                                 #checks if that song is already in the playlist...
                    temp_length = playlist_length_s + convert_length_s([temp_song["length"]])       #... if it is, calculates the length of the playlist if that song was added
                    if temp_length <= playlist_time_limit_s:                                        #if that length is less than the time limit...
                        playlist_songs.append(temp_song)                                            #...the song is added to the playlist...
                        playlist_length_s = temp_length                                             #...and the length counter is updated
                    else:                                                              #if the length is more than the time limit...
                        break                                                          #...the loop is broken
            playlists.update({playlist_name : {"songs" : playlist_songs , "length" : f"{playlist_length_s // 60}:{playlist_length_s % 60:02d}" , "num_songs" : int(len(playlist_songs))}})     #updates the playlists dictionary with a new playlist, with the key for it being its name
            save_json_playlist()
            print("\nCreated Successfully")
            time.sleep(1.5)
            continue                #goes back to the start of the function

        elif choice == "2":
            print()
            continue

        elif choice == "3":
            print()
            continue

        elif choice.lower() == "e":
            return

def view_delete_playlists():   #------------------------------ View And Delete Playlists --------------------------

    while True:
        global playlists
        print("\n-- View And Delete Playlists --")
        if not playlists:                                     #checks if there are any playlists
            print("\nYou have no playlists!")                 
        else:                                                 #if there are playlists
            print("\nHere are all your playlists")
            print("Type its name if you wish to view it")
            print("")
            for playlist in playlists:                        #a loop to go through all the playlists in the playlists dictionary
                print(f"{playlist} : View Or Delete")         #lists all the playlists that exist
                time.sleep(0.1)
        print("\nE : Exit")
        choice = input("\nChoice --> ")
        playlist_title = choice                               #the title is stored in playlist_title to be used later as choice changes

        if playlist_title in playlists.keys():                #if the input is one of the existing playlists

            print(f"\n-- {playlist_title} --")
            time.sleep(0.5)
            print(f"\nLength: {playlists[playlist_title]['length']} minutes")          #prints the length
            print(f"Number Of Songs: {playlists[playlist_title]['num_songs']}")        #prints the number of songs
            time.sleep(0.5)
            print("\nSongs:")
            time.sleep(0.5)
            print("")
            for song in playlists[playlist_title]['songs']:                            #a loop to list all the songs that are in the playlist
                print(f"{song['title']} by {song['artist']} - {song['length']}")       #prints the relevant information for each song
                time.sleep(0.1)
            print("\n1 : Delete This Playlist")
            print("\nE : Exit")
            choice = input("\nChoice --> ")

            if choice == "1":                                    #option to delete a playlist

                print("\n-- Deleting A Playlist --")
                print("\nAre You Sure?")                         #double checks with the user
                print("\n1 : Yes")
                print("2 : No")
                choice = input("\nChoice --> ")
                if choice == "1":
                    playlists.pop(playlist_title)                #deletes that playlist
                    save_json_playlist()
                    print("\nDeletion Succcessful")              #goes to the previous menu as that playlist does not exist anymore
                    time.sleep(1.5)
                    continue
                elif choice == "2":                              #cancels the deletion 
                    print("\nDeletion Aborted")
                    time.sleep(1.5)
                    continue                     #goes back to the start of the function
                else:
                    print("\nThat's not one of the options... Deletion Aborted")     #if the input is not 1 or 2 the deletion is aborted
                    time.sleep(1.5)
                    continue

            elif choice.lower() == "e":                        #exit the playlist menu
                continue

            else:                                              #if the input is not one of the options
                print("\nThat's not one of the options...")
                time.sleep(1.5)
                continue

        elif choice.lower() == "e":              #exit the playlist menu
            return

def save_songs():   #------------------------------ Save Songs --------------------------

    while True:
        print("\n-- Save An Artist's Songs --")
        print("\nType the name of the artist whose songs you wish to save to a file")
        print("Here are all the artists in the song library:")
        print("")
        artists = {song["artist"] for song in song_library}        #creates a set of all the artists in the song library, sets automatically remove duplicates

        for name in artists:               #a loop to go through all the artists in the set
            print(f"- {name}")
        print("\nE : Exit")
        choice = input("\nChoice --> ")
        artist_name = choice               #the name is stored in artist_name to be used later as choice changes

        if artist_name in artists:         #if the input is one of the existing artists

            print("\n-- File Creation --")       
            print("\nThe current file WILL BE OVERWRITTEN, continue?")   #double checks
            print("\n1 : Yes")
            print("2 : No")
            choice = input("\nChoice --> ")
            if choice == "2":                                            #cancels the file creation for 2
                print("\nAborted...")
                time.sleep(1.5)
                continue
            elif choice != "2" and choice != "1":                        #cancels everything else other than 1      
                print("\nThat's not one of the options... Aborted")
                time.sleep(1.5)
                continue

            try:                                         #tries to create a new file
                export = open("export.txt", "x")
            except FileExistsError:                      #if the file already exists it opens it in write mode
                export = open("export.txt", "w")

            export.write(f"-- {artist_name} --\n\n")                                                 #writes the artist name as a title in the file
            for songs in [song for song in song_library if song["artist"] == artist_name]:           #a loop to go through all the songs in the library that match the input artist
                export.write(f"{songs['title']} - {songs['genre']} - {songs['length']} minutes\n")   #writes the information for each song in the file

            export.close()                           #closes the file
            print("\nFile Creation Successful")      #informs the user that the file was created
            time.sleep(1.5)
            continue                                 #goes back to the start of the function                          
        
        elif choice.lower() == "e":
            return
        
        else:                                                 #if the input is not one of the options
            print("\nThat's not one of the options...")
            time.sleep(1.5)
            continue

def exit_program():   #------------------------------ Exit Program --------------------------

    save_json_playlist()
    print(f"\nBuh Bye {username}!\n")     #says bye to the user using their username
    return

def save_json_playlist():   #------------------------------- Save Playlists To JSON --------------------------

    with open("users.json", "r") as users_json:
        users = json.load(users_json)                #opens the json file in read mode and loads it into a dictionary
            
    users[username]["playlists"] = playlists         #updates the users dictionary with the new playlists dictionary
            
    with open("users.json", "w") as users_json:     
        json.dump(users, users_json, indent = 4)     #opens the json file in write mode and dumps the updated users dictionary into it


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


startup()       #runs the startup function to get user details

choice = main_menu()   # ---------------- Start of the main menu loop ----------------

while True:
    if choice == "1":

        view_profile()
        choice = main_menu()          #after the function is done, the main menu function is used again to get a new choice

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

    elif choice.lower() == "e":

        exit_program()               #runs any exit code before breaking the loop
        break
        
    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)
        choice = main_menu()         #if the input is not one of the options main_menu() is repeated



####################################### Notes #######################################

# Continue will always go back to the start of the loop it is in, break will exit the loop it is in (with exceptions)
# True loops are used so the memory does not get overloaded with function calls
# globals are used to changes variables in functions
# classes could be used, a bit too complicated for my liking
# functions make edits easier and cleaner
# Placeholders are being used
# try excepts are used to prevent crashes
