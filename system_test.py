import unittest
import databasefunction as db
import furniture
import login

class SystemTests(unittest.TestCase):
    def setUp(self):
        self.connection, self.cursor = db.loadDatabase(test=True)
        db.initializeDatabase(self.connection, self.cursor)
        login.initialize_users(self.connection, self.cursor)
        furniture.add_furniture(self.connection, self.cursor, 101, "Chair", "Black", 49.99, "Small", "A1")

    def test_ST_01_OB_admin_workflow(self):
        # Login as admin
        user = login.attemptLogin(self.cursor, "1", "pass123")
        self.assertIsNotNone(user, "Admin login failed")
        # View all
        furniture_list = furniture.get_furniture_list(self.cursor)
        self.assertTrue(len(furniture_list) > 0, "View all failed")
        # Add furniture
        furniture.add_furniture(self.connection, self.cursor, 103, "Sofa", "Red", 199.99, "Large", "E4")
        self.assertIn(furniture.Furniture(103, "Sofa", "Red", 199.99, "Large", "E4"), furniture.get_furniture_list(self.cursor), "Add furniture failed")
        # Edit furniture
        furniture.update_furniture(self.connection, self.cursor, 103, "Sofa", "Blue", 199.99, "Large", "E4")
        self.assertIn(furniture.Furniture(103, "Sofa", "Blue", 199.99, "Large", "E4"), furniture.get_furniture_list(self.cursor), "Edit furniture failed")
        # Remove furniture
        furniture.remove_furniture(self.connection, self.cursor, 103)
        self.assertNotIn(furniture.Furniture(103, "Sofa", "Blue", 199.99, "Large", "E4"), furniture.get_furniture_list(self.cursor), "Remove furniture failed")
        furniture.remove_furniture(self.connection, self.cursor, 101)
        db.closeDatabase(self.connection)

if __name__ == '__main__':
    unittest.main()