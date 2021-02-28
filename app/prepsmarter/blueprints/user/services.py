from prepsmarter.blueprints.user.models import User
import datetime
from prepsmarter.blueprints.user.hashers import get_hashed_password

class UserRepository():
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table  
    
    def add_user(self, User):
        sql = "INSERT INTO users (email, password, is_active, sign_in_count, current_sign_in_on, last_sign_in_on) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = self.conn.cursor()
        cursor.execute(sql, ( User.email, User.password, User.active, User.sign_in_count, User.current_sign_in_on, User.last_sign_in_on))
        resp = cursor.fetchall()
        return resp
    
    def delete_user(self):
        return ""
    
    def get_user(self):
        return ""
    
    def save(self):
        self.conn.commit()
    


class UserService():
    def register_user(self,
                      email,
                      password,
                      registration_date,
                      active,
                      sign_in_count,
                      current_sign_in_on,
                      last_sign_in_on):
        new_user = User(email, password, registration_date, active,
                        sign_in_count, current_sign_in_on, last_sign_in_on)
        return new_user

    def desactivate_user(self, User):
        if User.active == False:
            print(f"User {User.email} is already inactive")
        User.active = False

    def reactive_user(self, User):
        if User.active == True:
            print(f"User {User.email} is already active")
        User.active = True

    def is_active(self, User):
        return User.is_active

    def update_activity_tracking(self, User, ip_address):
        User.sign_in_count += 1
        User.last_sign_in_on = User.current_sign_in_on
        User.current_sign_in_on = datetime.datetime.now()

    def update_password(self, User, new_password):
        User.password = get_hashed_password(new_password)

