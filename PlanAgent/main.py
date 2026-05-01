
import json
import os

from agent.planner import TaskPlanner

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(task):
    planner = TaskPlanner()
    steps = planner.plan(task)

    tasks = load_tasks()
    for step in steps:
        tasks.append({"task": step, "done": False})
    save_tasks(tasks)

    print("\n[Agent] 已自动拆解任务：")
    for i, step in enumerate(steps):
        print(f"{i+1}. {step}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['task']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task completed!")
    else:
        print("Invalid index.")

def main():
    while True:
        print("\n=== AI Agent Todo CLI ===")
        print("1. Add Task (Agent 自动拆解)")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Task number: ")) - 1
            complete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
