class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print("Task completed!")
        except IndexError:
            print("Invalid task number.")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Quit")
        option = input("Choose an option: ")
        if option == "1":
            task = input("Enter a task: ")
            to_do_list.add_task(task)
        elif option == "2":
            to_do_list.view_tasks()
        elif option == "3":
            task_number = int(input("Enter the task number to complete: "))
            to_do_list.complete_task(task_number)
        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()