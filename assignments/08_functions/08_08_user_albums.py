print("a loop that allows users to enter album;s artist and title.") 
def make_album(artist_name, album_title):
    """Return a dictionary representing a music album."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    return album 
while True:
    print("\nPlease enter the artist and album title:")
    print("(enter 'q' at any time to quit)") 
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break 
    title = input("Album title: ")
    if title.lower() == 'q':
        break 
    album_info = make_album(artist, title)
    print(f"\nAlbum info: {album_info}")
# This program defines a function make_album() that creates a dictionary with artist and album title.
# It then enters a loop where it prompts the user to input artist names and album titles,
# creating and displaying the album dictionary for each entry until the user decides to quit.