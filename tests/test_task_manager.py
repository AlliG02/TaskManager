import unittest
from manager import TaskManager
from task import Task

# tests for the methods of the Task Manager class
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Use in-memory SQLite DB for isolated testing
        self.tm = TaskManager(":memory:")
    
    def test_add_task(self):
        self.tm.add_task("Test Task", "Test Description", "2025-06-18")
        tasks = self.tm.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")
        self.assertEqual(tasks[0].description, "Test Description")
        self.assertEqual(tasks[0].due_date, "2025-06-18")
        self.assertEqual(tasks[0].completed, 0)

    def test_mark_complete(self):
        self.tm.add_task("Incomplete Task", "Desc", "2025-06-18")
        task = self.tm.get_all_tasks()[0]
        self.tm.mark_complete(task.id)
        updated_task = self.tm.get_specific_task(task.id)
        self.assertEqual(updated_task.completed, 1)

    def test_delete_task(self):
        self.tm.add_task("Task to Delete", "Desc", "2025-06-18")
        task = self.tm.get_all_tasks()[0]
        self.tm.delete_task(task.id)
        deleted_task = self.tm.get_specific_task(task.id)
        self.assertIsNone(deleted_task)

    def test_get_specific_task_none(self):
        # Fetching a task that doesn't exist should return None
        self.assertIsNone(self.tm.get_specific_task(9999))

if __name__ == "__main__":
    unittest.main()
