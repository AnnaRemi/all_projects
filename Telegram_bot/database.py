from constant import *
from pymongo import MongoClient
import datetime


class Database(object):
    _client = MongoClient('localhost', 27017)
    _db = _client.db
    _users = _db.test_collection

    def create_new_user(self, user_id):
        if self._users.find_one({'user_id': user_id}) is None:
            new_user = {'user_id': user_id, 'name': '0', 'age': '0', 'zodiac': '0', 'plans': [],
                        'time': '0', 'updated': False}
            self._users.insert_one(new_user)

    def update(self, user_id: int, key, value):
        if key == 'plans':
            plans = self.get_data(user_id, 'plans')
            plans.append(value)
            self._users.update_one({'user_id': user_id}, {'$set': {key: plans}})
        else:
            self._users.update_one({'user_id': user_id}, {'$set': {key: value}})

    def get_data(self, user_id, key):
        try:
            current = self._users.find_one({'user_id': user_id})
            return current[key]
        except Exception:
            return None

    def get_users_id(self):
        lst = []
        for user in self._users.find():
            lst.append(user['user_id'])
        return lst
