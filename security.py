from werkzeug.security import safe_str_cmp
from models.user import UserModel

# users = [
#     UserModel(1, 'tom', 'abc')
# ]
# 
# username_mapping = {u.username: u for u in users}
# 
# userid_mapping = {i.id: i for i in users}

def authenticate(username, password):
#   user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
#   return userid_mapping.get(user_id, None)

