import tkinter as tk
from tkinter import ttk, messagebox
import databasefunction as db
import furniture
import login
import random

def main():
    connection, cursor = db.loadDatabase()
    db.initializeDatabase(connection, cursor)

    # Add test data if it’s not there
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 1")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 1, 1, "testAdmin", "pass123")
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 2")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 2, 2, "testManager", "pass456")
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 3")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 3, 3, "testEmployee", "pass789")
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 101, "Chair", "Black", 49.99)
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 102, "Table", "Brown", 99.99)

    # Set up the Tkinter window
    root = tk.Tk()
    root.title("FIMS - Furniture Inventory & Management System")

    # Login Frame
    login_frame = ttk.Frame(root)
    login_frame.pack(pady=20)
    ttk.Label(login_frame, text="Staff ID:").grid(row=0, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(login_frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    pass_entry = ttk.Entry(login_frame, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def attempt_login():
        staff_id = id_entry.get()
        password = pass_entry.get()
        user = db.attemptLogin(cursor, staff_id, password)
        if user:
            messagebox.showinfo("Login Success", f"Welcome, {user[2]}!")
            login_frame.pack_forget()
            show_main_menu(user[1])
        else:
            messagebox.showerror("Login Failed", "Wrong ID or password—try again!")

    ttk.Button(login_frame, text="Login", command=attempt_login).grid(row=2, column=1, pady=10)

    # Main Menu Frame (hidden until login)
    main_frame = ttk.Frame(root)

    def show_main_menu(user_level):
        main_frame.pack(pady=20)
        ttk.Label(main_frame, text="System Options").pack()
        ttk.Button(main_frame, text="View All Furniture", command=lambda: view_all(cursor)).pack(pady=5)
        ttk.Button(main_frame, text="View Specific Furniture", command=lambda: view_specific(cursor)).pack(pady=5)
        ttk.Button(main_frame, text="Sort Furniture", command=lambda: sort_furniture(cursor)).pack(pady=5)
        ttk.Button(main_frame, text="Search Furniture", command=lambda: search_furniture(cursor)).pack(pady=5)
        if user_level <= 2:
            ttk.Button(main_frame, text="Add Furniture", command=lambda: add_furniture(connection, cursor)).pack(pady=5)
            ttk.Button(main_frame, text="Edit Furniture", command=lambda: edit_furniture(connection, cursor)).pack(pady=5)
            ttk.Button(main_frame, text="Remove Furniture", command=lambda: remove_furniture(connection, cursor)).pack(pady=5)
        if user_level <= 1:
            ttk.Button(main_frame, text="View Logins", command=lambda: view_logins(cursor)).pack(pady=5)
            ttk.Button(main_frame, text="Add Login", command=lambda: add_login(connection, cursor)).pack(pady=5)
            ttk.Button(main_frame, text="Delete Login", command=lambda: delete_login(connection, cursor)).pack(pady=5)
        ttk.Button(main_frame, text="Log Out", command=lambda: log_out(root, login_frame)).pack(pady=5)

    root.mainloop()

# Feature Functions
def view_all(cursor):
    furniture_list = furniture.get_furniture_list(cursor)
    if furniture_list:
        view_window = tk.Toplevel()
        view_window.title("All Furniture Items")
        listbox = tk.Listbox(view_window, width=50)
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
        listbox = tk.Listbox(view_window, width=50)
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
        furniture_list = furniture.get_furniture_list(cursor)
        matches = [item for item in furniture_list if keyword in item.get_type().lower() or keyword in item.get_colour().lower()]
        if matches:
            view_window = tk.Toplevel()
            view_window.title("Search Results")
            listbox = tk.Listbox(view_window, width=50)
            listbox.pack(pady=10)
            for item in matches:
                listbox.insert(tk.END, str(item))
        else:
            messagebox.showinfo("Info", "Nothing matches that keyword.")
        search_window.destroy()
    ttk.Button(search_window, text="Search", command=search_and_show).pack(pady=5)

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
    def add_item():
        try:
            id = int(id_entry.get())
            type = type_entry.get()
            colour = colour_entry.get()
            price = float(price_entry.get())
            db.addFurniture(connection, cursor, id, type, colour, price)
            messagebox.showinfo("Success", "Furniture added!")
            add_window.destroy()
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
    def update_item():
        new_type = type_entry.get()
        new_colour = colour_entry.get()
        try:
            new_price = float(price_entry.get())
            cursor.execute("UPDATE furniture SET type = ?, colour = ?, price = ? WHERE furniture_id = ?", 
                           (new_type, new_colour, new_price, item.furniture_id))
            connection.commit()
            messagebox.showinfo("Success", "Furniture updated!")
            form_window.destroy()
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
        cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
        connection.commit()
        messagebox.showinfo("Success", "Furniture removed if it was there!")
        remove_window.destroy()
    ttk.Button(remove_window, text="Remove", command=remove_item).pack(pady=5)

def view_logins(cursor):
    login_list = login.get_login_list(cursor)
    if login_list:
        view_window = tk.Toplevel()
        view_window.title("All Logins")
        listbox = tk.Listbox(view_window, width=50)
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
    ttk.Label(add_window, text="Level (1-3):").pack(pady=5)
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
            id = int(id_entry.get())
            level = int(level_entry.get())
            username = username_entry.get()
            password = password_entry.get()
            db.addLogin(connection, cursor, id, level, username, password)
            messagebox.showinfo("Success", "Login added!")
            add_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "ID and Level need to be numbers!")
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

def log_out(root, login_frame):
    main_frame.pack_forget()
    login_frame.pack(pady=20)

if __name__ == "__main__":
    main()