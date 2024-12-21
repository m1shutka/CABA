from db_api import DBApi

class UserLogin():
    def fromDB(self, user_id):
        self.__user = DBApi().getUserInfo(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.__user['is_admin']

    def get_id(self):
        return str(self.__user['id'])
    
    def get_login(self):
        return self.__user['login']
    
    def get_user_sessions(self):
        self.__user_sessions = DBApi().getUserSessions(self.__user['id'])
        return self.__user_sessions





