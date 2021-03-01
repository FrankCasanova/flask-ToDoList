from flask_login import UserMixin
from .firestore_service import get_user


class UserData:
    def __init__(self,user_name,password) -> None:
        self.user_name = user_name
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data) -> None:

        """
        :param user_data: UserDAta
        """

        self.id = user_data.user_name
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            user_name=user_doc.id,
            password=user_doc.to_dict()['password']
        )    
        return UserModel(user_data)    

    