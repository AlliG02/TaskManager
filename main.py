import argparse
from manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Task Scheduler CLI")
    parser.add_argument("command", choices=["add", "list", "complete", "delete", "get"])
    parser.add_argument("--title")
    parser.add_argument("--description")
    parser.add_argument("--due")
    parser.add_argument("--id", type=int)

    args = parser.parse_args()
    tm = TaskManager()

    if args.command == "add":
        tm.add_task(args.title, args.description, args.due)
    elif args.command == "list":
        tasks = tm.get_all_tasks()
        for task in tasks:
            print(task)
    elif args.command == "complete":
        tm.mark_complete(args.id)
    elif args.command == "delete":
        tm.delete_task(args.id)
    elif args.command == "get":
        print(tm.get_specifc_task(args.id))

if __name__ == "__main__":
    main()