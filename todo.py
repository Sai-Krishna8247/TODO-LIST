import PySimpleGUI as sg
import os

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks

def main():
    layout = [
        [sg.Text("Enter Task:"), sg.InputText(key="task_input"), sg.Button("Add")],
        [sg.Listbox(values=[], size=(40, 10), key="task_list")],
        [sg.Button("Remove"), sg.Button("Mark Completed"), sg.Button("Save"), sg.Button("Exit")]
    ]

    window = sg.Window("To-Do List", layout)
    tasks = load_tasks()
    window["task_list"].update(values=tasks)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Add" and values["task_input"].strip() != "":
            task = values["task_input"].strip()
            tasks.append(task)
            window["task_list"].update(values=tasks)
            window["task_input"].update("")
        elif event == "Remove" and values["task_list"]:
            task = values["task_list"][0]
            tasks.remove(task)
            window["task_list"].update(values=tasks)
        elif event == "Mark Completed" and values["task_list"]:
            task = values["task_list"][0]
            index = tasks.index(task)
            tasks[index] = f"{task} (Completed)"
            window["task_list"].update(values=tasks)
        elif event == "Save":
            save_tasks(tasks)

    window.close()

if __name__ == "__main__":
    main()
