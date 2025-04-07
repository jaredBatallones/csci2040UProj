import tkinter as tk
from tkinter import ttk, messagebox
import databasefunction as db
import furniture
import login
from PIL import Image, ImageTk

def main():
    # Set up the database

    connection, cursor = db.loadDatabase(test=True)
    db.initializeDatabase(connection, cursor)
    login.initialize_users(connection, cursor)

    # Add test furniture if not present (with new size and aisle fields)
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 101, "Chair", "Black", 49.99, "Medium", "A3")
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        furniture.add_furniture(connection, cursor, 102, "Table", "Brown", 99.99, "Large", "B1")

    # Set up the Tkinter window
    root = tk.Tk()
    root.title("FIMS - Furniture Inventory & Management System")
    root.geometry("400x600")  # Adjusted for extra fields

    # Login Frame
    login_frame = ttk.Frame(root)
    login_frame.pack(pady=20)
    ttk.Label(login_frame, text="Username or ID:").grid(row=0, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(login_frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    pass_entry = ttk.Entry(login_frame, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def attempt_login():
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


    def show_main_menu(user_level):
        # Remove any previous main menu frames (using tk.Frame)
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != login_frame:
                widget.destroy()
        
        # Create the main frame with a neutral background (you can adjust as needed)
        main_frame = tk.Frame(root, bg="#ADD8E6")
        main_frame.pack(pady=20, fill="both", expand=True)
        
        # Top label showing Access Level spanning all three columns
        access_label = tk.Label(main_frame,
                                text=f"Access Level: {login.Login(0, user_level, '', '').__str__().split('Level: ')[1]}",
                                bg="#ADD8E6", fg="black")
        access_label.grid(row=0, column=0, columnspan=3, pady=5)
        
        # Create subframes for each column with desired background colors:
        # Column 1: Orange (#FFA500)
        col1 = tk.Frame(main_frame, bg="#FFA500")
        col1.grid(row=1, column=0, padx=10, sticky="n")
        
        # Column 2: White (#FFFFFF)
        col2 = tk.Frame(main_frame, bg="#FFFFFF")
        col2.grid(row=1, column=1, padx=10, sticky="n")
        
        # Column 3: Light Green (#90EE90)
        col3 = tk.Frame(main_frame, bg="#90EE90")
        col3.grid(row=1, column=2, padx=10, sticky="n")
        
        # Column 1: Common buttons (colored orange)
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
        
        # Column 2: Admin-only login management buttons (colored white)
        if user_level == 1:
            tk.Button(col2, text="View Logins", command=lambda: view_logins(cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)
            tk.Button(col2, text="Add Login", command=lambda: add_login(connection, cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)
            tk.Button(col2, text="Delete Login", command=lambda: delete_login(connection, cursor),
                      bg="#FFFFFF", fg="black").pack(pady=5)
        
        # Column 3: Picture-based search and specific view (colored light green)
        tk.Button(col3, text="Search by Picture", command=search_by_picture,
                  bg="#90EE90", fg="black").pack(pady=5)
        tk.Button(col3, text="View Specific Furniture", command=lambda: view_specific(cursor),
                  bg="#90EE90", fg="black").pack(pady=5)
        
        # Log Out button across the bottom spanning all columns, colored red
        tk.Button(main_frame, text="Log Out", command=lambda: log_out(root, login_frame, main_frame),
                  bg="#FF0000", fg="white").grid(row=2, column=0, columnspan=3, pady=10)


    def view_all(cursor):
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
        # Create a new window for picture-based search
        pic_window = tk.Toplevel(root)
        pic_window.title("Search by Picture")
        #pic_window.geometry("600x250")  # Enough room for grid layout
    
        # Load and resize all images
        chair_img = Image.open("chair.png").resize((100, 100))
        table_img = Image.open("table.png").resize((100, 100))
        sofa_img  = Image.open("sofa.png").resize((100, 100))
        cabinet_img = Image.open("cabinet.png").resize((100, 100))
        bed_img = Image.open("bed.png").resize((100, 100))
        shelf_img = Image.open("shelf.png").resize((100, 100))
    
        # Convert to PhotoImage
        chair_photo = ImageTk.PhotoImage(chair_img)
        table_photo = ImageTk.PhotoImage(table_img)
        sofa_photo  = ImageTk.PhotoImage(sofa_img)
        cabinet_photo = ImageTk.PhotoImage(cabinet_img)
        bed_photo = ImageTk.PhotoImage(bed_img)
        shelf_photo = ImageTk.PhotoImage(shelf_img)
    
        # Keep a frame and store references
        frame = tk.Frame(pic_window)
        frame.pack(pady=10)
    
        images = [
            ("Chair", chair_photo, "chair"),
            ("Table", table_photo, "table"),
            ("Sofa", sofa_photo, "sofa"),
            ("Cabinet", cabinet_photo, "cabinet"),
            ("Bed", bed_photo, "bed"),
            ("Shelf", shelf_photo, "shelf"),
        ]
    
        # Helper to add buttons in grid
        def add_button(image, keyword, row, col, label):
            btn = tk.Button(frame, image=image, command=lambda: perform_search(keyword))
            btn.image = image  # prevent garbage collection
            btn.grid(row=row * 2, column=col, padx=10, pady=5)
            tk.Label(frame, text=label).grid(row=row * 2 + 1, column=col)
    
        # Loop through and place in 2 rows
        for i, (label, img, key) in enumerate(images):
            row = i // 3
            col = i % 3
            add_button(img, key, row, col, label)


    def perform_search(keyword):
        # Use your furniture module's search function to find matches based on the keyword
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
        add_window = tk.Toplevel()
        add_window.title("Add Furniture")
        ttk.Label(add_window, text="ID:").pack(pady=5)
        id_entry = ttk.Entry(add_window)
        id_entry.pack(pady=5)
        ttk.Label(add_window, text="Type:").pack(pady=5)
        type_entry = ttk.Entry(add_window)
        type_entry.pack(pady=5)
        ttk.Label(add_window, text="Colour:").pack(pady=5)
        colour_entry = ttk.Entry(add_window)
        colour_entry.pack(pady=5)
        ttk.Label(add_window, text="Price:").pack(pady=5)
        price_entry = ttk.Entry(add_window)
        price_entry.pack(pady=5)
        # New fields for size and aisle
        ttk.Label(add_window, text="Size:").pack(pady=5)
        size_entry = ttk.Entry(add_window)
        size_entry.pack(pady=5)
        ttk.Label(add_window, text="Aisle:").pack(pady=5)
        aisle_entry = ttk.Entry(add_window)
        aisle_entry.pack(pady=5)
        def add_item():
            try:
                id_val = int(id_entry.get())
                type_val = type_entry.get()
                colour_val = colour_entry.get()
                price = float(price_entry.get())
                size_val = size_entry.get()
                aisle_val = aisle_entry.get()
                if furniture.add_furniture(connection, cursor, id_val, type_val, colour_val, price, size_val, aisle_val):
                    messagebox.showinfo("Success", "Furniture added!")
                    add_window.destroy()
                else:
                    messagebox.showerror("Error", "Furniture ID already exists!")
            except ValueError:
                messagebox.showerror("Error", "Check your inputs—ID and Price need to be numbers!")
        ttk.Button(add_window, text="Add", command=add_item).pack(pady=5)

    def edit_furniture(connection, cursor):
        edit_window = tk.Toplevel()
        edit_window.title("Edit Furniture")
        ttk.Label(edit_window, text="Furniture ID:").pack(pady=5)
        id_entry = ttk.Entry(edit_window)
        id_entry.pack(pady=5)
        def load_item():
            furniture_id = id_entry.get()
            furniture_list = furniture.get_furniture_list(cursor)
            for item in furniture_list:
                if str(item.furniture_id) == furniture_id:
                    edit_form(item)
                    edit_window.destroy()
                    return
            messagebox.showerror("Error", "That ID doesn’t exist!")
        ttk.Button(edit_window, text="Load", command=load_item).pack(pady=5)

    def edit_form(item):
        form_window = tk.Toplevel()
        form_window.title("Edit Furniture")
        ttk.Label(form_window, text="Type:").pack(pady=5)
        type_entry = ttk.Entry(form_window)
        type_entry.insert(0, item.get_type())
        type_entry.pack(pady=5)
        ttk.Label(form_window, text="Colour:").pack(pady=5)
        colour_entry = ttk.Entry(form_window)
        colour_entry.insert(0, item.get_colour())
        colour_entry.pack(pady=5)
        ttk.Label(form_window, text="Price:").pack(pady=5)
        price_entry = ttk.Entry(form_window)
        price_entry.insert(0, str(item.get_price()))
        price_entry.pack(pady=5)
        # New fields for size and aisle in the edit form
        ttk.Label(form_window, text="Size:").pack(pady=5)
        size_entry = ttk.Entry(form_window)
        size_entry.insert(0, item.size if hasattr(item, 'size') else "")
        size_entry.pack(pady=5)
        ttk.Label(form_window, text="Aisle:").pack(pady=5)
        aisle_entry = ttk.Entry(form_window)
        aisle_entry.insert(0, item.aisle if hasattr(item, 'aisle') else "")
        aisle_entry.pack(pady=5)
        def update_item():
            new_type = type_entry.get()
            new_colour = colour_entry.get()
            try:
                new_price = float(price_entry.get())
                new_size = size_entry.get()
                new_aisle = aisle_entry.get()
                if furniture.update_furniture(connection, cursor, item.furniture_id, new_type, new_colour, new_price, new_size, new_aisle):
                    messagebox.showinfo("Success", "Furniture updated!")
                    form_window.destroy()
                else:
                    messagebox.showerror("Error", "Update failed!")
            except ValueError:
                messagebox.showerror("Error", "Price needs to be a number!")
        ttk.Button(form_window, text="Update", command=update_item).pack(pady=5)

    def remove_furniture(connection, cursor):
        remove_window = tk.Toplevel()
        remove_window.title("Remove Furniture")
        ttk.Label(remove_window, text="Furniture ID:").pack(pady=5)
        id_entry = ttk.Entry(remove_window)
        id_entry.pack(pady=5)
        def remove_item():
            furniture_id = id_entry.get()
            if furniture.remove_furniture(connection, cursor, furniture_id):
                messagebox.showinfo("Success", "Furniture removed if it was there!")
            else:
                messagebox.showerror("Error", "Removal failed!")
            remove_window.destroy()
        ttk.Button(remove_window, text="Remove", command=remove_item).pack(pady=5)

    def view_logins(cursor):
        login_list = login.get_login_list(cursor)
        if login_list:
            view_window = tk.Toplevel()
            view_window.title("All Logins")
            listbox = tk.Listbox(view_window, width=70)
            listbox.pack(pady=10)
            for item in login_list:
                listbox.insert(tk.END, str(item))
        else:
            messagebox.showinfo("Info", "No logins yet!")

    def add_login(connection, cursor):
        add_window = tk.Toplevel()
        add_window.title("Add Login")
        ttk.Label(add_window, text="Staff ID:").pack(pady=5)
        id_entry = ttk.Entry(add_window)
        id_entry.pack(pady=5)
        ttk.Label(add_window, text="Level (1-5):").pack(pady=5)
        level_entry = ttk.Entry(add_window)
        level_entry.pack(pady=5)
        ttk.Label(add_window, text="Username:").pack(pady=5)
        username_entry = ttk.Entry(add_window)
        username_entry.pack(pady=5)
        ttk.Label(add_window, text="Password:").pack(pady=5)
        password_entry = ttk.Entry(add_window)
        password_entry.pack(pady=5)
        def add_user():
            try:
                id_val = int(id_entry.get())
                level = int(level_entry.get())
                if level not in [1, 2, 3, 4, 5]:
                    raise ValueError("Level must be between 1 and 5")
                username = username_entry.get()
                password = password_entry.get()
                db.addLogin(connection, cursor, id_val, level, username, password)
                messagebox.showinfo("Success", "Login added!")
                add_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        ttk.Button(add_window, text="Add", command=add_user).pack(pady=5)

    def delete_login(connection, cursor):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Login")
        ttk.Label(delete_window, text="Staff ID:").pack(pady=5)
        id_entry = ttk.Entry(delete_window)
        id_entry.pack(pady=5)
        def delete_user():
            staff_id = id_entry.get()
            cursor.execute("DELETE FROM login WHERE staff_id = ?", (staff_id,))
            connection.commit()
            messagebox.showinfo("Success", "Login deleted if it existed!")
            delete_window.destroy()
        ttk.Button(delete_window, text="Delete", command=delete_user).pack(pady=5)

    def log_out(root, login_frame, current_frame):
        current_frame.destroy()
        login_frame.pack(pady=20)

    root.mainloop()
    db.closeDatabase(connection)

if __name__ == "__main__":
    main()
