import requests
import datetime

from User import User

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

def postUser(user, status_code):
    response = requests.post(
        "https://petstore.swagger.io/v2/user/",
        headers=headers,
        data=user.toStr()
    )
    assert_equals(status_code, response.status_code, "StatusCode does not math")


def getUser(user_name, status_code):
    response = requests.get(
        "https://petstore.swagger.io/v2/user/" + user_name
    )
    assert_equals(status_code, response.status_code, "StatusCode does not math")
    return response.json()


def putUser(user, status_code):
    response = requests.put(
        "https://petstore.swagger.io/v2/user/" + user.user_name,
        headers=headers,
        data=user.toStr()
    )
    assert_equals(status_code, response.status_code, "StatusCode does not math")


def deleteUser(user_name, status_code):
    response = requests.delete(
        "https://petstore.swagger.io/v2/user/" + user_name
    )
    assert_equals(status_code, response.status_code, "StatusCode does not math")


def assert_equals(expected, actual, message):
    if expected != actual:
        raise ValueError(message + "\nExpected: " + str(expected) + "\nActual: " + str(actual))


total_seconds = int((datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()) - 6380000000

# step1
reference_user = User(
    total_seconds,
    "Ivan" + str(total_seconds),
    "Ivanovich",
    "Ivanov1",
    "Ivan-Ivanov@email.com",
    "qwerty1234",
    "1111111111",
    1
)
postUser(reference_user, 200)

# step2
createdUser = User(str(getUser(reference_user.user_name, 200)))
print(createdUser.toStr())

assert_equals(reference_user.id, createdUser.id, "id юзера не совпадает")
assert_equals(reference_user.user_name, createdUser.user_name, "user_name юзера не совпадает")
assert_equals(reference_user.first_name, createdUser.first_name, "first_name юзера не совпадает")
assert_equals(reference_user.last_name, createdUser.last_name, "last_name юзера не совпадает")
assert_equals(reference_user.email, createdUser.email, "email юзера не совпадает")
assert_equals(reference_user.password, createdUser.password, "password юзера не совпадает")
assert_equals(reference_user.phone, createdUser.phone, "phone юзера не совпадает")
assert_equals(reference_user.user_status, createdUser.user_status, "user_status юзера не совпадает")

# step 3
reference_user.first_name = "Ivan2"
reference_user.last_name = "Vladimir"
reference_user.email = "Ivan-Ivanov2@email.com"
reference_user.user_status = 2

putUser(reference_user, 200)

# step 4
updatedUser = User(str(getUser(reference_user.user_name, 200)))
print(updatedUser.toStr())

assert_equals(reference_user.id, updatedUser.id, "id юзера не совпадает")
assert_equals(reference_user.user_name, updatedUser.user_name, "user_name юзера не совпадает")
assert_equals(reference_user.first_name, updatedUser.first_name, "first_name юзера не совпадает")
assert_equals(reference_user.last_name, updatedUser.last_name, "last_name юзера не совпадает")
assert_equals(reference_user.email, updatedUser.email, "email юзера не совпадает")
assert_equals(reference_user.password, updatedUser.password, "password юзера не совпадает")
assert_equals(reference_user.phone, updatedUser.phone, "phone юзера не совпадает")
assert_equals(reference_user.user_status, updatedUser.user_status, "user_status юзера не совпадает")

# step 5
deleteUser(reference_user.user_name, 200)

# step 6
getUser(reference_user.user_name, 404)
