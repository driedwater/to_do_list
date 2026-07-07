import unittest
import os
import json
from app import ToDoList

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.test_tasks_file = "test_tasks.json"
        self.todo_list = ToDoList(self.test_tasks_file)

    def tearDown(self):
        if os.path.exists(self.test_tasks_file):
            os.remove(self.test_tasks_file)

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), [{"task": "Task 1", "completed": False}])

    def test_add_multiple_tasks(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.assertEqual(self.todo_list.view_tasks(), [{"task": "Task 1", "completed": False}, {"task": "Task 2", "completed": False}])

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), [{"task": "Task 2", "completed": False}])

    def test_remove_task_not_found(self):
        with self.assertRaises(ValueError):
            self.todo_list.remove_task("Task 1")

    def test_view_tasks(self):
        self.assertEqual(self.todo_list.view_tasks(), [])
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), [{"task": "Task 1", "completed": False}])

    def test_mark_task_as_completed(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.mark_task_as_completed("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), [{"task": "Task 1", "completed": True}])

    def test_mark_task_as_completed_not_found(self):
        with self.assertRaises(ValueError):
            self.todo_list.mark_task_as_completed("Task 1")

    def test_save_and_load_tasks(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.mark_task_as_completed("Task 1")
        
        # Create a new ToDoList instance to load the tasks from the file
        new_todo_list = ToDoList(self.test_tasks_file)
        self.assertEqual(new_todo_list.view_tasks(), [{"task": "Task 1", "completed": True}, {"task": "Task 2", "completed": False}])

if __name__ == '__main__':
    unittest.main()
