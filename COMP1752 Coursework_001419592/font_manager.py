import tkinter.font as tkfont


def configure():
    """
    Configure the default fonts for the application.
    Sets up consistent font styles across all widgets.
    """
    # family = "Segoe UI"  # Alternative font option
    family = "Helvetica"  # Default font family
    
    # Configure default font for general use
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=9, family=family)
    
    # Configure text font for text widgets
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=9, family=family)
    
    # Configure fixed-width font for code and monospace text
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=9, family=family)
