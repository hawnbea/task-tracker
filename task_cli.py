#!/usr/bin/env python3
import json
import sys

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def get_next_id(tasks):
    if len(tasks) == 0:
        return 1
    else:
        new_id = 0
        for task in tasks:
            if task["id"] > new_id:
                new_id = task["id"]
        return new_id + 1

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if status is None or task["status"] == status:
            print(f"{task}")

def delete_task(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break
    save_tasks(tasks)
    print(f"Task {id} deleted successfully")

def update_task(id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["description"] = new_description
            break
    save_tasks(tasks)
    print(f"Task {id} updated successfully")

def update_status(id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = new_status
            break
    save_tasks(tasks)
    print(f"Task {id} set to {new_status}")

def main():
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])
    elif command == "list":
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    elif command == "update":
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "mark-in-progress":
        update_status(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        update_status(int(sys.argv[2]), "done")

if __name__ == "__main__":
    main()