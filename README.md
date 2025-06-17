# Task Scheduler CLI

A simple Python CLI tool to manage your tasks — add, list, complete, and delete. Tasks are saved in a SQLite database so they stick around.

---

## Tech Used

- Python 3  
- SQLite  
- argparse for CLI parsing  
- OOP for clean code (Task, TaskManager classes)  

---

## How to Use

Run commands like these:

- Add a task:

  ```bash
  python3 main.py add --title "Buy groceries" --description "Milk, eggs, bread" --due "2025-06-20"

- List tasks:

  ```bash
  python3 main.py list

- Mark complete:

  ```bash  
  python3 main.py complete --id 1

- Delete tasks:

  ```bash  
  python3 main.py delete --id 1



