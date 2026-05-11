import json
import os

# Filename where tasks will be stored
DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If file doesn't exist, return empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def display_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("List is empty!")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task['done'] else "❌"
                print(f"{i}. {task['title']} [{status}]")

        elif choice == '2':
            title = input("Enter task title: ")
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added!")

        elif choice == '3':
            try:
                idx = int(input("Enter task number to mark done: ")) - 1
                tasks[idx]['done'] = True
                save_tasks(tasks)
                print("Task updated!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '4':
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                tasks.pop(idx)
                save_tasks(tasks)
                print("Task deleted!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()