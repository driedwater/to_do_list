from app import ToDoList

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. Edit task")
        print("5. View tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            try:
                todo_list.remove_task(task)
            except ValueError:
                print("Task not found.")
        elif choice == "3":
            task = input("Enter the task to mark as completed: ")
            try:
                todo_list.mark_task_as_completed(task)
            except ValueError:
                print("Task not found.")
        elif choice == "4":
            old_task = input("Enter the task to edit: ")
            new_task = input("Enter the new task: ")
            try:
                todo_list.edit_task(old_task, new_task)
            except ValueError:
                print("Task not found.")
        elif choice == "5":
            tasks = todo_list.view_tasks()
            if tasks:
                for i, task in enumerate(tasks, 1):
                    status = "Completed" if task["completed"] else "Not completed"
                    print(f"{i}. {task['task']} - {status}")
            else:
                print("No tasks in the to-do list.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
