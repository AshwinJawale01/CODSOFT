# Create an empty list to store tasks
tasks = []

def print_welcome_message():
    print("/// To-Do List!")

def print_menu():
    print("\nPlease select an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Update a task")
    print("5. Quit the program")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)

def view_tasks():
    print("\nHere's your list of tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def complete_task():
    task_number = int(input("Enter the number of the task to complete: "))
    if task_number > 0 and task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' completed!")
    else:
        print("Sorry, that's an invalid option. Please try again.")

def update_task():
    task_number = int(input("Enter the number of the task to update: "))
    if task_number > 0 and task_number <= len(tasks):
        updated_task = input("Enter the updated task: ")
        tasks[task_number - 1] = updated_task
        print(f"Task '{updated_task}' updated!")
    else:
        print("Sorry, that's an invalid option. Please try again.")

def main():
    print_welcome_message()

    while True:
        print_menu()
        choice = input("Enter the number of your option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            print("\nThanks for using the Python To-Do List! Have a great day!")
            break
        else:
            print("Sorry, that is not a valid option. Please try again.")

if __name__ == "__main__":
    main()