from flask import Flask
from flask_restful import Api, Resource, reqparse
from User import User

app = Flask(__name__)
api = Api()

user1 = User(1, "ivan-ivanov", "ivan1", "Ivanov1", "ivan-ivanov1@email.ru", "qwerty1", "111111111", 1)
user2 = User(2, "petr-petrov", "petr1", "Petrov", "petr-petrov1@email.ru", "qwerty2", "222222222", 0)
user3 = User(3, "sidr-sidorov", "sidr1", "Sidorov1", "sidr-sidorov1@email.ru", "qwerty3", "3333333333", 1)

users = {user1.id:user1, user2.id:user2, user3.id:user3}

def getUserDict():
    userDict = {}
    for key in users:
        userDict[users[key].id] = users[key].toDict()
    return userDict

parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("username", type=str)
parser.add_argument("firstName", type=str)
parser.add_argument("lastName", type=str)
parser.add_argument("email", type=str)
parser.add_argument("password", type=str)
parser.add_argument("phone", type=str)
parser.add_argument("userStatus", type=int)

class Main(Resource):
    def get(self, user_id):
        if user_id == 0:
            return getUserDict()
        else:
            return getUserDict()[user_id]

    def delete(self, user_id):
        del users[user_id]
        return getUserDict()

    def post(self, user_id):
        users[user_id] = User(parser.parse_args())
        return getUserDict()

    def put(self, user_id):
        users[user_id] = User(parser.parse_args())
        return getUserDict()


class Main2(Resource):
    def get(self):
        return getUserDict()

api.add_resource(Main, "/api/users/<int:user_id>")
api.add_resource(Main2, "/api/users")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
