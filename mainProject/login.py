from databasefunction import returnLogin

# Simple class to represent login details
class Login:
    def __init__(self, staff_id, level, username, password):
        self.staff_id = staff_id
        self.level = level
        self.username = username
        self.password = password
    
    def __str__(self):
        levels = ['admin', 'manager', 'employee']
        return f"ID: {self.staff_id}, Username: {self.username}, Password: {self.password}, Access Level: {levels[self.level - 1]}"
    
    def get_staff_id(self):
        return self.staff_id
    
    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
        return
    
    def get_level(self):
        return self.level
    
    def set_level(self, level):
        self.level = level
        return
    
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username
        return
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
        return
    
def get_login_list(cursor):
    raw_stuff = returnLogin(cursor)
    login_list = []
    for row in raw_stuff:
        login_list.append(Login(row[0], row[1], row[2], row[3]))
    return login_list