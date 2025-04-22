# Unit Tests for Track Library Management System
# Tests cover loading, listing, and managing music tracks from CSV file
# Includes tests for track information retrieval, rating management, and play count tracking

import pytest
import track_library as lib
import csv
import os

def test_load_library():
    """Test loading library from CSV"""
    lib.load_library("music.csv")
    assert len(lib.library) > 0  # Check if library is loaded
    assert lib.get_name("01") == "Smells Like Teen Spirit"
    assert lib.get_artist("01") == "Nirvana"
    assert lib.get_rating("01") == 5  # Rating 6 should be converted to 5

def test_list_all():
    """Test list_all() output format"""
    lib.load_library("music.csv")
    output = lib.list_all()
    assert "01\tSmells Like Teen Spirit\tNirvana\t⭐⭐⭐⭐⭐\t0" in output
    assert "02\tUptown Funk\tBruno Mars\t⭐⭐⭐⭐\t0" in output

def test_get_methods():
    """Test all getter methods"""
    lib.load_library("music.csv")
    assert lib.get_name("01") == "Smells Like Teen Spirit"
    assert lib.get_artist("01") == "Nirvana"
    assert lib.get_rating("01") == 5
    assert lib.get_play_count("01") == 0
    assert lib.get_name("99") is None  # Non-existent ID

def test_set_rating():
    """Test updating track rating"""
    lib.load_library("music.csv")
    lib.set_rating("01", 2)
    assert lib.get_rating("01") == 2
    # Verify unchanged play count
    assert lib.get_play_count("01") == 0

def test_increment_play_count():
    """Test play count increment"""
    lib.load_library("music.csv")
    lib.increment_play_count("01")
    assert lib.get_play_count("01") == 1
    lib.increment_play_count("01")
    assert lib.get_play_count("01") == 2

def test_nonexistent_track_operations():
    """Test operations on non-existent tracks"""
    lib.load_library("music.csv")
    # Should not raise errors but return default values
    assert lib.get_name("99") is None
    assert lib.get_play_count("99") == -1
    # These should silently fail (no exception)
    lib.set_rating("99", 3)
    lib.increment_play_count("99")

def test_file_not_found():
    """Test handling of missing CSV file"""
    with pytest.raises(FileNotFoundError):
        lib.load_library("nonexistent.csv")

def test_track_information():
    """Test getting information of specific tracks"""
    lib.load_library("music.csv")

    assert lib.get_name("01") == "Smells Like Teen Spirit"
    assert lib.get_artist("01") == "Nirvana"
    assert lib.get_rating("01") == 5
    assert lib.get_play_count("01") == 0
    

def test_track_rating_conversion():
    """Test rating conversion for different values"""
    lib.load_library("music.csv")
    
    # Test rating above 5 (should be converted to 5)
    assert lib.get_rating("01") == 5  # Original rating is 6
    
    # Test rating below 0 (should be converted to 0)
    assert lib.get_rating("43") == 0  #  Original rating is -1

def test_track_duplicates():
    """Test handling of duplicate tracks"""
    lib.load_library("music.csv")
    
    # Test tracks with same name but different artists
    assert lib.get_name("09") == "Bad Guy"
    assert lib.get_artist("09") == "Billie Eilish"
    assert lib.get_rating("09") == 3
    
    assert lib.get_name("35") == "bad guy"
    assert lib.get_artist("35") == "Billie Eilish"
    assert lib.get_rating("35") == 4
    
    # Test multiple tracks with same name and artist
    assert lib.get_name("43") == "Epilogue"
    assert lib.get_artist("43") == "YOASOBI"
    assert lib.get_rating("43") == 0
    
    assert lib.get_name("44") == "Epilogue"
    assert lib.get_artist("44") == "YOASOBI"
    assert lib.get_rating("44") == 1