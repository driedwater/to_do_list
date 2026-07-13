import unittest
from main import app

class TestToDoApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset tasks before each test
        from main import tasks
        tasks.clear()
        tasks.append("initial task")


    def test_main_page_loads(self):
        """Test that the main page loads correctly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'To-Do List', response.data)
        self.assertIn(b'initial task', response.data)

    def test_add_new_task(self):
        """Test that a new task can be added."""
        response = self.app.post('/add', data=dict(newTask='A New Task'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'A New Task', response.data)
        self.assertIn(b'initial task', response.data)

    def test_complete_a_task(self):
        """Test that a task can be marked as complete."""
        response = self.app.post('/complete', data=dict(taskCheckbox='1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'initial task - Completed', response.data)

    def test_delete_a_task(self):
        """Test that a task can be deleted."""
        # Add a task to be deleted
        self.app.post('/add', data=dict(newTask='Task to delete'), follow_redirects=True)
        #Now delete the first task
        response = self.app.post('/delete', data=dict(taskCheckbox='1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'initial task', response.data)
        self.assertIn(b'Task to delete', response.data)

    def test_delete_multiple_tasks(self):
        """Test that multiple tasks can be deleted."""
        self.app.post('/add', data=dict(newTask='Task 2'), follow_redirects=True)
        self.app.post('/add', data=dict(newTask='Task 3'), follow_redirects=True)
        response = self.app.post('/delete', data=dict(taskCheckbox=['1', '3']), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'initial task', response.data)
        self.assertIn(b'Task 2', response.data)
        self.assertNotIn(b'Task 3', response.data)


if __name__ == '__main__':
    unittest.main()
