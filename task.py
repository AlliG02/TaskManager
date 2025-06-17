class Task:
    # constructor in python 
    def __init__(self, id, title, description, due_date, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
    # function that returns a readable string of an object 
    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.id}: {self.title} (Due: {self.due_date})"