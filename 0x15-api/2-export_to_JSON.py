#!/usr/bin/python3
'''
This Python script to export data in the JSON format.

'''


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id))
    username = user.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={'userId': user_id})
    todos = todos.json()

    emp = {}
    emp[user_id] = []

    for tasks in todos:
        t = {}
        t['username'] = username
        t['task'] = tasks.get('title')
        t['completed'] = tasks.get('completed')
        emp[user_id].append(t)

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(emp, f)
