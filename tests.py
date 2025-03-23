import unittest
import databasefunction as db
import furniture
import login

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.connection, self.cursor = db.loadDatabase(test=True)
        db.initializeDatabase(self.connection, self.cursor)
        # Add initial data for consistent testing
        furniture.add_furniture(self.connection, self.cursor, 1, "Couch", "Red", 99.99)
        furniture.add_furniture(self.connection, self.cursor, 2, "Chair", "Brown", 100.99)
        login.initialize_users(self.connection, self.cursor)

    def test_UT_01_CB_add_furniture(self):
        new_furniture = furniture.Furniture(3, "Table", "Black", 150.00)
        furniture.add_furniture(self.connection, self.cursor, new_furniture.get_furniture_id(), new_furniture.get_type(), new_furniture.get_colour(), new_furniture.get_price())
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        self.assertEqual(len(database_furniture_list), 3, "Wrong number of items after adding")
        self.assertEqual(database_furniture_list[-1], new_furniture, "Furniture addition failed")
        db.closeDatabase(self.connection)

    def test_UT_02_CB_sort_by_type(self):
        sorted_list = furniture.sort_furniture_by_type(furniture.get_furniture_list(self.cursor))
        expected_list = [furniture.Furniture(2, "Chair", "Brown", 100.99), furniture.Furniture(1, "Couch", "Red", 99.99)]
        for i in range(len(expected_list)):
            self.assertEqual(sorted_list[i], expected_list[i], "Sort by type failed")
        db.closeDatabase(self.connection)

    def test_UT_03_CB_sort_by_price(self):
        sorted_list = furniture.sort_furniture_by_price(furniture.get_furniture_list(self.cursor))
        expected_list = [furniture.Furniture(1, "Couch", "Red", 99.99), furniture.Furniture(2, "Chair", "Brown", 100.99)]
        for i in range(len(expected_list)):
            self.assertEqual(sorted_list[i], expected_list[i], "Sort by price failed")
        db.closeDatabase(self.connection)

    def test_UT_04_CB_modify_furniture(self):
        furniture.update_furniture(self.connection, self.cursor, 1, "Couch", "Blue", 120.00)
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        expected_furniture = furniture.Furniture(1, "Couch", "Blue", 120.00)
        self.assertIn(expected_furniture, database_furniture_list, "Furniture modification failed")
        db.closeDatabase(self.connection)

    def test_UT_05_CB_search_keyword(self):
        matches = furniture.search_furniture(self.cursor, "Couch")
        expected_list = [furniture.Furniture(1, "Couch", "Red", 99.99)]
        self.assertEqual(len(matches), 1, "Search returned wrong number of items")
        self.assertEqual(matches[0], expected_list[0], "Search keyword failed")
        db.closeDatabase(self.connection)

    def test_UT_06_CB_remove_furniture(self):
        furniture.remove_furniture(self.connection, self.cursor, 1)
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        self.assertEqual(len(database_furniture_list), 1, "Furniture removal failed - wrong count")
        self.assertNotIn(furniture.Furniture(1, "Couch", "Red", 99.99), database_furniture_list, "Furniture not removed")
        db.closeDatabase(self.connection)

    def test_UT_07_CB_add_login(self):
        new_login = login.Login(6, 3, "newEmployee", "pass999")
        login.add_login(self.connection, self.cursor, new_login.get_staff_id(), new_login.get_level(), new_login.get_username(), new_login.get_password())
        database_login_list = login.get_login_list(self.cursor)
        self.assertEqual(len(database_login_list), 6, "Wrong number of logins after adding")
        self.assertIn(new_login, database_login_list, "Login addition failed")
        db.closeDatabase(self.connection)

    def test_UT_08_CB_remove_login(self):
        login.remove_login(self.connection, self.cursor, 1)
        database_login_list = login.get_login_list(self.cursor)
        self.assertEqual(len(database_login_list), 4, "Login removal failed - wrong count")
        self.assertNotIn(login.Login(1, 1, "testAdmin", "pass123"), database_login_list, "Login not removed")
        db.closeDatabase(self.connection)

    def test_UT_09_CB_login_validation_success(self):
        user = db.attemptLogin(self.cursor, "1", "pass123")
        self.assertIsNotNone(user, "Valid login failed")
        self.assertEqual(user[0], 1, "Wrong staff ID returned")
        db.closeDatabase(self.connection)

    def test_UT_10_CB_login_validation_failure(self):
        user = db.attemptLogin(self.cursor, "999", "wrongpass")
        self.assertIsNone(user, "Invalid login should return None")
        db.closeDatabase(self.connection)

    def test_UT_11_CB_add_furniture_duplicate(self):
        result = furniture.add_furniture(self.connection, self.cursor, 1, "Table", "Black", 150.00)
        self.assertFalse(result, "Adding duplicate ID should fail")
        db.closeDatabase(self.connection)
        
    def test_IT_01_TB_login_to_database(self):
      user = db.attemptLogin(self.cursor, "1", "pass123")
      self.assertIsNotNone(user, "Login to database integration failed")
      login_list = login.get_login_list(self.cursor)
      expected_login = login.Login(1, 1, "testAdmin", "pass123")
      self.assertIn(expected_login, login_list, "Login data not found in database")
      db.closeDatabase(self.connection)

    def test_IT_02_CB_gui_to_database(self):
      # Simulate GUI adding furniture (mocking GUI input)
      furniture.add_furniture(self.connection, self.cursor, 3, "Table", "Black", 150.00)
      database_furniture_list = furniture.get_furniture_list(self.cursor)
      expected_furniture = furniture.Furniture(3, "Table", "Black", 150.00)
      self.assertIn(expected_furniture, database_furniture_list, "GUI to database integration failed")
      db.closeDatabase(self.connection)