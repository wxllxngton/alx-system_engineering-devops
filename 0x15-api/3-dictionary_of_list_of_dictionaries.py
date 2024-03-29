#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
and exports data in CSV and JSON formats.
"""

from requests import get
from json import dump
from sys import argv
import csv


def fetch(url):
    """
    Fetches data from the provided URL.

    Parameters:
        - url (str): URL to fetch from.

    Returns:
        - data in JSON format.
    """
    r = get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
        exit(1)

    return r.json()


def fetch_user_data(employee_id):
    """
    Fetches user data from the API.

    Parameters:
        - employee_id (int): Employee ID.

    Returns:
        - Tuple containing user data and todo data.
    """
    try:
        data_users = fetch(
            "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        )
        data_todos = fetch("https://jsonplaceholder.typicode.com/todos/")
        return data_users, data_todos
    except KeyError as e:
        print("KeyError: " + str(e))
        exit(1)
    except Exception as e:
        print("Exception: " + str(e))
        exit(1)


def get_employee_progress(employee_id):
    """
    Retrieves and prints the progress of an employee's TODO list.

    Parameters:
        - employee_id (int): Employee ID.

    Returns:
        - None
    """
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        exit(1)

    completed = 0
    total = 0
    tasks = []

    try:
        data_users, data_todos = fetch_user_data(employee_id)

        for data in data_todos:
            if data.get("userId") == employee_id:
                total += 1
                if data.get("completed") is True:
                    completed += 1
                    tasks.append(data.get("title"))

        print(
            "Employee {} is done with tasks({}/{}):".format(
                data_users.get("name"), completed, total
            )
        )

        for task in tasks:
            print("\t {}".format(task))

    except KeyError as e:
        print("KeyError: " + str(e))
        exit(1)
    except Exception as e:
        print("Exception: " + str(e))
        exit(1)


def export_to_csv(employee_id):
    """
    Exports employee tasks to CSV.

    Parameters:
        - employee_id (int): Employee ID.

    Returns:
        - None
    """
    data_users, data_todos = fetch_user_data(employee_id)

    with open("{}{}".format(employee_id, ".csv"), "w", newline="") as file:
        file_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for data in data_todos:
            if data.get("userId") == employee_id:
                file_writer.writerow(
                    [
                        employee_id,
                        data_users.get("username"),
                        data.get("completed"),
                        data.get("title"),
                    ]
                )


def export_to_json(employee_id):
    """
    Exports employee tasks to JSON.

    Parameters:
        - employee_id (int): Employee ID.

    Returns:
        - None
    """
    user_tasks = {employee_id: []}
    data_users, data_todos = fetch_user_data(employee_id)

    for data in data_todos:
        if data["userId"] == employee_id:
            new_dict = {
                "task": data.get("title"),
                "completed": data.get("completed"),
                "username": data_users.get("username"),
            }
            user_tasks[employee_id].append(new_dict)

    with open("{}{}".format(employee_id, ".json"), "w", newline="") as file:
        dump(user_tasks, file)


def export_all_to_json():
    """
    Exports all employee tasks to JSON.

    Returns:
        - None
    """
    user_tasks = {}
    data_todos = fetch("https://jsonplaceholder.typicode.com/todos/")
    data_users = fetch("https://jsonplaceholder.typicode.com/users/")

    with open("todo_all_employees.json", "w", newline="") as file:
        for user_data in data_users:
            user_id = user_data.get("id")
            for todo_data in data_todos:
                if user_id == (todo_data.get("userId")):
                    # Append to dictionary if user exists
                    if user_id in user_tasks:
                        user_tasks[user_id].append(
                            {
                                "task": todo_data.get("title"),
                                "completed": todo_data.get("completed"),
                                "username": user_data.get("username"),
                            }
                        )
                    # Else, add new list
                    else:
                        user_tasks[(user_id)] = [
                            {
                                "task": todo_data.get("title"),
                                "completed": todo_data.get("completed"),
                                "username": user_data.get("username"),
                            }
                        ]

        dump(user_tasks, file)


if __name__ == "__main__":
    # if len(argv) != 2:
    #     print("Usage: ./{} {}".format(argv[0], "<employee_id>"))
    #     exit(1)

    # get_employee_progress(argv[1])
    # export_to_csv(argv[1])
    # export_to_json(argv[1])
    export_all_to_json()
