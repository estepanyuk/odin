import requests
import datetime

from User import User

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}


def postUser(user, status_code):
    response = requests.post(
        "https://petstore.swagger.io/v2/user",
        headers=headers,
        data=user.toStr()
    )
    assert_equals(status_code,
                  response.status_code,
                  "StatusCode does not match")


def getUser(user_name, status_code):
    response = requests.get(
        "https://petstore.swagger.io/v2/user/" + user_name
    )
    assert_equals(status_code, response.status_code, "StatusCode does not match")
    return response.json()


def putUser(user, status_code):
    response = requests.put(
        "https://petstore.swagger.io/v2/user/" + user.user_name,
        headers=headers,
        data=user.toStr()
    )
    assert_equals(status_code, response.status_code, "StatusCode does not match")


def deleteUser(user_name, status_code):
    response = requests.delete(
        "https://petstore.swagger.io/v2/user/" + user_name
    )
    assert_equals(status_code, response.status_code, "StatusCode does not match")


def assert_equals(expected, actual, message):
    if expected != actual:
        raise ValueError(message + "\nExpected: " + str(expected) + "\nActual:   " + str(actual))


total_seconds = int((datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()) - 63800000000

# Step 1
reference_user = User(
    total_seconds,
    "ivan" + str(total_seconds),
    "Vladimir",
    "Ivanov1",
    "ivan-ivanov1@email.ru",
    "qwerty1",
    "111111111",
    1
)
postUser(reference_user, 200)

# Step 2
createdUser = User(str(getUser(reference_user.user_name, 200)))
print(createdUser.toStr())

assert_equals(reference_user.id, createdUser.id, "id юзеров не совпадают")
assert_equals(reference_user.user_name, createdUser.user_name, "user_name юзеров не совпадают")
assert_equals(reference_user.first_name, createdUser.first_name, "first_name юзеров не совпадают")
assert_equals(reference_user.last_name, createdUser.last_name, "last_name юзеров не совпадают")
assert_equals(reference_user.email, createdUser.email, "email юзеров не совпадают")
assert_equals(reference_user.password, createdUser.password, "password юзеров не совпадают")
assert_equals(reference_user.phone, createdUser.phone, "Id phone не совпадают")
assert_equals(reference_user.user_status, createdUser.user_status, "user_status юзеров не совпадают")

# Step 3
reference_user.first_name = "Ivan2"
reference_user.last_name = "Vladimir2"
reference_user.email = "ivan-ivanov2@email.ru"
reference_user.password = "qwerty2"
reference_user.phone = "222222222"
reference_user.user_status = 2

putUser(reference_user, 200)

# Step 4
updateUser = User(str(getUser(reference_user.user_name, 200)))
print(updateUser.toStr())

assert_equals(reference_user.id, updateUser.id, "id юзера не совпадает")
assert_equals(reference_user.user_name, updateUser.user_name, "user_name юзера не совпадает")
assert_equals(reference_user.first_name, updateUser.first_name, "first_name юзера не совпадает")
assert_equals(reference_user.last_name, updateUser.last_name, "last_name юзера не совпадает")
assert_equals(reference_user.email, updateUser.email, "email юзера не совпадает")
assert_equals(reference_user.password, updateUser.password, "password юзера не совпадает")
assert_equals(reference_user.phone, updateUser.phone, "phone юзера не совпадает")
assert_equals(reference_user.user_status, updateUser.user_status, "phone юзера не совпадает")

# Step 5
deleteUser(reference_user.user_name, 200)

# Step 6
getUser(reference_user.user_name, 404)
