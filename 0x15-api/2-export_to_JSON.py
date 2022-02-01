#!/usr/bin/python3
"""
REST API script
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    employee_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))

    name_employee = user.json()['username']
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employee_id))
    todo = todo.json()

    json_dict = {}
    json_dict[employee_id] = []

    for data in todo:
        json_dict[employee_id].append({
                  'task': data['title'],
                  'completed': data['completed'],
                  'username': name_employee
        })

        with open("{}.json".format(employee_id), 'w') as jFile:
            json.dump(json_dict, jFile)
