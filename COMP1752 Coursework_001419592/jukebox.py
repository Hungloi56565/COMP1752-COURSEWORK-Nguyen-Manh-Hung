import tkinter as tk
from tkinter import ttk, messagebox, font, filedialog
import track_library as lib
import csv
import os
from PIL import Image, ImageTk
import pygame
import time
import requests
import json
from io import BytesIO
import view_tracks
import create_track_list
import update_tracks

class JukeBox:
    def __init__(self, window):
        """
        Initialize the main JukeBox application.
        
        This class serves as the main controller for the music player application.
        It sets up the main window, initializes the audio system, and creates the UI components.
        
        Args:
            window: The root Tkinter window
        """
        # Initialize main window properties
        self.window = window
        self.window.title("Media Player")  # Set window title
        self.window.geometry("1200x700")  # Set window size
        self.window.iconbitmap("spotify.ico")  # Set window icon

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Setup custom fonts for the application
        self.setup_fonts()

        # Define constants for image display
        self.IMAGE_WIDTH = 120  # Width of album art
        self.IMAGE_HEIGHT = 120  # Height of album art

        # Create main content frame that holds all other frames
        self.main_frame = ttk.Frame(window)
        self.main_frame.pack(fill="both", expand=True)

        # Create navigation frame at the top
        nav_frame = ttk.Frame(self.main_frame)
        nav_frame.pack(fill="x", padx=10, pady=5)

        # Configure custom style for navigation buttons
        style = ttk.Style()
        style.configure('Nav.TButton',
                      padding=[15, 5],  # Add padding to buttons
                      font=('Helvetica', 10))  # Set button font

        # Create separate frames for each section of the application
        self.view_frame = ttk.Frame(self.main_frame)  # For viewing tracks
        self.playlist_frame = ttk.Frame(self.main_frame)  # For playlist management
        self.update_frame = ttk.Frame(self.main_frame)  # For library updates

        # Create navigation buttons with custom style
        self.view_btn = ttk.Button(nav_frame, text="View Tracks", command=lambda: self.show_frame(self.view_frame))
        self.view_btn.pack(side='left', padx=5)

        self.playlist_btn = ttk.Button(nav_frame, text="Playlists",command=lambda: self.show_frame(self.playlist_frame))
        self.playlist_btn.pack(side='left', padx=5)

        self.update_btn = ttk.Button(nav_frame, text="Update Library",command=lambda: self.show_frame(self.update_frame))
        self.update_btn.pack(side='left', padx=5)

        self.refresh_btn = ttk.Button(nav_frame, text="🔄 Refresh",
                                  command=self.refresh_all)
        self.refresh_btn.pack(side='left', padx=5)

        # Initialize each module with its corresponding frame
        self.view_track = view_tracks.ViewTrack(self.view_frame)  # Initialize track viewer
        self.track_list = create_track_list.TrackList(self.playlist_frame)  # Initialize playlist manager
        self.update_lib = update_tracks.Update(self.update_frame)  # Initialize library updater

        # Show the initial frame (View Tracks)
        self.show_frame(self.view_frame)

        # Load initial data
        lib.load_library()  # Load music library from CSV
        self.load_all_tracks()  # Load all tracks into the player
        self.load_playlist()  # Load playlist data

    def setup_fonts(self):
        """
        Configure custom fonts for the application.
        Sets up default font and heading font styles.
        """
        # Configure default font
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        
        # Configure heading font
        heading_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        # Apply fonts to different widget types
        self.window.option_add("*TButton*Font", default_font)
        self.window.option_add("*TLabel*Font", default_font)
        self.window.option_add("*Treeview*Font", default_font)
        self.window.option_add("*Treeview*Heading*Font", heading_font)

    def show_frame(self, frame):
        """
        Show the selected frame and hide all others.
        Updates button states to reflect current active section.
        
        Args:
            frame: The frame to show
        """
        # Hide all frames
        self.view_frame.pack_forget()
        self.playlist_frame.pack_forget()
        self.update_frame.pack_forget()

        # Show the selected frame
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Get lists of all buttons and frames
        all_buttons = [self.view_btn, self.playlist_btn, self.update_btn]
        all_frames = [self.view_frame, self.playlist_frame, self.update_frame]
        
        # Reset all buttons to normal state
        for btn in all_buttons:
            btn.state(['!pressed'])
        
        # Set the active button based on the selected frame
        current_index = all_frames.index(frame)
        all_buttons[current_index].state(['pressed'])

    def load_all_tracks(self):
        """
        Load all tracks from the library into the track list.
        This is called during initialization and when refreshing the library.
        """
        self.track_list.load_all_tracks()

    def load_playlist(self):
        """
        Load the current playlist from file.
        This is called during initialization and when refreshing the library.
        """
        self.track_list.load_playlist()

    def refresh_all(self):
        """
        Refresh all data in the application.
        Reloads library and updates all views.
        """
        # Reload library
        lib.load_library()
        
        # Update views
        self.view_track.list_tracks_clicked()  # Update view tracks
        self.track_list.load_all_tracks()      # Update playlist all tracks
        self.track_list.load_playlist()        # Update playlist selected tracks
        self.update_lib.load_data()            # Update library data

if __name__ == "__main__":
    """
    Main entry point of the application.
    Creates the root window and starts the JukeBox application.
    """
    root = tk.Tk()  # Create the root window
    app = JukeBox(root)  # Initialize the JukeBox application
    root.mainloop()  # Start the main event loop 