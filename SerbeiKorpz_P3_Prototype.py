def clear_screen():
    for i in range(50):
        print()

def pause():
    print()
    input("Press Enter to continue...")

def show_menu():
    print("===== 2 DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================")

def is_number(text):
    if text == "":
        return False
    for letter in text:
        if letter not in "0123456789":
            return False
    return True

def get_task_number():
    number = input("Enter task number: ")
    while is_number(number) == False:
        print("Please enter a valid number.")
        number = input("Enter task number: ")
    return int(number)

def add_task(tasks, statuses):
    task = input("Enter task description: ")
    while task.strip() == "":
        print("Task description cannot be empty. Please try again.")
        task = input("Enter task description: ")
    tasks.append(task)
    statuses.append("Pending")
    print("Task added successfully.")

def view_tasks(tasks, statuses):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i] + " [" + statuses[i] + "]")

def complete_task(tasks, statuses):
    view_tasks(tasks, statuses)
    if len(tasks) == 0:
        return
    print()
    number = get_task_number()
    if number >= 1 and number <= len(tasks):
        statuses[number - 1] = "Completed"
        print("Task marked as completed.")
    else:
        print("Invalid number.")

def delete_task(tasks, statuses):
    view_tasks(tasks, statuses)
    if len(tasks) == 0:
        return
    print()
    number = get_task_number()
    if number >= 1 and number <= len(tasks):
        tasks (number - 1)
        statuses.pop(number - 1)
        print("Task deleted successfully.")
    else:
        print("Invalid number.")

def start():
    tasks = []
    statuses = []

    running = True
    while running == True:
        clear_screen()
        show_menu()
        choice = input("Enter your choice (1-5): ")
        print("==========================")
        print()

        if choice == "1":
            add_task(tasks, statuses)
        elif choice == "2":
            view_tasks(tasks, statuses)
        elif choice == "3":
            complete_task(tasks, statuses)
        elif choice == "4":
            delete_task(tasks, statuses)
        elif choice == "5":
            print("Thank you for using the 2 Do List!")
            running = False
        else:
            print("Invalid choice. Please try again.")

        if running == True:
            pause()

start()