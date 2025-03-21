import unittest
import databasefunction as db
import furniture
import login

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.connection, self.cursor = db.loadDatabase(test=True)
        db.initializeDatabase(self.connection, self.cursor)
    
    def test_1_add_furniture(self):
        test_furniture = furniture.Furniture(1, "Couch", "Brown", "99.99")
        test_furniture_list = [test_furniture]
        furniture.add_furniture(self.connection, self.cursor, test_furniture.get_furniture_id(), test_furniture.get_type(), test_furniture.get_colour(), test_furniture.get_price())
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        self.assertEqual(database_furniture_list[0], test_furniture_list[0], "Furniture addition unsuccessful")
        db.closeDatabase(self.connection)

    def test_2_sort_by_type(self):
        test_furniture_1 = furniture.Furniture(1, "Couch", "Brown", "99.99")

        test_furniture_2 = furniture.Furniture(2, "Chair", "Brown", "100.99")
        furniture.add_furniture(self.connection, self.cursor, test_furniture_2.get_furniture_id(), test_furniture_2.get_type(), test_furniture_2.get_colour(), test_furniture_2.get_price())
        
        test_furniture_3 = furniture.Furniture(3, "Couch", "White", "80.99")
        furniture.add_furniture(self.connection, self.cursor, test_furniture_3.get_furniture_id(), test_furniture_3.get_type(), test_furniture_3.get_colour(), test_furniture_3.get_price())

        test_furniture_list = [test_furniture_2, test_furniture_1, test_furniture_3]
        database_furniture_list = furniture.sort_furniture_by_type(furniture.get_furniture_list(self.cursor))

        for i in range(len(test_furniture_list)):
            self.assertEqual(database_furniture_list[i], test_furniture_list[i], "Furniture sort by type unsuccessful")
        db.closeDatabase(self.connection)
    
    def test_3_sort_by_price(self):
        test_furniture_1 = furniture.Furniture(1, "Couch", "Brown", "99.99")
        test_furniture_2 = furniture.Furniture(2, "Chair", "Brown", "100.99")
        test_furniture_3 = furniture.Furniture(3, "Couch", "White", "80.99")

        test_furniture_list = [test_furniture_3, test_furniture_1, test_furniture_2]
        database_furniture_list = furniture.sort_furniture_by_price(furniture.get_furniture_list(self.cursor))

        for i in range(len(test_furniture_list)):
            self.assertEqual(database_furniture_list[i], test_furniture_list[i], "Furniture sort by price unsuccessful")
        db.closeDatabase(self.connection)
    
    def test_4_modify_furniture(self):
        test_furniture_1 = furniture.Furniture(1, "Couch", "Red", "99.99")
        test_furniture_2 = furniture.Furniture(2, "Chair", "Brown", "100.99")
        test_furniture_3 = furniture.Furniture(3, "Couch", "White", "80.99")

        furniture.update_furniture(self.connection, self.cursor, test_furniture_1.get_furniture_id(), test_furniture_1.get_type(), test_furniture_1.get_colour(), test_furniture_1.get_price())

        test_furniture_list = [test_furniture_1, test_furniture_2, test_furniture_3]
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        for i in range(len(test_furniture_list)):
            self.assertEqual(database_furniture_list[i], test_furniture_list[i], "Furniture modification unsuccessful")
        db.closeDatabase(self.connection)

    def test_5_remove_furniture(self):
        furniture.remove_furniture(self.connection, self.cursor, 1)
        furniture.remove_furniture(self.connection, self.cursor, 2)
        furniture.remove_furniture(self.connection, self.cursor, 3)

        test_furniture_list = []
        database_furniture_list = furniture.get_furniture_list(self.cursor)

        self.assertEqual(database_furniture_list, test_furniture_list, "Furniture removal unsuccessful")
        db.closeDatabase(self.connection) 
    def test_6_add_furniture_with_aisle_size(self):
        #add a furniture with an aisle, TDD should fail for now
        test_furniture = furniture.Furniture(5, "Lamp", "Silver", "45.00", "B2", "Small")
        test_furniture_list = [test_furniture]
        furniture.add_furniture(self.connection, self.cursor, test_furniture.get_furniture_id(), test_furniture.get_type(), test_furniture.get_colour(), test_furniture.get_price())
        database_furniture_list = furniture.get_furniture_list(self.cursor)
        self.assertEqual(database_furniture_list[0], test_furniture_list[0], "Furniture addition unsuccessful")
        db.closeDatabase(self.connection)
        
    def test_7_sort_by_aisle(self):
        test_furniture_1 = furniture.Furniture(1, "Couch", "Brown", "99.99")
        test_furniture_2 = furniture.Furniture(2, "Chair", "Brown", "100.99")
        test_furniture_3 = furniture.Furniture(3, "Couch", "White", "80.99")

        test_furniture_list = [test_furniture_3, test_furniture_1, test_furniture_2]
        database_furniture_list = furniture.sort_furniture_by_aisle(furniture.get_furniture_list(self.cursor))

        for i in range(len(test_furniture_list)):
            self.assertEqual(database_furniture_list[i], test_furniture_list[i], "Furniture sort by aisle unsuccessful")
        db.closeDatabase(self.connection)
    def test_8_sort_by_size(self):
        test_furniture_1 = furniture.Furniture(1, "Couch", "Brown", "99.99")
        test_furniture_2 = furniture.Furniture(2, "Chair", "Brown", "100.99")
        test_furniture_3 = furniture.Furniture(3, "Couch", "White", "80.99")

        test_furniture_list = [test_furniture_3, test_furniture_1, test_furniture_2]
        database_furniture_list = furniture.sort_furniture_by_size(furniture.get_furniture_list(self.cursor))

        for i in range(len(test_furniture_list)):
            self.assertEqual(database_furniture_list[i], test_furniture_list[i], "Furniture sort by aisle unsuccessful")
        db.closeDatabase(self.connection)




if __name__ == '__main__':
    unittest.main()
