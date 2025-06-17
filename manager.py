import sqlite3
from task import Task

class TaskManager:
    def __init__(self, dbname="tasks.db"):
        # create connection to database and store in conn object 
        self.conn = sqlite3.connect(dbname)
        self._create_table() 

    # static method as it needs object. Creates a table for tasks. 
    # execute method allows us to run sql commands
    def _create_table(self):
        self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        description TEXT,
                        due_date TEXT,
                        completed INTEGER
                    )
                ''')
        self.conn.commit()

    # method to add task entries to the database
    def add_task(self, title, description, due_date):
        self.conn.execute(
            "INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, 0)",
            (title, description, due_date)
        )
        self.conn.commit()

    # wrap tuples in Task objects
    def get_all_tasks(self):
        cursor = self.conn.execute("SELECT id, title, description, due_date, completed FROM tasks")
        rows = cursor.fetchall()
        tasks = [Task(*row) for row in rows]
        return tasks

    def delete_task(self, id):
        if id is None:
            raise ValueError("ID must exist")
        self.conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()

    def get_specifc_task(self, id):
        cursor = self.conn.execute(
        "SELECT id, title, description, due_date, completed FROM tasks WHERE id = ?",
        (id,)
        )
        # get the row of the tuple 
        row = cursor.fetchone()
        if row:
            return Task(*row)  # Now you can use __str__ on this (converts into Task object)
        else:
            return None
    
    def mark_complete(self, id):
        # update the database
        self.conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (id,))
        self.conn.commit()
        print(f"Task {id} marked as complete.")
