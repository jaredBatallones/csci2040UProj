# Furniture Inventory & Management System (FIMS)

## Overview
FIMS is a handy tool we created to manage inventory for a small-to-medium furniture store. It started as a command-line app, but we’ve upgraded it to a Tkinter GUI for this MVP. The system lets you log in with different roles (Admin, Manager, Employee), track furniture, add or remove items, sort them, and search with keywords—all powered by a SQLite database. We’ve come a long way, and this is what we’re submitting!

## Features
- **User Authentication**: Secure login using Staff ID and Password, with role-based access.
- **Inventory Management**: Add, edit, or remove furniture items with a few clicks.
- **Sorting & Filtering**: Sort by type or price using the GUI.
- **Search Functionality**: Search by keywords like type or color.
- **Role-Based Access**: Admins manage everything, Managers handle users, Employees view only.
- **Database Integration**: Stores data in SQLite.

## Prerequisites
- Python 3.8 or higher (includes Tkinter and SQLite3).
- Git :  https://github.com/jaredBatallones/csci2040UProj.git

## How to Set It Up
1. Clone the repo (if needed):
git clone https://github.com/jaredBatallones/csci2040UProj.git

2. Run the app:
python main.py

3. Log in with:
- Admin: Staff ID `1`, Password `pass123`
- Manager: Staff ID `2`, Password `pass456`
- Employee: Staff ID `3`, Password `pass789`
4. Use the GUI buttons (e.g., "View All Furniture" or "Add Furniture") to get started.

## Quick Look
- Log in as Admin (ID `1`, `pass123`) to see the full menu.
- Click "View All Furniture" to see items like:
- ID: 101, Type: Chair, Colour: Black, Price: $49.99
- ID: 102, Type: Table, Colour: Brown, Price: $99.99
- Try "Add Furniture" with ID `103`, Type `Sofa`, Colour `Red`, Price `199.99`.

## Dig Deeper
- **Walkthrough**: Check `MVP_Walkthrough.md` for screenshots of the GUI in action.
- **Details**: See `MVP_Overview.md` for what we built and any gaps.
- **Challenges**: Look at `Challenges_NextSteps.md` for hurdles and future plans.

## What’s Next?
We’re thinking of adding furniture images, beefing up permissions, and handling bigger inventories down the road.
