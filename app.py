import json

class ToDoList:
    def __init__(self, tasks_file="tasks.json"):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.tasks_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def remove_task(self, task):
        task_to_remove = None
        for t in self.tasks:
            if t["task"] == task:
                task_to_remove = t
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.save_tasks()
        else:
            raise ValueError("Task not found")

    def mark_task_as_completed(self, task):
        task_to_mark = None
        for t in self.tasks:
            if t["task"] == task:
                task_to_mark = t
                break
        if task_to_mark:
            task_to_mark["completed"] = True
            self.save_tasks()
        else:
            raise ValueError("Task not found")

    def edit_task(self, old_task, new_task):
        task_to_edit = None
        for t in self.tasks:
            if t["task"] == old_task:
                task_to_edit = t
                break
        if task_to_edit:
            task_to_edit["task"] = new_task
            self.save_tasks()
        else:
            raise ValueError("Task not found")

    def view_tasks(self):
        return self.tasks
