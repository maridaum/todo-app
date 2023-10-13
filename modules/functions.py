def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(list, filepath="files/todos.txt"):
    """ Write todos to a text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(list)