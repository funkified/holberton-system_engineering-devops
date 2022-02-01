#!/usr/bin/python3
"""
REST API script
"""

import requests
from sys import argv
import csv


if __name__ == '__main__':

    employee_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))

    name_employee = user.json()['name']
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employee_id))
    todo = todo.json()

    with open("{}.csv".format(employee_id), 'w') as cFile:
        for data in todo:
            cFile.write(
                    '"{}","{}","{}","{}"\n'.format(employee_id,
                                                   name_employee,
                                                   data['completed'],
                                                   data['title']))
