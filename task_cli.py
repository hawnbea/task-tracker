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

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])