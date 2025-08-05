# Task definition:
# Task: name of the task
# Completed: () (x)


def adding_task(tasks, task_name):

    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' has been added")
    return

def see_tasks(tasks):
    print("\n See your current to-do list:")
    for index, task in enumerate(tasks, start =1):
        status = "✔" if task["completed"] else ""
        task_name = task["name"]
        print(f"{index}. [{status}], {task_name}")
    return

tasks = []

while True:
    print("\n Menu to for managing tasks/to-do-list")
    print("1. Add a task")
    print("2. See tasks")
    print("3. Update a task")
    print("4. Mark task as completed")
    print("5. Delete complete task(s)")
    print("6. Exit")

    user_input = input("Please choose an item: ")

    if user_input == "1":
        task_name = input("Please add your task:")
        adding_task(tasks, task_name)
    elif user_input == "2":
        see_tasks(tasks)
    elif user_input == "6":
        break