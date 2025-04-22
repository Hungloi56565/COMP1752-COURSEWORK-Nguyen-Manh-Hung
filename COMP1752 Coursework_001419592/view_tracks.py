import tkinter as tk
from tkinter import ttk, messagebox
import track_library as lib
from PIL import Image, ImageTk
import os
import csv

class ViewTrack:
    """
    Class for viewing and managing tracks in the music library.
    Provides functionality for searching, viewing, and playing tracks.
    """
    def __init__(self, parent):
        """
        Initialize the ViewTrack class for viewing and managing tracks.
        
        Args:
            parent: The parent widget where this component will be placed
        """
        self.parent = parent
        self.setup_ui()  # Set up the user interface
        
    def setup_ui(self):
        """
        Create and configure the track viewing interface.
        Sets up search controls, track list display, and track details panel.
        """
        # Create search frame with controls
        search_frame = ttk.Frame(self.parent)
        search_frame.pack(fill="x", padx=5, pady=5)

        # Create search entry field
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, width=30, textvariable=self.search_var)
        self.search_entry.pack(side="left", padx=5)

        # Create radio buttons for search type selection
        self.search_type = tk.StringVar(value="name")
        ttk.Radiobutton(search_frame, text="Search by Name", variable=self.search_type, value="name").pack(side="left", padx=5)
        ttk.Radiobutton(search_frame, text="Search by Artist", variable=self.search_type, value="artist").pack(side="left", padx=5)

        # Create search button
        ttk.Button(search_frame, text="Search", command=self.search_tracks).pack(side="left", padx=5)

        # Create track ID frame for direct track access
        track_id_frame = ttk.Frame(self.parent)
        track_id_frame.pack(fill="x", padx=5, pady=5)

        # Create track ID entry and control buttons
        ttk.Label(track_id_frame, text="Track ID:").pack(side="left", padx=5)
        self.track_id_entry = ttk.Entry(track_id_frame, width=10)
        self.track_id_entry.pack(side="left", padx=5)

        # Create action buttons
        ttk.Button(track_id_frame, text="View Track", command=self.view_track).pack(side="left", padx=5)
        ttk.Button(track_id_frame, text="List All", command=self.list_tracks_clicked).pack(side="left", padx=5)
        ttk.Button(track_id_frame, text="Play", command=self.play_track).pack(side="left", padx=5)
        ttk.Button(track_id_frame, text="Save", command=self.save_track).pack(side="left", padx=5)

        # Create treeview for displaying tracks
        self.view_tree = ttk.Treeview(self.parent, columns=("ID", "Name", "Artist", "Rating", "Plays"), show="headings")

        # Configure columns
        self.view_tree.heading("ID", text="ID")
        self.view_tree.heading("Name", text="Name")
        self.view_tree.heading("Artist", text="Artist")
        self.view_tree.heading("Rating", text="Rating")
        self.view_tree.heading("Plays", text="Plays")
        
        # Configure column widths and alignment
        for col in ("ID", "Name", "Artist", "Rating", "Plays"):
            self.view_tree.column(col, width=100, anchor="center")
        
        self.view_tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.view_tree.bind("<ButtonRelease-1>", self.on_treeview_click)

        # Create details frame for track information
        details_frame = ttk.Frame(self.parent)
        details_frame.pack(fill="x", padx=5, pady=5)

        # Create text widget for track details
        self.details_text = tk.Text(details_frame, height=5, width=50)
        self.details_text.pack(side="left", fill="x", expand=True, padx=5)

        # Create label for track image
        self.image_label = ttk.Label(details_frame, width=20)
        self.image_label.pack(side="left", padx=5)

    def view_track(self):
        """
        Display details for the track specified by the track ID.
        Shows track information and associated image if available.
        """
        key = self.track_id_entry.get().strip()
        name = lib.get_name(key)
        if name:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            plays = lib.get_play_count(key)
            stars = "⭐" * int(rating)
            details = (
                f"Name:   {name}\n"
                f"Artist: {artist}\n"
                f"Rating: {stars} ({rating})\n"
                f"Plays:  {plays}"
            )
            self.load_image(key)
        else:
            details = f"Track {key} not found."
            self.image_label.config(image="", text="No image")

        self.details_text.delete("1.0", tk.END)
        self.details_text.insert(tk.END, details)

    def load_image(self, key):
        """
        Load and display the track's associated image.
        The image is resized to fit the display area while maintaining aspect ratio.

        """
        image_path = f"images/{key}.gif"
        if os.path.exists(image_path):
            # Open image with PIL
            img = Image.open(image_path)
            
            # Calculate aspect ratio
            aspect_ratio = img.width / img.height
            
            # Calculate new dimensions while maintaining aspect ratio
            if aspect_ratio > 1:  # Width is greater than height
                new_width = 120
                new_height = int(120 / aspect_ratio)
            else:  # Height is greater than width
                new_height = 120
                new_width = int(120 * aspect_ratio)
            
            # Resize image
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img, text="")
        else:
            self.image_label.config(image="", text="No image")

    def list_tracks_clicked(self):
        """
        Display all tracks in the library.
        Updates the treeview with all available tracks.
        """
        self.view_tree.delete(*self.view_tree.get_children())
        for line in lib.list_all().strip().split("\n"):
            parts = line.split("\t")
            if len(parts) == 5:
                self.view_tree.insert("", "end", values=parts)

    def on_treeview_click(self, event):
        """
        Handle click events on the track list.
        Updates the track ID entry with the selected track's ID.

        """
        selected = self.view_tree.selection()
        if selected:
            track_id = self.view_tree.item(selected, "values")[0]
            self.track_id_entry.delete(0, tk.END)
            self.track_id_entry.insert(0, track_id)
            self.view_track()

    def play_track(self):
        """
        Play the selected track and update play count.
        """
        key = self.track_id_entry.get().strip()
        if key:
            lib.increment_play_count(key)
            self.list_tracks_clicked()
            self.view_track()

    def search_tracks(self):
        """
        Search for tracks by name or artist.
        Updates the track list with matching results.
        """
        search_term = self.search_var.get().lower()
        search_type = self.search_type.get()
        
        if not search_term:
            self.list_tracks_clicked()
            return

        # Clear current view
        for i in self.view_tree.get_children():
            self.view_tree.delete(i)

        # Search through track library
        track_list = lib.list_all()
        for line in track_list.strip().split("\n"):
            parts = line.strip().split("\t")
            if len(parts) == 5:
                if search_type == "name":
                    if search_term in parts[1].lower():  # Name is at index 1
                        self.view_tree.insert("", "end", values=parts)
                else:  # search by artist
                    if search_term in parts[2].lower():  # Artist is at index 2
                        self.view_tree.insert("", "end", values=parts)

    def save_track(self):
        """
        Save the current track to the music library.
        """
        key = self.track_id_entry.get().strip()
        if not key:
            messagebox.showwarning("Warning", "Please enter a track ID")
            return

        try:
            # Check if track exists
            name = lib.get_name(key)
            if not name:
                messagebox.showerror("Error", f"Track with ID {key} not found")
                return

            # Get track details
            artist = lib.get_artist(key)
            
            # Save to music.csv
            with open("music.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([name, artist, "0"])  # Default rating of 0
            
            # Reload library
            lib.load_library()
            
            messagebox.showinfo("Success", f"Track '{name}' saved successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save track: {str(e)}")
            print(f"Error details: {str(e)}")  # Print error for debugging