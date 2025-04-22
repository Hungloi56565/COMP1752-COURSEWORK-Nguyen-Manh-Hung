# test_library_item.py
import pytest
from library_item import LibraryItem
import csv

# Test data setup
@pytest.fixture
def sample_library_item():
    # Read first track from music.csv
    with open("music.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        name, artist, rating = next(reader)
        return LibraryItem(name, artist, rating)

def test_library_item_creation(sample_library_item):
    """Test LibraryItem initialization with real data"""
    assert sample_library_item.name == "Smells Like Teen Spirit"
    assert sample_library_item.artist == "Nirvana"
    assert sample_library_item.rating == 5  # Rating 6 should be converted to 5
    assert sample_library_item.play_count == 0

def test_library_item_rating_setter(sample_library_item):
    """Test rating setter with valid values"""
    sample_library_item.rating = 5
    assert sample_library_item.rating == 5
    sample_library_item.rating = 0
    assert sample_library_item.rating == 0

def test_library_item_invalid_rating(sample_library_item):
    """Test rating validation"""
    # Test with non-integer value
    sample_library_item.rating = "invalid"  # Should be converted to 0
    assert sample_library_item.rating == 0
    
    # Test with out of range values
    sample_library_item.rating = -1  # Should be converted to 0
    assert sample_library_item.rating == 0
    
    sample_library_item.rating = 6  # Should be converted to 5
    assert sample_library_item.rating == 5

def test_library_item_play_count(sample_library_item):
    """Test play count increment"""
    sample_library_item.play_count += 1
    assert sample_library_item.play_count == 1
    sample_library_item.play_count += 5
    assert sample_library_item.play_count == 6 