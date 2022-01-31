#!/usr/bin/python3
"""
REST API script
"""

import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(employee_id))

    name_employee = user.json()['name']
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employee_id))
    todo = todo.json()

    task_list = []
    done_task = 0
    for task in todo:
        if task['completed'] is True:
            done_task += 1
            task_list.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".
          format(name_employee, done_task, len(todo)))

    for done in range(len(task_list)):
        print("\t {}".format(task_list[done]))
