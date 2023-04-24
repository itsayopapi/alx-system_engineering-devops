#!/usr/bin/python3
"""Python script to export data in the JSON format."""
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    apiEndpoint = 'https://jsonplaceholder.typicode.com'
    apiUser = get(apiEndpoint + '/users/' + argv[1]).json()['username']
    todos = get(apiEndpoint + '/todos?userId=' + argv[1]).json()

    record, userData, group = {}, {}, []
    for todo in todos:
        record['task'] = todo['title']
        record['completed'] = todo['completed']
        record['username'] = apiUser
        group.append(record)
        record = {}

    userData[argv[1]] = group

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(userData, file)
