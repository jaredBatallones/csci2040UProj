```markdown
# 🛋️ Furniture Inventory & Management System (FIMS) 🎉

## 🌟 Overview
Welcome to **FIMS**, a sleek and **user-friendly inventory management system** crafted for small-to-medium furniture stores! Originally a command-line tool, we’ve elevated it to a **Tkinter-based GUI** for this MVP. Featuring **secure login with role-based access** for **Admin, Manager, Employee, Inventory Manager, and Warehouse Employee** roles, FIMS empowers users to **track furniture, add or remove items, sort, search by keywords, and view specifics**—all backed by a robust **SQLite database**. This is our proud submission for the project milestone! 🚀

---

## ✨ Features
- 🔐 **User Authentication**: Secure login with **Staff ID and Password**, customized by role-based access levels (1-5).  
- 📦 **Inventory Management**: Effortlessly add, edit, or remove furniture items via an intuitive GUI.  
- 🔄 **Sorting & Filtering**: Sort by **type** or **price** (available to **Managers** and **Inventory Managers**).  
- 🔍 **Search Functionality**: Quickly find items using **keywords** (e.g., type or color) (available to **Employees** and **Inventory Managers**).  
- 🛡️ **Role-Based Access**:  
  - **Admin (Level 1)**: Full access, including user management (add/delete users). 🧑‍💼  
  - **Manager (Level 2)**: Add, edit, remove, sort, search, and view furniture. 🖥️  
  - **Employee (Level 3)**: Search and view furniture items. 👀  
  - **Inventory Manager (Level 4)**: Sort, search, and view furniture items. 📊  
  - **Warehouse Employee (Level 5)**: View-only access (all or specific items). 📋  
- 💾 **Database Integration**: Data stored in **SQLite database** (`data/placeholderData.db`), initialized with defaults on startup.  

---

## 🛠️ Prerequisites
- 🐍 **Python 3.8 or higher**: Comes with `tkinter` and `sqlite3` in the standard library.  
- 🌍 **Git (Optional)**: Useful for cloning the repository (not required if using the zip file).  

---

## 🚀 How to Set It Up
### 1️⃣ Clone the Repository (if needed)
Run this command to get the code:  
```bash
git clone https://github.com/jaredBatallones/csci2040UProj.git
```

### 2️⃣ Run the App
Launch the application with:  
```bash
python main.py
```
This will create and initialize the SQLite database (`data/placeholderData.db`) with default users and furniture items.

### 3️⃣ Log in with Default Credentials
Use these pre-set accounts to get started:  

| Role                 | Staff ID | Password  |
|----------------------|----------|-----------|
| **Admin**            | `1`      | `pass123` |
| **Manager**          | `2`      | `pass456` |
| **Employee**         | `3`      | `pass789` |
| **Inventory Manager**| `4`      | `pass101` |
| **Warehouse Employee**| `5`     | `pass202` |

### 4️⃣ Explore the GUI
After logging in, discover role-specific options like **"View All Furniture"** or **"Add Furniture"**. Dive in—try adding, sorting, or searching for items!

---

## 👀 Quick Look
1. **Log in as Admin** (ID `1`, Password `pass123`):  
   Unlock the full menu, including user management options (**"View Logins," "Add Login," "Delete Login"**).  

2. **View Default Furniture**:  
   Hit **"View All Furniture"** to see:  
   - **ID:** 101, **Type:** Chair, **Colour:** Black, **Price:** $49.99  
   - **ID:** 102, **Type:** Table, **Colour:** Brown, **Price:** $99.99  

3. **Add a New Item** (as Manager, ID `2`, Password `pass456`):  
   Select **"Add Furniture"** and input:  
   - **ID:** 103, **Type:** Sofa, **Colour:** Red, **Price:** $199.99  
   Confirm it in **"View All Furniture."**

4. **Sort or Search** (as Inventory Manager, ID `4`, Password `pass101`):  
   Sort by **price** or **type**, or search **"Red"** to locate the sofa.  

5. **View Only** (as Warehouse Employee, ID `5`, Password `pass202`):  
   Check stock with **"View All Furniture"** or **"View Specific Furniture"** (e.g., ID `101`).  

---

## 📖 Dig Deeper
- 📸 **Walkthrough**: Explore **`MVP_Walkthrough.md`** for GUI screenshots across roles.  
- 📖 **Details**: Dive into **`MVP_Overview.md`** for user stories and project gaps.  
- ⚠️ **Challenges**: Review **`Challenges_NextSteps.md`** for obstacles and future plans.  

---

## 🌍 What’s Next?
We’re gearing up to enhance FIMS with:  
- 🖼️ **Support for furniture images** in the inventory.  
- 🧑‍💼 **Manager-level user management** (e.g., adding Employees).  
- 💾 **Persistent data storage** across sessions (no more resets).  
- 🔧 **Advanced features** like bulk uploads and autocomplete search.  
- 🎨 **UI improvements** with enhanced layouts, themes, and dialogs.  

---

## 📁 Project Structure
```
mainProject/
├── data/
│   └── placeholderData.db    # SQLite database (ignored in Git)
├── __pycache__/             # Compiled Python files (ignored in Git)
├── databasefunction.py      # Database connection and login functions
├── furniture.py             # Furniture class and inventory operations
├── login.py                 # Login class and user initialization
├── main.py                  # Main application logic and GUI
├── Challenges_NextSteps.md  # Challenges and future improvements
├── MVP_Overview.md          # Project summary and implemented user stories
├── MVP_Walkthrough.md       # Screenshots and walkthrough
├── README.md                # This file
├── repo_link.txt            # GitHub repository URL
└── .gitignore               # Ignores __pycache__ and database file
```

---

## 👥 Team Members
- Jared nathan Batallones
- Arian Vares
- Wei Cui
- Guillermo Rebolledo
- Jilun Liang 

---

## 📜 License
This project is for educational purposes only. No formal license applies, but feel free to use it as a reference!  

---

## 🔗 Repository
- **GitHub**: https://github.com/jaredBatallones/csci2040UProj.git 
```