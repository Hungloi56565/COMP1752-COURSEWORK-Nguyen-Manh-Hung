# Import necessary libraries
import csv

class LibraryItem:
    """
    Represents a single track in the music library.
    This class stores track information including name, artist, rating, and play count.
    """
    def __init__(self, name, artist, rating=0):
        """
        Initialize a new track with basic information.

        """
        # Initialize LibraryItem with name, artist, and rating
        self.name = name
        self.artist = artist
        self._rating = 0  # Initialize with default value
        self.rating = rating  # Use the setter to validate
        self.play_count = 0  # Track play count, initialized to 0

    @property
    def rating(self):
        """
        Get the track's rating.

        """
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        Set the track's rating with validation.
        Ensures rating is between 0 and 5.
        
        """
        try:
            value = int(value)
            if value < 0:
                self._rating = 0
            elif value > 5:
                self._rating = 5
            else:
                self._rating = value
        except (TypeError, ValueError):
            self._rating = 0  # Default to 0 for invalid inputs

# Initialize library list
library = []

# Load initial data from music.csv
try:
    with open("music.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, artist, rating = row
            library.append(LibraryItem(name, artist, rating))
except FileNotFoundError:
    print("File music.csv does not exist!")
