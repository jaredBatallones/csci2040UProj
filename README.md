## **Overview**
FIMS is a **user-friendly inventory management system** designed for small-to-medium furniture stores. It started as a command-line application, but we’ve upgraded it to a **Tkinter-based GUI** for this MVP.  

The system provides **secure login with role-based access** for different user types (**Admin, Manager, Employee, Inventory Manager, and Warehouse Employee**). Users can **track furniture, add or remove items, sort them, search by keywords, and view specific items**—all powered by an **SQLite database**.  

This is our submission for the project milestone, and we’re excited to share our progress! 🚀  

---

## **Features**
- 🔐 **User Authentication** – Secure login using **Staff ID and Password**, with **role-based access** levels (1-5).  
- 📦 **Inventory Management** – Add, edit, or remove furniture items with an intuitive GUI.  
- 🔄 **Sorting & Filtering** – Sort items by **type** or **price** (available to **Managers** and **Inventory Managers**).  
- 🔍 **Search Functionality** – Search by **keywords** (e.g., type or color) for quick lookups (**available to Employees and Inventory Managers**).  
- 🛡️ **Role-Based Access**:  

  - **Admin (Level 1)** – Full access, including user management (add/delete users).  
  - **Manager (Level 2)** – Add, edit, remove, sort, search, and view furniture.  
  - **Employee (Level 3)** – Search and view furniture items.  
  - **Inventory Manager (Level 4)** – Sort, search, and view furniture items.  
  - **Warehouse Employee (Level 5)** – View-only access (all or specific items).  

- 💾 **Database Integration** – Stores data in an **SQLite database** (`data/placeholderData.db`), initialized with default users and furniture on startup.  

---

## **Prerequisites**
- 🐍 **Python 3.8 or higher** – Includes `tkinter` and `sqlite3` in the standard library.  
- 🌍 **Git (Optional)** – For cloning the repository (not required if downloading the zip).  

---

## **How to Set It Up**
### **1️⃣ Clone the Repository (if needed)**
Run the following command:  
```bash
git clone https://github.com/jaredBatallones/csci2040UProj.git
cd fims


2. **2.Run the App**:
 python main.py
 
 The application will create and initialize the SQLite database (data/placeholderData.db) with default users and furniture items.
 
3. **Log in with Default Credentials**:
Admin: Staff ID 1, Password pass123
Manager: Staff ID 2, Password pass456
Employee: Staff ID 3, Password pass789
Inventory Manager: Staff ID 4, Password pass101
Warehouse Employee: Staff ID 5, Password pass202

4. **Use the GUI**:
After logging in, you’ll see buttons based on your role (e.g., "View All Furniture," "Add Furniture").
Click to interact with the inventory—try adding, sorting, or searching for items!

## **Quick Look**

**1. Log in as Admin** (ID `1`, Password `pass123`):  
See the full menu, including user management options (**"View Logins," "Add Login," "Delete Login"**).

**2. View Default Furniture**:  
Click **"View All Furniture"** to see preloaded items:  
- **ID:** 101, **Type:** Chair, **Colour:** Black, **Price:** $49.99  
- **ID:** 102, **Type:** Table, **Colour:** Brown, **Price:** $99.99  

**3. Add a New Item (as Manager, ID `2`, Password `pass456`)**:  
Click **"Add Furniture"** and enter:  
- **ID:** 103, **Type:** Sofa, **Colour:** Red, **Price:** $199.99  
Verify it appears in **"View All Furniture."**

**4. Sort or Search (as Inventory Manager, ID `4`, Password `pass101`)**:  
Sort by **price** or **type**, or search for **"Red"** to find the sofa.

**5. View Only (as Warehouse Employee, ID `5`, Password `pass202`)**:  
Check stock with **"View All Furniture"** or **"View Specific Furniture"** (e.g., ID `101`).

---

## **Dig Deeper**

📸 **Walkthrough:** Check **`MVP_Walkthrough.md`** for screenshots of the GUI in action across different roles.  

📖 **Details:** See **`MVP_Overview.md`** for a full summary of implemented user stories and gaps.  

⚠️ **Challenges:** Look at **`Challenges_NextSteps.md`** for hurdles we faced and future plans.  

---

## **What’s Next?**

We’re planning to enhance FIMS with the following features:

- 🖼️ **Support for furniture images** in the inventory.  
- 🧑‍💼 **Manager-level user management** (e.g., adding Employees).  
- 💾 **Persistent data storage** across sessions (avoid resetting the database).  
- 🔧 **Advanced features** like bulk uploads and autocomplete search.  
- 🎨 **UI improvements** with better layouts, themes, and confirmation dialogs.  

---

## **Project Structure**


## **Team Members**

Jared nathan Batallones
Arian Vares
Wei Cui
Guillermo Rebolledo
Jilun Liang
