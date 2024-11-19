class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, task):
        task_id = self.next_id
        self.tasks[task_id] = {"task": task, "completed": False}
        self.next_id += 1
        print(f"Task added: {task} (ID: {task_id})")

    def view_tasks(self):
        for task_id, task in self.tasks.items():
            status = "Completed" if task["completed"] else "Pending"
            print(f"{task_id}. {task['task']} ({status})")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} completed!")
        else:
            print("Invalid task ID.")

    def edit_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id]["task"] = new_task
            print(f"Task {task_id} updated: {new_task}")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted!")
        else:
            print("Invalid task ID.")

def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Manager:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Quit")
        option = input("Choose an option: ")
        if option == "1":
            task = input("Enter a task: ")
            task_manager.add_task(task)
        elif option == "2":
            task_manager.view_tasks()
        elif option == "3":
            task_id = int(input("Enter the task ID to complete: "))
            task_manager.complete_task(task_id)
        elif option == "4":
            task_id = int(input("Enter the task ID to edit: "))
            new_task = input("Enter the new task: ")
            task_manager.edit_task(task_id, new_task)
        elif option == "5":
            task_id = int(input("Enter the task ID to delete: "))
            task_manager.delete_task(task_id)
        elif option == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()