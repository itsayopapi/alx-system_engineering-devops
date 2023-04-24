#!/usr/bin/python3
"""Python script to export data in the JSON format."""
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    apiEndpoint = 'https://jsonplaceholder.typicode.com'
    apiUsers = get(apiEndpoint + '/users/').json()
    todos = get(apiEndpoint + '/todos/').json()

    k, apiRecords = 0, []
    apiId, user, all = apiUsers[k]['id'], apiUsers[k]['username'], {}

    for todo in todos:
        if todo['userId'] != apiId:
            all[apiId] = apiRecords
            k += 1
            apiId, user = apiUsers[k]['id'], apiUsers[k]['username']
            records = []
        apiRecords.append({'username': user, 'task': todo['title'],
                           'completed': todo['completed']})

    all[apiId] = records
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all, file)
