
tasks = [] # Initialize an empty list to store tasks

def add_task():
    # Ask the user to enter a task
    task_description = input("Enter the task description: ")

    # Add the task to the list
    tasks.append(task_description)

    # Confirm that the task was added
    print(f"Task '{task_description}' added successfully!")

if __name__ == "__main__":
    add_task() # Only run main() if this file is executed directly