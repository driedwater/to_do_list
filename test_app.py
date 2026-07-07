import unittest
from app import ToDoList

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), ["Task 1"])

    def test_add_multiple_tasks(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.assertEqual(self.todo_list.view_tasks(), ["Task 1", "Task 2"])

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), ["Task 2"])

    def test_remove_task_not_found(self):
        with self.assertRaises(ValueError):
            self.todo_list.remove_task("Task 1")

    def test_view_tasks(self):
        self.assertEqual(self.todo_list.view_tasks(), [])
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.view_tasks(), ["Task 1"])

if __name__ == '__main__':
    unittest.main()
