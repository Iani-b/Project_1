import time  #library to add a timer so text is not instantly skipped
import random

def title_func(song):                                   #this is essentialy a function that will be used to sort the dictionaries within the list. The inputs are the dicts...
    return song["title"]                                #...and the outputs are the titles of the songs for each dict

def remove_dupes(my_list):                  #this removes dictionary duplicates from a list
    no_dupes_set = set()                    #a set is defined
    no_dupes = []                           #a list is defined
    for d in my_list:                       #this goes through every dictionary in the list
        pair_set = frozenset(d.items())     #frozen sets are immutable, therfore hashable so it can be added to a set. d.items looks at every key:value pair and returns an object, which can be made into a frozen set 
        no_dupes_set.add(pair_set)          #this adds teh frozen set to our initial set
    for s in no_dupes_set:                  #this goes through every frozen set in the set (There cannot be duplicates)
        no_dupes.append(dict(s))            #it then adds the dictionary key:value pair back to the list
    return no_dupes


def convert_length_s(items):                                             #function to add song times and return back a string, a LIST of STRINGS is needed
    total_seconds = 0                                                    #counter is set to 0
    for string in items:
        minutes, seconds = string.split(":")                             #the minutes and seconds are split at the : and placed into the corresponding variable (unpacking)
        total_seconds = total_seconds + int(seconds) + int(minutes)*60   #total seconds are added for each song length that is went through
    return total_seconds                                                 #total seconds are returned

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

while True:                           #While True loop keeps the section running until explicitly quit
    print("\n-- OCRTunes --")         #\n is use d to move onto the next line, I find it easier
    print("\n1 : View Profile")
    print("2 : Edit Profile")
    print("3 : View Song Library")
    print("4 : Create A Playlist")
    print("5 : View And Edit Playlists")
    print("6 : Save Songs")
    print("E : Exit")
    choice = input("\nChoice --> ")            #Asks the user to which menu they want to go to and sets that as the choice

    if choice == "1":                          #First menu for details

        while True:                            #kept running until quit
            print("\n-- Profile --")
            print(f"\nUsername: {username}")                  #f statments just to make everything look a lot cleaner
            print(f"Date of birth: {date_of_birth}")
            print(f"Favourite artist: {favourite_artist}")
            print(f"Favourite genre: {favourite_genre}")
            print("\nE : Exit")
            choice = input("\nChoice --> ")
            if choice.lower() == "e":               #doesnt matter if e is capital or not
                break                                        #breaks the inner loop, so it goes to the previous menu
            else:                                             #random inputs, will return saying you did something wrong
                print("\nThat's not one of the options...")
                time.sleep(1.5)                                 #waits a bit so you can read about how you cant type to save your life

    elif choice == "2":                               #second menu to change details

        while True:
            print("\n-- Edit Profile --")
            print("\nWhat would you like to change?")
            print("\n1 : Favourite artist")
            print("2 : Favourite genre")
            print("\nE : Exit")
            choice = input("\nChoice --> ")             #decides what is going to be changed

            if choice == "1":                           #menu to change the favourite artist

                favourite_artist = input("\nWho is your new favourite artist?: ")        #basic input for the variable
                print("Changed Successfully")                                            #not really needed but looks nice
                time.sleep(1.5)                                                          #gives you time to read the nice looking text

            elif choice == "2":                                                          #menu to change favourite genre    

                favourite_genre = input("\nWhat is your new favourite genre?: ")         #basic input
                print("Changed Successfully")                                            #fancy text
                time.sleep(1.5)                          #time for the fancy text

            elif choice.lower() == "e":          
                    break                                 #back to the main menu           
            else:
                print("\nThat's not one of the options...")            #whoopsie daisy
                time.sleep(1.5)                                        #admire the dismissive text for a whole 1.5 seconds

    elif choice == "3":           #the menu for the song library

        while True:
            print("\n-- Song Library --")
            print("")
            sorted_songs = sorted(song_library, key = title_func)                    #key requires a function which I defined before. Every dictionary in song_library (input) is sorted using the titles of the songs (output) for which the key states (so song_library[0 to 19] are sorted in alphabetical order of song_library[0 to 19]["title"] hence the function). Found on https://www.w3schools.com/python/ref_func_sorted.asp very helpful.
            for song in sorted_songs:                                                #this for statement will then go through every dictionary within the sorted list in order...
                print(f"{song['title']} by {song['artist']} - {song['length']}")     #...and print the relevant information using f statements for each loop (dictionary)
                time.sleep(0.1)
            print("\nE : Exit")
            choice = input("\nChoice --> ")                                        #realistically only one choice

            if choice.lower() == "e":
                break                                                              #goes back to the main menu

            else:
                print("\nThat's not one of the options...")
                time.sleep(1.5)

    elif choice == "4":                                    #choice for creating a list

        while True:
            print("\n-- Create A Playlist --")
            print("\n1 : Create Via Time Limit")
            print("2 : Create Via Genre")
            print("3 : Create Via Added Songs")
            print("\nE : Exit")
            choice = input("\nChoice --> ")

            if choice == "1":

                print("\n-- Create Playlist With Time Limit --")
                playlist_name = input("\nName of the playlist: ")                                           #gets the playlist name
                while playlist_name in playlists.keys():                                                    #checks if it already exists
                    print("\nThis Playlist Already exists...")
                    time.sleep(1.5)
                    playlist_name = input("\nName of the playlist: ")
                playlist_time_limit_s = int(input("Length of the playlist in minutes: ")) * 60             #gets the requested length of the playlist in seconds
                while playlist_time_limit_s <= 185 or playlist_time_limit_s >= 693:                       #checks if playlist length is between shortest (3:05) and longest (11:33) song
                    print("\nPlaylist length must be between 3:05 and 11:33 minutes...")
                    time.sleep(1.5)
                    playlist_time_limit_s = int(input("\nLength of the playlist in minutes: ")) * 60
                playlist_songs = []                                                                    #initial empty list for the songs
                playlist_length_s = 0                                                                        #initial length of the playlist (in seconds)
                while playlist_length_s < playlist_time_limit_s:                                             #repeats until the time requirements have been met
                    playlist_songs.append(random.choice(song_library))                                       #adds a random song from the library
                    playlist_songs = remove_dupes(playlist_songs)                                            #removes any duplicates
                    song_times = [times["length"] for times in playlist_songs]                               #adds all the lengths of the songs to a seperate list
                    playlist_length_s = convert_length_s(song_times)                                         #converts the list of strings to the duration in seconds
                playlist_songs.pop()                                                      #removes the last song that caused it to go over
                song_times = [times["length"] for times in playlist_songs]                #recalculates the time taken
                playlist_length_s = convert_length_s(song_times)                          #converts
                playlists.update({playlist_name : {"songs" : playlist_songs , "length" : f"{playlist_length_s // 60}:{playlist_length_s % 60}" , "num_songs" : int(len(playlist_songs))}})     #updates the playlists dictionary with a new playlist with the key for it being its name
                print("\nCreated Successfully")
                time.sleep(1.5)

            elif choice == "2":
                
                print()

            elif choice == "3":

                print()

            elif choice.lower() == "e":                             #exits the create playlists menu
                break

            else:
                print("\nThat's not one of the options...")
                time.sleep(1.5)

    elif choice == "5":                                             #the menu for viewing and deleting playlists
        
        while True:
            print("\n-- View And Edit Playlists --")
            if not playlists:                                       #checks if there are any playlists
                print("\nYou have no playlists!")
            else:
                print("")
                for playlist in playlists:
                    print(f"{playlist} : View Or Edit")
                print("\nHere are all your playlists")
                print("Type it's name if you wish to view it")
            print("\nE : Exit")
            choice = input("\nChoice --> ")

            if choice in playlists.keys():                          #creates a menu based on the playlist that was chosen

                playlist_title = choice                             #stores the playlist title as choice can change
                while True:
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
                            break

                        elif choice == "2":                              #cancels the deletion

                            print("\nDeletion Aborted")
                            time.sleep(1.5)
                            
                        else:                                                                #brings the user back to  the playlist menu to make sure no accidents happen
                            print("\nThat's not one of the options... Deletion Aborted")
                            time.sleep(1.5)

                    elif choice.lower() == "e":                        #exit the playlist menu
                        break
                    
                    else:
                        print("\nThat's not one of the options...")
                        time.sleep(1.5)

            elif choice.lower() == "e":                             #exit  
                break 

    elif choice == "6":
        break

    elif choice.lower() == "e":               #input for choice to exit
        print(f"\nBuh Bye {username}!\n")     #says bye to the user
        break                                 #breaks the outermost while loop, ending the code

    else:
        print("\nThat's not one of the options...")
        time.sleep(1.5)

#not done yet also testing git