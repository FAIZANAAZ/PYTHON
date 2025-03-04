# uv add click


# 📌 Complete Code with Comments

import click  # CLI commands create karne ke liye Click library import ki
import json  # JSON file me data store aur retrieve karne ke liye import ki
import os  # File ka existence check karne ke liye OS module import kiya

TODO_FILE = "todo.json"  # JSON file jisme tasks store honge


# ✅ Function: Tasks ko JSON file se load karne ke liye
def load_tasks():
    if not os.path.exists(TODO_FILE):  # Agar file exist nahi karti
        return []  # To empty list return kar do
    with open(TODO_FILE, "r") as file:  # File read mode me open karo
        return json.load(file)  # File ka data load karke list me return karo


# ✅ Function: Tasks ko JSON file me save karne ke liye
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:  # File write mode me open karo
        json.dump(tasks, file, indent=4)  # JSON format me store karo (indent ke saath)


@click.group()  # CLI commands ka group define kar raha hai
def cli():
    """Simple To-Do List Manager"""  # CLI ka description
    pass  # Yahan koi direct action nahi ho raha


# ✅ Command: Naya task add karne ke liye
@click.command()
@click.argument("task")  # User se task ka naam argument me lega
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()  # Pehle existing tasks load karo
    tasks.append({"task": task, "done": False})  # Naya task list me add karo (default: not done)
    save_tasks(tasks)  # Updated list wapas file me save karo
    click.echo(f"Task added: {task}")  # Success message show karo


# ✅ Command: Sare tasks list karne ke liye
@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()  # Pehle tasks load karo
    if not tasks:  # Agar list empty hai
        click.echo("No tasks found!")  # Message show karo
        return  # Function yahin end ho jaye
    for index, task in enumerate(tasks, 1):  # Loop chalakar tasks print karo (1 se numbering)
        status = "✓" if task["done"] else "✗"  # Agar task complete hai to "✓", warna "✗"
        click.echo(f"{index}. {task['task']} [{status}]")  # Task print karo status ke saath


# ✅ Command: Task ko complete mark karne ke liye
@click.command()
@click.argument("task_number", type=int)  # User task ka number dega
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()  # Pehle tasks load karo
    if 0 < task_number <= len(tasks):  # Agar valid task number diya hai
        tasks[task_number - 1]["done"] = True  # Task ko "done" mark karo
        save_tasks(tasks)  # Updated list wapas file me save karo
        click.echo(f"Task {task_number} marked as completed!")  # Success message show karo
    else:
        click.echo("Invalid task number.")  # Agar galat number hai to error message


# ✅ Command: Task ko delete karne ke liye
@click.command()
@click.argument("task_number", type=int)  # User task ka number dega
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()  # Pehle tasks load karo
    if 0 < task_number <= len(tasks):  # Agar valid task number diya hai
        removed_task = tasks.pop(task_number - 1)  # Task list se remove karo
        save_tasks(tasks)  # Updated list wapas file me save karo
        click.echo(f"Removed task: {removed_task['task']}")  # Success message show karo
    else:
        click.echo("Invalid task number.")  # Agar galat number hai to error message


# ✅ CLI commands ko CLI group me add karna
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)


# ✅ Script direct run hone par CLI start karna
if __name__ == "__main__":
    cli()  # CLI commands enable karo




# 📌 Summary (Ye Code Kya Karta Hai?)

# 1. Tasks ko JSON file me store aur retrieve karta hai.


# 2. 4 CLI Commands support karta hai:

# add: Naya task add karne ke liye

# list: Sare tasks dekhne ke liye

# complete: Kisi task ko complete mark karne ke liye

# remove: Kisi task ko delete karne ke liye



# 3. CLI ko click library se control karta hai.


# 4. Agar script direct run ho rahi ho (_name_ == "_main_"), to CLI enable hoti hai.






# 📌 Example Usage in Terminal

# python todo.py add "Buy milk"

# Task added: Buy milk

# python todo.py list

# 1. Buy milk [✗]

# python todo.py complete 1

# Task 1 marked as completed!

# python todo.py list

# 1. Buy milk [✓]

# python todo.py remove 1

# Removed task: Buy milk


