#!/bin/bash/python3
"""
REST API script
"""

import requests
from sys import argv

if __name__ == '__main__':
    employee_id = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(employee_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id)).json()

    done_task = []
    for task in todo:
        if task.get('completed') is True:
            done_task.append(task.get('title'))
    print("Employee {} is done with tasks([]/[]):".
          format(user.get('name'), len(done_task), len(todo)))
    for done in done_task:
        print('\t {}'.format(done))

