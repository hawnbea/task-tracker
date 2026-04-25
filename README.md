# Task Tracker CLI

This is my first project in Python. This is a simple task manager to track and manage tasks.

## Installation

Clone and repo and install
git clone https://github.com/hawnbea/task-tracker.git
cd task-tracker
pip3 install -e .

## Usage

# Add a task
tasks add "Buy groceries"
# List all tasks
tasks list

# List by status
tasks list todo
tasks list in-progress
tasks list done

# Update a task
tasks update 1 "Buy groceries and cook dinner"

# Mark a task
tasks mark-in-progress 1
tasks mark-done 1

# Delete a task
tasks delete 1