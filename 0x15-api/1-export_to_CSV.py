#!/usr/bin/python3
"""Python script to export data in the CSV format."""
from sys import argv
from requests import get
import csv


if __name__ == '__main__':
    apiEndpoint = 'https://jsonplaceholder.typicode.com'
    apiUser = get(apiEndpoint + '/users/' + argv[1]).json()['username']
    todos = get(apiEndpoint + '/todos?userId=' + argv[1]).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        fileWriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            fileWriter.writerow([argv[1], apiUser, todo['completed'], todo['title']])
