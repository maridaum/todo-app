from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n" # this extracts part of the string starting at this index

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos] alternative way to remove extra line break

        print(f"You have {len(todos)} todos.")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            index = number - 1
            todo_removed = todos[index].strip("\n")
            todos.pop(index)


            functions.write_todos(todos)

            print(f"You completed {todo_removed}")
            print("Todos remaining:")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")
        except IndexError:
            print("There is no todo with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Exiting app")

