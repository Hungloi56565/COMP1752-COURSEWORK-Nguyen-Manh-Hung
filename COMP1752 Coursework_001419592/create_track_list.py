import tkinter as tk
from tkinter import ttk, messagebox
import track_library as lib
import csv
import os

class TrackList:
    """
    Class for managing playlists in the music player.
    Provides functionality for creating, editing, and playing playlists.
    """
    def __init__(self, parent):
        """
        Initialize the TrackList class for playlist management.
        
        Args:
            parent: The parent widget where this component will be placed
        """
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        """
        Create and configure the playlist management interface.
        Sets up playlist selection, track lists, and control buttons.
        """
        # Playlist selection
        playlist_frame = ttk.Frame(self.parent)
        playlist_frame.pack(fill="x", padx=5, pady=5)

        ttk.Label(playlist_frame, text="Select Playlist:").pack(side="left", padx=5)
        self.playlist_var = tk.StringVar(value="list1")
        self.playlist_dropdown = ttk.Combobox(playlist_frame, textvariable=self.playlist_var, 
                                            values=["list1", "list2", "More List..."])
        self.playlist_dropdown.pack(side="left", padx=5)
        self.playlist_dropdown.bind("<<ComboboxSelected>>", self.handle_playlist_selection)

        # Main content frame
        content_frame = ttk.Frame(self.parent)
        content_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # All tracks tree
        ttk.Label(content_frame, text="All Tracks").grid(row=0, column=0, padx=5)
        self.all_tree = ttk.Treeview(content_frame, columns=("ID", "Name", "Artist", "Rating", "Plays"), show="headings")
        for col in ("ID", "Name", "Artist", "Rating", "Plays"):
            self.all_tree.heading(col, text=col)
            self.all_tree.column(col, width=100, anchor="center")
        self.all_tree.grid(row=1, column=0, sticky="nsew", padx=5)
        self.all_tree.bind("<Double-1>", self.add_to_playlist)

        # Selected tracks tree
        ttk.Label(content_frame, text="Selected Tracks").grid(row=0, column=1, padx=5)
        self.select_tree = ttk.Treeview(content_frame, columns=("ID", "Name", "Artist", "Rating", "Plays", "Play"), 
                                      show="headings")
        for col in ("ID", "Name", "Artist", "Rating", "Plays", "Play"):
            self.select_tree.heading(col, text=col)
            self.select_tree.column(col, width=100, anchor="center")
        self.select_tree.grid(row=1, column=1, sticky="nsew", padx=5)
        self.select_tree.bind("<ButtonRelease-1>", self.toggle_play_check)

        # Buttons
        button_frame = ttk.Frame(self.parent)
        button_frame.pack(fill="x", padx=5, pady=5)

        ttk.Button(button_frame, text="▶ Play Selected", command=self.play_selected).pack(side="left", padx=5)
        ttk.Button(button_frame, text="🗑 Remove Selected", command=self.remove_selected).pack(side="left", padx=5)
        ttk.Button(button_frame, text="💾 Save Playlist", command=self.save_playlist).pack(side="left", padx=5)

        # Configure grid weights
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

    def handle_playlist_selection(self, event):
        """
        Handle playlist selection from the dropdown.
        Allows creating new playlists and loading existing ones.
        
        """
        if self.playlist_var.get() == "More List...":
            new_list = tk.simpledialog.askstring("New Playlist", "Enter new playlist name:")
            if new_list:
                self.playlist_var.set(new_list)
                if new_list not in self.playlist_dropdown['values']:
                    new_values = list(self.playlist_dropdown['values'])[:-1] + [new_list, "More List..."]
                    self.playlist_dropdown['values'] = new_values
        self.load_playlist()

    def load_all_tracks(self):
        """
        Load all available tracks from the library into the all tracks treeview.
        """
        self.all_tree.delete(*self.all_tree.get_children())
        for line in lib.list_all().strip().split("\n"):
            parts = line.split("\t")
            if len(parts) == 5:
                self.all_tree.insert("", "end", values=parts)

    def load_playlist(self):
        """
        Load the selected playlist from file.
        Displays tracks in the selected tracks treeview.
        """
        self.select_tree.delete(*self.select_tree.get_children())
        filename = f"{self.playlist_var.get()}.csv"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 1 and row[0] in lib.library:
                        item = lib.library[row[0]]
                        checked = row[1] if len(row) > 1 else "1"
                        play_icon = "🎧" if checked == "1" else ""
                        self.select_tree.insert("", "end", values=(row[0], item.name, item.artist, 
                                                               "⭐" * item.rating, item.play_count, play_icon))

    def add_to_playlist(self, event):
        """
        Add selected tracks from the all tracks list to the playlist.
        Prevents duplicate tracks in the playlist.
        

        """
        selected = self.all_tree.selection()
        for sel in selected:
            data = self.all_tree.item(sel, "values")
            track_id = data[0]
            # Check for duplicates
            duplicate_found = False
            for child in self.select_tree.get_children():
                if self.select_tree.item(child, "values")[0] == track_id:
                    duplicate_found = True
                    break
            
            if duplicate_found:
                messagebox.showwarning(
                    "Duplicate Track",
                    f"Track '{data[1]}' by '{data[2]}' is already in the playlist."
                )
                continue
                
            self.select_tree.insert("", "end", values=(track_id, data[1], data[2], data[3], data[4], "🎧"))
        self.save_playlist()

    def toggle_play_check(self, event):
        """
        Toggle the play status of a track in the playlist.
        Updates the play icon in the treeview.
        

        """
        region = self.select_tree.identify_column(event.x)
        if region != "#6":  # Play column
            return
        item_id = self.select_tree.identify_row(event.y)
        if not item_id:
            return
        values = list(self.select_tree.item(item_id, "values"))
        values[5] = "" if values[5] == "🎧" else "🎧"
        self.select_tree.item(item_id, values=values)
        self.save_playlist()

    def save_playlist(self):
        """
        Save the current playlist to a CSV file.
        Stores track IDs and their play status.
        """
        filename = f"{self.playlist_var.get()}.csv"
        with open(filename, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for child in self.select_tree.get_children():
                row = self.select_tree.item(child, "values")
                writer.writerow([row[0], "1" if row[5] == "🎧" else "0"])

    def play_selected(self):
        """
        Play all selected tracks in the playlist.
        Updates play counts for played tracks.
        """
        for child in self.select_tree.get_children():
            row = self.select_tree.item(child, "values")
            if row[5] == "🎧":
                lib.increment_play_count(row[0])
        self.load_all_tracks()
        self.load_playlist()

    def remove_selected(self):
        """
        Remove selected tracks from the playlist.
        Updates the playlist file after removal.
        """
        selected_items = self.select_tree.selection()
        for item in selected_items:
            self.select_tree.delete(item)
        self.save_playlist()

    def refresh_list(self):
        """
        Refresh the playlist by reloading the library and updating the view.
        """
        lib.load_library()  # Reload library
        self.load_all_tracks()  # Update the view
        self.load_playlist()  # Reload playlist
        messagebox.showinfo("Success", "Playlist refreshed successfully") 