'''
1.To-Do List Application:
Create a command-line or web-based to-do list application where users can
add, delete, and mark tasks as completed.
'''


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def delete_task(self, index):
        try:
            del self.tasks[index]
        except IndexError:
            print("Task index out of range!")

    def mark_completed(self, index):
        try:
            self.tasks[index].completed = True
        except IndexError:
            print("Task index out of range!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Mark task as completed")
        print("4. Display tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
