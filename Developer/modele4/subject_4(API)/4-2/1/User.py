import json


class User:
    id = 0
    user_name = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
    phone = ""
    user_status = 0

    def __init__(self, *nums):
        if len(nums) == 1:
            data = json.loads(nums[0].replace("'", "\""))
            self.id = data["id"]
            self.user_name = data["username"]
            self.first_name = data["firstName"]
            self.last_name = data["lastName"]
            self.email = data["email"]
            self.password = data["password"]
            self.phone = data["phone"]
            self.user_status = data["userStatus"]
        else:
            self.id = nums[0]
            self.user_name = nums[1]
            self.first_name = nums[2]
            self.last_name = nums[3]
            self.email = nums[4]
            self.password = nums[5]
            self.phone = nums[6]
            self.user_status = nums[7]

    def toStr(self):
        dict_data = {"id": self.id,
                     "username": self.user_name,
                     "firstName": self.first_name,
                     "lastName": self.last_name,
                     "email": self.email,
                     "password": self.password,
                     "phone": self.phone,
                     "userStatus": self.user_status}
        return json.dumps(dict_data)
