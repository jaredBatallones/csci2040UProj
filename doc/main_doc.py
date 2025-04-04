import tkinter as tk
from tkinter import ttk, messagebox
import databasefunction as db
import furniture
import login
from PIL import Image, ImageTk

def main():
    """
    Entry point for the Furniture Inventory & Management System (FIMS).
    Initializes the database, loads default entries, and launches the GUI.

    Responsibilities:
    - Connect to and initialize the database
    - Pre-load some furniture items if missing
    - Display a login window for staff
    - Handle authentication and transition to main menu
    """
    # Connect to test or production database
    connection, cursor = db.loadDatabase(test=True)
    db.initializeDatabase(connection, cursor)
    login.initialize_users(connection, cursor)

    # Preload two furniture items if not already in the database
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 101, "Chair", "Black", 49.99, "Medium", "A3")
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 102, "Table", "Brown", 99.99, "Large", "B1")

    # Setup the main Tkinter window
    root = tk.Tk()
    root.title("FIMS - Furniture Inventory & Management System")
    root.geometry("400x600")

    # Create login frame
    login_frame = ttk.Frame(root)
    login_frame.pack(pady=20)

    # Login input fields
    ttk.Label(login_frame, text="Staff ID:").grid(row=0, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(login_frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    pass_entry = ttk.Entry(login_frame, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def attempt_login():
        """
        Handles login authentication when the Login button is clicked.

        Parameters: None (uses values from id_entry and pass_entry fields)
        Returns:
            Transitions to the main menu if credentials are valid,
            otherwise shows an error popup.
        """
        staff_id = id_entry.get()
        password = pass_entry.get()
        user = db.attemptLogin(cursor, staff_id, password)
        if user:
            messagebox.showinfo("Login Success", f"Welcome, {user[2]}!")
            login_frame.pack_forget()
            show_main_menu(user[1])
        else:
            messagebox.showerror("Login Failed", "Wrong ID or password—try again!")

    # Login button
    ttk.Button(login_frame, text="Login", command=attempt_login).grid(row=2, column=1, pady=10)

    def show_main_menu(user_level):
        """
        Displays the main menu interface after successful login.

        Parameters:
        ----------
        user_level : int
            Access level of the logged-in user (1 = admin, 2–5 = staff).

        Behavior:
        - Dynamically renders available buttons based on user_level.
        - Organizes UI into three vertical columns (feature groups).
        - Displays access level and allows logout.
        """
        # Remove other frames if they exist
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != login_frame:
                widget.destroy()

        # Main wrapper frame with background color
        main_frame = tk.Frame(root, bg="#ADD8E6")
        main_frame.pack(pady=20, fill="both", expand=True)

        # Access level label
        access_label = tk.Label(
            main_frame,
            text=f"Access Level: {user_level}",
            bg="#ADD8E6",
            fg="black"
        )
        access_label.grid(row=0, column=0, columnspan=3, pady=5)

        # --- COLUMN LAYOUT ---

        # Column 1: Furniture actions (Orange)
        col1 = tk.Frame(main_frame, bg="#FFA500")
        col1.grid(row=1, column=0, padx=10, sticky="n")

        # Column 2: Login management (White)
        col2 = tk.Frame(main_frame, bg="#FFFFFF")
        col2.grid(row=1, column=1, padx=10, sticky="n")

        # Column 3: Image search + specific item view (Light green)
        col3 = tk.Frame(main_frame, bg="#90EE90")
        col3.grid(row=1, column=2, padx=10, sticky="n")

        # --- COLUMN 1 BUTTONS ---
        tk.Button(col1, text="View All Furniture", command=lambda: view_all(cursor), bg="#FFA500").pack(pady=5)

        if user_level <= 4:
            tk.Button(col1, text="Search Furniture", command=lambda: search_furniture(cursor), bg="#FFA500").pack(pady=5)
            tk.Button(col1, text="Sort Furniture", command=lambda: sort_furniture(cursor), bg="#FFA500").pack(pady=5)

        if user_level <= 2:
            tk.Button(col1, text="Add Furniture", command=lambda: add_furniture(connection, cursor), bg="#FFA500").pack(pady=5)
            tk.Button(col1, text="Edit Furniture", command=lambda: edit_furniture(connection, cursor), bg="#FFA500").pack(pady=5)
            tk.Button(col1, text="Remove Furniture", command=lambda: remove_furniture(connection, cursor), bg="#FFA500").pack(pady=5)

        # --- COLUMN 2 BUTTONS ---
        if user_level == 1:
            tk.Button(col2, text="View Logins", command=lambda: view_logins(cursor), bg="#FFFFFF").pack(pady=5)
            tk.Button(col2, text="Add Login", command=lambda: add_login(connection, cursor), bg="#FFFFFF").pack(pady=5)
            tk.Button(col2, text="Delete Login", command=lambda: delete_login(connection, cursor), bg="#FFFFFF").pack(pady=5)

        # --- COLUMN 3 BUTTONS ---
        tk.Button(col3, text="Search by Picture", command=search_by_picture, bg="#90EE90").pack(pady=5)
        tk.Button(col3, text="View Specific Furniture", command=lambda: view_specific(cursor), bg="#90EE90").pack(pady=5)

        # --- LOGOUT BUTTON ---
        tk.Button(
            main_frame,
            text="Log Out",
            command=lambda: log_out(root, login_frame, main_frame),
            bg="#FF0000",
            fg="white"
        ).grid(row=2, column=0, columnspan=3, pady=10)

    # The rest of the functions (view_all, add_login, etc.) must be implemented
    # as defined elsewhere in your codebase.

    root.mainloop()
    db.closeDatabase(connection)

if __name__ == "__main__":
    main()
