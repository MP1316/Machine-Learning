def task():
    task_list = []         
    print("---WELCOME TO THE TASK MANAGEMENT SYSTEM---")

    total_tasks = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter  task {i}= ")
        task_list.append(task_name)

    print(f"Task added successfully! \n '{task_name}' ")

    while True:
            operation = int(input("Do you want to add another task \n 1-add\n 2-update\n 3-delete\n 4-view\n 5-exit/stop: "))
            if operation == 1:
                add = input("Enter the name of the task you want to add: ")
                task_list.append(add)
                print(f"Task added successfully! \n '{add}' ")

            elif operation == 2:
                update = input("Enter the name of the task you want to update: ")
                if update in task_list:
                    new_task = input("Enter the new name for the task: ")
                    index = task_list.index(update)
                    task_list[index] = new_task
                    print(f"Task updated successfully! \n '{update}' is now '{new_task}' ")
                else:
                    print("Task not found.")
                    
            elif operation == 3:
                del_val = input("Which task you want to delete =  ")
                if del_val in task_list:
                    task_list.remove(del_val)
                    print(f"Task deleted successfully! \n '{del_val}' ")
                else:
                    print("Task not found.")

            elif operation == 4:
                print(f"Total tasks = {task_list}:")

            elif operation == 5:
                print("Exiting the Task Management System.")
                break
            else:
                print("Invalid operation. Please try again.")

task()
