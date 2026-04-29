# Import the built-in tkinter library for GUI creation
import tkinter as tk
from tkinter import ttk, messagebox

def get_user_info_from_terminal():
    """Read user personal information from the terminal with basic input validation"""
    print("===== Enter Your Personal Information =====")
    # Get full name and remove leading/trailing spaces
    full_name = input("Full Name: ").strip()
    # Age validation: ensure it's a positive integer within a reasonable range
    while True:
        try:
            age = int(input("Age: ").strip())
            if 0 < age < 150:
                break
            else:
                print("Error! Age must be a number between 1 and 149.")
        except ValueError:
            print("Error! Age must be a valid integer. Please try again.")
    # Get phone number and email
    phone_num = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    
    # Return info as a dictionary for easy GUI rendering
    return {
        "Full Name": full_name,
        "Age": f"{age} years",
        "Phone Number": phone_num,
        "Email Address": email
    }

def display_info_in_gui(user_info):
    """Create a GUI window and display the user information formatted"""
    # Initialize the main GUI window
    root = tk.Tk()
    root.title("Personal Information Dashboard")
    root.geometry("1260x300")  # Set fixed window size (width x height)
    root.resizable(False, False)  # Disable window resizing

    # Configure font style and padding for UI elements
    default_font = ("Arial", 12)
    x_pad, y_pad = 25, 18

    # Iterate through the info dict and create label pairs (label + value)
    row_index = 0
    for info_label, info_value in user_info.items():
        # Create static label for the information type (left side)
        ttk.Label(
            root, text=f"{info_label}:", font=default_font, anchor="w"
        ).grid(
            row=row_index, column=0, padx=x_pad, pady=y_pad, sticky="w"
        )
        # Create highlighted label for the information value (right side)
        ttk.Label(
            root, text=info_value, font=default_font, foreground="#0056b3", anchor="w"
        ).grid(
            row=row_index, column=1, padx=5, pady=y_pad, sticky="w"
        )
        row_index += 1

    # Add a close button to exit the GUI window
    ttk.Button(
        root, text="Close Window", command=root.quit, width=15
    ).grid(
        row=row_index, column=0, columnspan=2, pady=10
    )

    # Center the GUI window on the screen (optimization for better UX)
    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_x = (screen_width - root.winfo_width()) // 2
    window_y = (screen_height - root.winfo_height()) // 2
    root.geometry(f"+{window_x}+{window_y}")

    # Start the main GUI event loop
    root.mainloop()

# Main program execution entry
if __name__ == "__main__":
    try:
        # Step 1: Get info from terminal
        user_data = get_user_info_from_terminal()
        # Step 2: Trigger GUI display
        print("\n===== Information Read Successfully | Opening GUI Window =====")
        display_info_in_gui(user_data)
    # Handle manual program interruption (e.g., Ctrl + C in terminal)
    except KeyboardInterrupt:
        print("\nProgram terminated manually by the user.")
    # Handle other unexpected runtime errors
    except Exception as e:
        messagebox.showerror("Runtime Error", f"Program failed to run: {str(e)}")
