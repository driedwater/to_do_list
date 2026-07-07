from app import ToDoList

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
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
            tasks = todo_list.view_tasks()
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks in the to-do list.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
