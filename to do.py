class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print('Task "{}" added successfully.'.format(task))

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print('Task "{}" removed successfully.'.format(task))
        else:
            print('Task "{}" not found.'.format(task))

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, 1):
                print('{}. {}'.format(i, task))

# Example Usage
todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)

    elif choice == '2':
        task = input("Enter the task to remove: ")
        todo_list.remove_task(task)

    elif choice == '3':
        todo_list.view_tasks()

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
