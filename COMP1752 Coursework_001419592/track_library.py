# Import necessary libraries for CSV handling and track management
import csv  # For reading and writing CSV files
from library_item import LibraryItem  # Import LibraryItem class for track representation

# Initialize global library dictionary to store all tracks
library = {}

def load_library(filename="music.csv"):
    """
    Load the music library from a CSV file.
    Each track is stored as a LibraryItem object in the global library dictionary.
    
    Args:
        filename (str): The name of the CSV file to load. Defaults to "music.csv".
    
    Raises:
        FileNotFoundError: If the specified file does not exist
    """
    global library
    library.clear()  # Clear existing library
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for index, row in enumerate(reader, start=1):
                if len(row) == 3:  # Ensure row has name, artist, and rating
                    name, artist, rating = row
                    library[f"{index:02d}"] = LibraryItem(name, artist, int(rating))
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} does not exist!")

def list_all():
    """
    Generate a formatted string containing all tracks in the library.
    The string includes track ID, name, artist, rating (as stars), and play count.
    
    Returns:
        str: A formatted string containing all track information
    """
    output = ""
    for key, item in library.items():
        stars = "⭐" * item.rating  # Convert rating to stars
        output += f"{key}\t{item.name}\t{item.artist}\t{stars}\t{item.play_count}\n"
    return output

def get_name(key):
    """
    Get the name of a track by its key.
    
    Args:
        key (str): The track's unique identifier
    
    Returns:
        str: The track's name, or None if the track doesn't exist
    """
    return library[key].name if key in library else None

def get_artist(key):
    """
    Get the artist of a track by its key.
    
    """
    return library[key].artist if key in library else None

def get_rating(key):
    """
    Get the rating of a track by its key.
    
    """
    return library[key].rating if key in library else -1

def set_rating(key, rating):
    """
    Set the rating for a track.
    
    """
    if key in library:
        library[key].rating = rating

def get_play_count(key):
    """
    Get the play count of a track by its key.

    """
    return library[key].play_count if key in library else -1

def increment_play_count(key):
    """
    Increment the play count for a track.

    """
    if key in library:
        library[key].play_count += 1

# Load library when module is imported
load_library()
