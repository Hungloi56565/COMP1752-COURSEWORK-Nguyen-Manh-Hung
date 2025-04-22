import tkinter as tk
from tkinter import ttk, messagebox
import track_library as lib
import csv
import os

class Update:
    """
    Class for managing and updating the music library.
    Provides functionality for adding, editing, and deleting tracks.
    """
    def __init__(self, parent):
        """
        Initialize the Update class for managing the music library.

        """
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        """
        Create and configure the library update interface.
        Sets up input fields, track list, and control buttons.
        """
        # Create entry frame for track information input
        entry_frame = ttk.Frame(self.parent)
        entry_frame.pack(fill="x", padx=5, pady=5)

        # Create labels and entry fields for track information
        ttk.Label(entry_frame, text="Track Name:").grid(row=0, column=0, padx=5)
        self.name_entry = ttk.Entry(entry_frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(entry_frame, text="Artist:").grid(row=0, column=2, padx=5)
        self.artist_entry = ttk.Entry(entry_frame, width=25)
        self.artist_entry.grid(row=0, column=3, padx=5)

        ttk.Label(entry_frame, text="Rating:").grid(row=0, column=4, padx=5)
        self.rating_entry = ttk.Entry(entry_frame, width=5)
        self.rating_entry.grid(row=0, column=5, padx=5)

        # Create control buttons
        ttk.Button(entry_frame, text="➕ Add Track", command=self.add_track).grid(row=0, column=6, padx=5)
        ttk.Button(entry_frame, text="💾 Save Changes", command=self.save_to_csv).grid(row=0, column=7, padx=5)
        ttk.Button(entry_frame, text="🗑 Delete Selected", command=self.delete_selected_tracks).grid(row=0, column=8, padx=5)

        # Create treeview for displaying and editing tracks
        self.update_tree = ttk.Treeview(self.parent, columns=("ID", "Name", "Artist", "Rating"), show="headings")
        for col in ("ID", "Name", "Artist", "Rating"):
            self.update_tree.heading(col, text=col)
            self.update_tree.column(col, width=150, anchor="center")
        self.update_tree.pack(fill="both", expand=True, padx=5, pady=5)
        self.update_tree.bind("<Double-1>", self.on_double_click)
        
        # Enable multiple selection in treeview
        self.update_tree.configure(selectmode="extended")

        self.load_data()

    def delete_selected_tracks(self):
        """
        Delete selected tracks from the library and their associated images.
        Prompts for confirmation before deletion.
        """
        selected_items = self.update_tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select tracks to delete")
            return

        # Confirm deletion
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {len(selected_items)} track(s)?"):
            # Delete selected items and their images
            for item in selected_items:
                track_id = self.update_tree.item(item)["values"][0]  # Get track ID
                # Delete image file if it exists
                image_path = f"images/{track_id}.gif"
                if os.path.exists(image_path):
                    try:
                        os.remove(image_path)
                    except Exception as e:
                        messagebox.showwarning("Warning", f"Could not delete image for track {track_id}: {str(e)}")
                # Delete track from treeview
                self.update_tree.delete(item)
            
            # Update IDs to maintain sequential order
            self.update_track_ids()
            
            messagebox.showinfo("Success", f"Successfully deleted {len(selected_items)} track(s)")

    def update_track_ids(self):
        """
        Update track IDs to maintain sequential order after deletions.
        Also renames image files to match new track IDs.
        """
        # Get all items and update their IDs
        items = self.update_tree.get_children()
        for idx, item in enumerate(items, 1):
            old_id = self.update_tree.item(item)["values"][0]  # Get old ID
            new_id = f"{idx:02d}"  # New ID
            
            # Rename image file if it exists
            old_image_path = f"images/{old_id}.gif"
            new_image_path = f"images/{new_id}.gif"
            if os.path.exists(old_image_path):
                try:
                    os.rename(old_image_path, new_image_path)
                except Exception as e:
                    messagebox.showwarning("Warning", f"Could not rename image from {old_id} to {new_id}: {str(e)}")
            
            # Update track ID in treeview
            values = list(self.update_tree.item(item)["values"])
            values[0] = new_id
            self.update_tree.item(item, values=values)

    def save_to_csv(self):
        """
        Save the current library state to a CSV file.
        Updates the track library after saving.
        """
        try:
            with open("music.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "artist", "rating"])
                for child in self.update_tree.get_children():
                    values = self.update_tree.item(child)["values"]
                    name, artist, rating = values[1], values[2], values[3]
                    writer.writerow([name, artist, rating])
            messagebox.showinfo("Success", "Data saved successfully to music.csv")
            lib.load_library()  # Reload library after saving
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def on_double_click(self, event):
        """
        Handle double-click events for inline editing of track information.
        Allows editing of track name, artist, and rating directly in the treeview.
        
        """
        region = self.update_tree.identify("region", event.x, event.y)
        if region != "cell":
            return
        row_id = self.update_tree.identify_row(event.y)
        column = self.update_tree.identify_column(event.x)
        column_index = int(column.replace("#", "")) - 1

        if column_index == 0:  # prevent editing ID
            return

        item = self.update_tree.item(row_id)
        old_value = item["values"][column_index]

        # Create entry widget for editing
        entry = ttk.Entry(self.update_tree)
        entry.insert(0, old_value)
        entry.focus()
        entry.place(x=event.x_root - self.update_tree.winfo_rootx(),
                    y=event.y_root - self.update_tree.winfo_rooty(),
                    width=150)

        def save_edit(event):
            """
            Save the edited value and update the treeview.
            
            """
            new_value = entry.get()
            values = list(self.update_tree.item(row_id)["values"])

            # Validate rating if editing rating column
            if column_index == 3:  # Rating column
                try:
                    rating_val = int(new_value)
                    if rating_val < 0 or rating_val > 5:
                        messagebox.showwarning("Input Error", "Rating must be between 0 and 5 stars.")
                        entry.destroy()
                        return
                except ValueError:
                    messagebox.showwarning("Input Error", "Rating must be a number between 0 and 5.")
                    entry.destroy()
                    return

            values[column_index] = new_value
            self.update_tree.item(row_id, values=values)
            entry.destroy()

        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", lambda e: entry.destroy())

    def load_data(self):
        """
        Load track data from the CSV file into the treeview.
        """
        self.update_tree.delete(*self.update_tree.get_children())
        if os.path.exists("music.csv"):
            with open("music.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)  # skip header
                for idx, row in enumerate(reader, start=1):
                    if len(row) >= 3:
                        self.update_tree.insert("", "end", values=(f"{idx:02d}", row[0], row[1], row[2]))

    def add_track(self):
        """
        Add a new track to the library.
        Validates input and checks for duplicates.
        """
        name = self.name_entry.get().strip()
        artist = self.artist_entry.get().strip()
        rating = self.rating_entry.get().strip() or "0"

        if not name or not artist:
            messagebox.showwarning("Input Error", "Track name and artist cannot be empty.")
            return

        try:
            # Validate rating
            rating_val = int(rating)
            if rating_val < 0 or rating_val > 5:
                messagebox.showwarning("Input Error", "Rating must be between 0 and 5 stars.")
                return
        except ValueError:
            messagebox.showwarning("Input Error", "Rating must be a number between 0 and 5.")
            return

        # Check for duplicate (same name and artist)
        for child in self.update_tree.get_children():
            values = self.update_tree.item(child)["values"]
            if name.lower() == str(values[1]).lower() and artist.lower() == str(values[2]).lower():
                answer = messagebox.askyesno("Duplicate", 
                    f"The track '{name}' by '{artist}' already exists.\nDo you still want to add it?")
                if not answer:
                    return
                break

        # Add new track with sequential ID
        new_id = f"{len(self.update_tree.get_children()) + 1:02d}"
        self.update_tree.insert("", "end", values=(new_id, name, artist, rating))
        
        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.artist_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

    def refresh_list(self):
        """
        Refresh the track list by reloading the library and updating the view.
        """
        lib.load_library()  # Reload library
        self.load_data()  # Update the view
        messagebox.showinfo("Success", "Track list refreshed successfully") 