# MVP Overview

## Project Summary
The Furniture Inventory & Management System (FIMS) is a Tkinter-based GUI application that replaces a CLI system, offering an intuitive interface for managing furniture inventory. It features secure login with role-based access and stores data in a SQLite database (`data/placeholderData.db`). The system supports multiple user roles, ensuring tailored functionality for different users.

## Implemented User Stories
- **As an Administrator, I can securely log in to access all system features.**  
  - *Status*: Done.  
  - *Details*: Login with ID: 1, Password: pass123 grants full access (add, edit, remove, sort, search, view all, view specific, manage users). Tested successfully with sample data (e.g., added ID: 103, Sofa, Red, $199.99).

- **As a Store Manager, I can add, edit, and remove furniture items in the inventory.**  
  - *Status*: Done.  
  - *Details*: Login with ID: 2, Password: pass456 allows adding (e.g., ID: 103), editing (e.g., change price to $250), and removing items. Also includes view, sort, search, and view specific. Tested successfully.

- **As an Inventory Manager, I can sort and filter furniture items to organize the inventory.**  
  - *Status*: Done.  
  - *Details*: Login with ID: 4, Password: pass101 provides access to sort (by type or price) and search (filter by keyword). Also includes view all and view specific. Tested successfully after login fix.

- **As a Sales Associate, I can search furniture items to assist customers.**  
  - *Status*: Done.  
  - *Details*: Login with ID: 3, Password: pass789 (Employee role) allows searching by keyword (e.g., "Red"). Also includes view all and view specific. Tested successfully.

- **As a Warehouse Employee, I can view the furniture list to check stock.**  
  - *Status*: Done.  
  - *Details*: Login with ID: 5, Password: pass202 provides view-only access (view all and view specific). Tested successfully after login and GUI fix to ensure proper button reset.

- **As a Furniture Consultant, I can view specific furniture items to provide details to clients.**  
  - *Status*: Done.  
  - *Details*: All users can view specific items by ID (e.g., ID: 101 shows "Chair, Black, $49.99"). Tested successfully across all roles.

- **As a system, I can store and retrieve inventory data using a SQLite database.**  
  - *Status*: Done.  
  - *Details*: Furniture items are stored and retrieved from `data/placeholderData.db` (e.g., IDs 101, 102 preloaded; new items like ID: 103 added). Supports all view, sort, and search operations. Tested successfully.

## Gaps and Notes
- **Manager User Management**: Admin can add/delete users, but Manager-level user management (e.g., adding employees) is not implemented yet.
- **Advanced Features**: No support for images, bulk uploads, or autocomplete search—planned for future iterations.
- **Login Persistence**: Fixed issue where previous login buttons persisted; now resets GUI for each new login.
- **Database Reset**: Database was cleared to ensure all users (IDs 1–5) are initialized correctly.
- **Testing**: All features tested with sample data. Edge cases (e.g., duplicate IDs, invalid inputs) handled with error messages.
