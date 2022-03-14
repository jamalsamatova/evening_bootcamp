import json

users = []

with open('../db.json', 'r+') as f:
    python_data = json.load(f)
    # print(type(python_data))
    users = python_data['users']

print(users)

def send_message(users):
    for user in users:
        if int(user['age']) >= 18:
            print(f"hello, {user['name']}! We have special offer for you!")

send_message(users)
