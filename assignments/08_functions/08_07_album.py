print("function called make_album().") 
def make_album(artist_name, album_title, track_count=None):
    """Return a dictionary representing a music album."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if track_count:
        album['tracks'] = track_count
    return album
# Call the function with different albums and print the results
album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('the beatles', 'abbey road', 17)
album3 = make_album('taylor swift', '1989', 13)
print(album1)
print(album2)
print(album3)
# This function takes an artist's name and an album title as required parameters,
# and an optional track count parameter. It returns a dictionary containing the album information.
# The function is then called with different albums to demonstrate its usage.