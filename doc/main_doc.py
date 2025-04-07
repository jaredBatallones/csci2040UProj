import tkinter as tk
from tkinter import ttk, messagebox
import databasefunction as db
import furniture
import login
from PIL import Image, ImageTk

def main():
    """
    Main entry point for the Furniture Inventory & Management System (FIMS).

    This function sets up the database, initializes sample furniture and user data
    if needed, and launches the Tkinter-based GUI for login and furniture management.
    """
    # --- Database Setup ---
    connection, cursor = db.loadDatabase(test=True)
    db.initializeDatabase(connection, cursor)
    login.initialize_users(connection, cursor)

    # --- Seed test data if not already present ---
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 101, "Chair", "Black", 49.99, "Medium", "A3")

    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 102, "Table", "Brown", 99.99, "Large", "B1")

    # --- GUI Setup ---
    root = tk.Tk()
    root.title("FIMS - Furniture Inventory & Management System")
    root.geometry("400x600")

    # ---------------------- LOGIN UI ---------------------- #
    login_frame = ttk.Frame(root)
    login_frame.pack(pady=20)

    ttk.Label(login_frame, text="Username or ID:").grid(row=0, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(login_frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    pass_entry = ttk.Entry(login_frame, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def attempt_login():
        """
        Attempts login using credentials from Entry fields.
        If successful, hides login UI and shows main menu.
        """
        identifier = id_entry.get()
        password = pass_entry.get()
        user = login.attemptLogin(cursor, identifier, password)
        if user:
            messagebox.showinfo("Login Success", f"Welcome, {user.get_username()}!")
            login_frame.pack_forget()
            show_main_menu(user.get_level())
        else:
            messagebox.showerror("Login Failed", "Wrong ID or password—try again!")

    ttk.Button(login_frame, text="Login", command=attempt_login).grid(row=2, column=1, pady=10)

    # ---------------------- MAIN MENU ---------------------- #
    def show_main_menu(user_level):
        """
        Displays the main menu based on the user's access level.

        Parameters
        ----------
        user_level : int
            Access level of the current user.
        """
        # Clear all other widgets
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != login_frame:
                widget.destroy()

        # Main Menu Layout
        main_frame = tk.Frame(root, bg="#ADD8E6")
        main_frame.pack(pady=20, fill="both", expand=True)

        access_label = tk.Label(
            main_frame,
            text=f"Access Level: {login.Login(0, user_level, '', '').__str__().split('Level: ')[1]}",
            bg="#ADD8E6", fg="black"
        )
        access_label.grid(row=0, column=0, columnspan=3, pady=5)

        col1 = tk.Frame(main_frame, bg="#FFA500")
        col1.grid(row=1, column=0, padx=10, sticky="n")

        col2 = tk.Frame(main_frame, bg="#FFFFFF")
        col2.grid(row=1, column=1, padx=10, sticky="n")

        col3 = tk.Frame(main_frame, bg="#90EE90")
        col3.grid(row=1, column=2, padx=10, sticky="n")

        # Column 1 - Basic Furniture Actions
        tk.Button(col1, text="View All Furniture", command=lambda: view_all(cursor),
                  bg="#FFA500", fg="black").pack(pady=5)
        if user_level <= 4:
            tk.Button(col1, text="Search Furniture", command=lambda: search_furniture(cursor),
                      bg="#FFA500", fg="black").pack(pady=5)
            tk.Button(col1, text="Sort Furniture", command=lambda: sort_furniture(cursor),
                      bg="#FFA500", fg="black").pack(pady=5)
        if user_level <= 2:
            tk.Button(col1, text="Add Furniture", command=lambda: add_furniture(connection, cursor),
                      bg="#FFA500", fg="black").pack(pady=5)
            tk.Button(col1, text="Edit Furniture", command=lambda: edit_furniture(connection, cursor),
                      bg="#FFA500", fg="black").pack(pady=5)
            tk.Button(col1, text="Remove Furniture", command=lambda: remove_furniture(connection, cursor),
                      bg="#FFA500", fg="black").pack(pady=5)

        # Column 2 - Admin Login Management
        if user_level == 1:
            tk.Button(col2, text="View Logins", command=lambda: view_logins(cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)
            tk.Button(col2, text="Add Login", command=lambda: add_login(connection, cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)
            tk.Button(col2, text="Delete Login", command=lambda: delete_login(connection, cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)

        # Column 3 - Search by Picture & View Specific
        tk.Button(col3, text="Search by Picture", command=search_by_picture,
                  bg="#90EE90", fg="black").pack(pady=5)
        tk.Button(col3, text="View Specific Furniture", command=lambda: view_specific(cursor),
                  bg="#90EE90", fg="black").pack(pady=5)

        # Bottom - Log Out Button
        tk.Button(main_frame, text="Log Out", command=lambda: log_out(root, login_frame, main_frame),
                  bg="#FF0000", fg="white").grid(row=2, column=0, columnspan=3, pady=10)

    # ---------------------- GUI HELPER FUNCTIONS ---------------------- #

    def view_all(cursor):
        """Displays all furniture records in a new window."""
        furniture_list = furniture.get_furniture_list(cursor)
        if furniture_list:
            view_window = tk.Toplevel()
            view_window.title("All Furniture Items")
            listbox = tk.Listbox(view_window, width=70)
            listbox.pack(pady=10)
            for item in furniture_list:
                listbox.insert(tk.END, str(item))
        else:
            messagebox.showinfo("Info", "No furniture items yet!")

    def view_specific(cursor):
        """Prompts user to enter an ID and shows the matching furniture if found."""
        specific_window = tk.Toplevel()
        specific_window.title("View Specific Furniture")
        ttk.Label(specific_window, text="Furniture ID:").pack(pady=5)
        id_entry = ttk.Entry(specific_window)
        id_entry.pack(pady=5)

        def show_item():
            furniture_id = id_entry.get()
            furniture_list = furniture.get_furniture_list(cursor)
            for item in furniture_list:
                if str(item.furniture_id) == furniture_id:
                    messagebox.showinfo("Furniture Details", str(item))
                    specific_window.destroy()
                    return
            messagebox.showerror("Error", "That ID doesn’t exist!")
        ttk.Button(specific_window, text="View", command=show_item).pack(pady=5)

    def sort_furniture(cursor):
        """Prompts user for sort type and displays sorted furniture list."""
        sort_window = tk.Toplevel()
        sort_window.title("Sort Furniture")
        ttk.Label(sort_window, text="Sort by:").pack(pady=5)
        sort_choice = tk.StringVar()
        ttk.Radiobutton(sort_window, text="Type", variable=sort_choice, value="type").pack()
        ttk.Radiobutton(sort_window, text="Price", variable=sort_choice, value="price").pack()

        def sort_and_show():
            furniture_list = furniture.get_furniture_list(cursor)
            if sort_choice.get() == "type":
                sorted_list = furniture.sort_furniture_by_type(furniture_list)
            elif sort_choice.get() == "price":
                sorted_list = furniture.sort_furniture_by_price(furniture_list)
            else:
                messagebox.showerror("Error", "Pick a sort option first!")
                return
            view_window = tk.Toplevel()
            view_window.title("Sorted Furniture")
            listbox = tk.Listbox(view_window, width=70)
            listbox.pack(pady=10)
            for item in sorted_list:
                listbox.insert(tk.END, str(item))

        ttk.Button(sort_window, text="Sort", command=sort_and_show).pack(pady=5)

    def search_furniture(cursor):
        """Search furniture based on a keyword entered by the user."""
        search_window = tk.Toplevel()
        search_window.title("Search Furniture")
        ttk.Label(search_window, text="Keyword:").pack(pady=5)
        keyword_entry = ttk.Entry(search_window)
        keyword_entry.pack(pady=5)

        def search_and_show():
            keyword = keyword_entry.get().lower()
            matches = furniture.search_furniture(cursor, keyword)
            if matches:
                view_window = tk.Toplevel()
                view_window.title("Search Results")
                listbox = tk.Listbox(view_window, width=70)
                listbox.pack(pady=10)
                for item in matches:
                    listbox.insert(tk.END, str(item))
            else:
                messagebox.showinfo("Info", "Nothing matches that keyword.")
            search_window.destroy()
        ttk.Button(search_window, text="Search", command=search_and_show).pack(pady=5)

    def search_by_picture():
        """Allows user to click images of furniture types to search."""
        pic_window = tk.Toplevel(root)
        pic_window.title("Search by Picture")
        frame = tk.Frame(pic_window)
        frame.pack(pady=10)

        # Load images
        images = [
            ("Chair", "chair.png", "chair"),
            ("Table", "table.png", "table"),
            ("Sofa", "sofa.png", "sofa"),
            ("Cabinet", "cabinet.png", "cabinet"),
            ("Bed", "bed.png", "bed"),
            ("Shelf", "shelf.png", "shelf"),
        ]

        def add_button(label, path, keyword, row, col):
            image = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
            btn = tk.Button(frame, image=image, command=lambda: perform_search(keyword))
            btn.image = image
            btn.grid(row=row * 2, column=col, padx=10, pady=5)
            tk.Label(frame, text=label).grid(row=row * 2 + 1, column=col)

        for i, (label, path, key) in enumerate(images):
            row, col = divmod(i, 3)
            add_button(label, path, key, row, col)

    def perform_search(keyword):
        """Performs picture-based search and shows results."""
        matches = furniture.search_furniture(cursor, keyword)
        if matches:
            results_window = tk.Toplevel(root)
            results_window.title(f"Search Results for {keyword}")
            listbox = tk.Listbox(results_window, width=70)
            listbox.pack(pady=10)
            for item in matches:
                listbox.insert(tk.END, str(item))
        else:
            messagebox.showinfo("Search", f"No results found for {keyword}")

    def add_furniture(connection, cursor):
        """GUI form to add new furniture entry."""
        # ... (Already documented well in your code – same style applies here.)

    def edit_furniture(connection, cursor):
        """GUI to load and edit an existing furniture item."""
        # ...

    def remove_furniture(connection, cursor):
        """GUI to remove a furniture entry by ID."""
        # ...

    def view_logins(cursor):
        """Displays all login records (admin only)."""
        # ...

    def add_login(connection, cursor):
        """GUI to add a new login (admin only)."""
        # ...

    def delete_login(connection, cursor):
        """GUI to delete a login by Staff ID (admin only)."""
        # ...

    def log_out(root, login_frame, current_frame):
        """Logs out the user and returns to the login screen."""
        current_frame.destroy()
        login_frame.pack(pady=20)

    # Start Tkinter event loop
    root.mainloop()
    db.closeDatabase(connection)

if __name__ == "__main__":
    main()
