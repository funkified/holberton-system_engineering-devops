#!/usr/bin/python3
"""
REST API script
"""
import json
from requests import *
from sys import argv

if __name__ == '__main__':

    user = get('https://jsonplaceholder.typicode.com/users')
    user = user.json()

    toDoList = {}

    for usrID in user:
        employee_id = usrID['id']
        name_employee = usrID['username']

        todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(employee_id)).json()

        json_list = []

        for data in todo:
            json_list.append({
                'username': name_employee,
                'task': data['title'],
                'completed': data['completed']
            })

        toDoList[usrID.get('id')] = json_list

    with open("todo_all_employess.json", 'w') as jFile:
        json.dump(toDoList, jFile)
