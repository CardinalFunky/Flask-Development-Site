from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user):
        self.user = user

    @staticmethod
    def is_authenticated(self):
        return True

    @staticmethod
    def is_active(self):
        return True

    @staticmethod
    def is_anonymous(self):
        return False

    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user.get('_id')
        return str(object_id)