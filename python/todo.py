"""A simple command-line todo list manager."""
import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Add a task to the todo list."""
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task+"\n")
        
    
    

def list_tasks():
    """List all tasks to user"""
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    output_string = ""
    for i, task in enumerate(tasks, start=1):
        output_string += f"{i}. {task.strip()}\n"
        
    return output_string.rstrip("\n")


def remove_task(index):
    """Remove task from to-do list"""
    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        if len(tasks) == 0:
            print("This list is empty!")
            return
        elif index < 1 or index > len(tasks):
            print ("Invalid task number!")
            return
        else:
            index = index - 1
            tasks.pop(index)
            with open(TASK_FILE, "w" , encoding="utf-8") as file:
                file.writelines(tasks)
                return
    
            print (tasks)
            return            
  

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
