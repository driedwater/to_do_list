class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, task):
        task_to_remove = None
        for t in self.tasks:
            if t["task"] == task:
                task_to_remove = t
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
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
        else:
            raise ValueError("Task not found")

    def view_tasks(self):
        return self.tasks
