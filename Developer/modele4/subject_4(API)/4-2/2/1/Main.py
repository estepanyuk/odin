from flask import Flask
from flask_restful import Api, Resource, reqparse
from User import User

app = Flask(__name__)
api = Api()

user1 = User(1, "ivan-ivanov1", "Ivan1", "Ivanov1", "ivan-ivanov1@email.com", "Ivan1", "100000000001", 1)
user2 = User(2, "petr-petrov", "Petr1", "Petrov1", "petr-petrov@email.com", "Petr1", "200000000002", 0)
user3 = User(3, "sidr-sidorov1", "Sidr1", "Sidorov1", "sidr-sidorov@email.com", "Sidr1", "300000000003", 1)

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
