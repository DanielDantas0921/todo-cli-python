import argparse 
import json_custom
import generate_id
import date_and_hour

def addTask(description):
    object = {"id": generate_id.generate_id(), "description": description, "status": "todo" ,"createdAt": date_and_hour.formate_date_and_hour(), "updatedAt": None }
    dados = json_custom.read_json("tasks.json")
    if dados is None:
        json_custom.write_json("tasks.json", [object])
    else:
        dados.append(object)
        json_custom.write_json("tasks.json", dados)

def updateTask(id, description):
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = date_and_hour.formate_date_and_hour()
        json_custom.write_json("tasks.json", dados)

def deleteTask(id):
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["id"] == id:
            dados.remove(task)
    json_custom.write_json("tasks.json", dados)

def listTasks():
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        print(f"id: {task['id']}, description: {task['description']}")

def listTasksAreDone():
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["status"] == "done":
            print(f"id: {task['id']}, description: {task['description']}")

def listTasksToDo():
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["status"] == "todo": 
            print(f"id: {task['id']}, description: {task['description']}")

def listTasksInProgress():
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["status"] == "in_progress":
            print(f"id: {task['id']}, description: {task['description']}")

def markInProgress(id):
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["id"] == id:
            task["status"] = "in_progress"
    json_custom.write_json("tasks.json", dados)

def markDone(id):
    dados = json_custom.read_json("tasks.json")
    for task in dados:
        if task["id"] == id:
            task["status"] = "done"
    json_custom.write_json("tasks.json", dados)

def run_cli():
    parser = argparse.ArgumentParser(description=  "Task Tracker")

    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")
    
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="Task description")

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")

    parser_list = subparsers.add_parser("list", help="List all tasks")
    list_subparsers = parser_list.add_subparsers(dest="subcommand")

    list_done = list_subparsers.add_parser("done", help="List done tasks")
    list_todo = list_subparsers.add_parser("todo", help="List todo tasks")
    list_in_progress = list_subparsers.add_parser("in-progress", help="List in progress tasks")


    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_mark_in_progress.add_argument("id", type=int, help="Task ID")

    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="Task ID")
    

    args = parser.parse_args()
    if args.command == "add":
        if args.description:
            addTask(args.description)
    elif args.command == "update":
        if args.id and args.description:
            updateTask(args.id, args.description)
    elif args.command == "delete":
        if args.id:
            deleteTask(args.id)
    elif args.command == "list":
        if args.subcommand == "done":
            listTasksAreDone()
        elif args.subcommand == "todo":
            listTasksToDo()
        elif args.subcommand == "in-progress":
            listTasksInProgress()
        else:
            listTasks()
    elif args.command == "mark-in-progress":
        if args.id:
            markInProgress(args.id)
    elif args.command == "mark-done":
        if args.id:
            markDone(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    run_cli()