import os
import sys
from datetime import date

TODO_FILE = '/todo.txt'
DONE_FILE = '/done.txt'

# ========= HELPER FUNCTIONS =========

def display_help():
    output = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    print(output, end='')
    print()

def check_length(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return len(lines)

def prepend_text(new_item, file_name):
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(new_item + '\n')
        for i in lines:
            f.writelines(i)

def display_todos():
    length = check_length(TODO_FILE)
    if length == 0:
        print('There are no pending todos!', end='')
    else:
        with open(TODO_FILE, 'r') as f:
            lines = f.readlines()
            for i in lines:
                num = f'[{length}]'
                i = i.strip('\n')
                print(f'{num} {i}')
                length -= 1

def delete_todo(id):
    length = check_length(TODO_FILE)
    if id > length or id <= 0:
        print(f'Error: todo #{id} does not exist. Nothing deleted.', end='')
        return (False, None)
    
    with open(TODO_FILE, 'r') as f:
        lines = f.readlines()
    content = lines.pop(-id).strip('\n')
    with open(TODO_FILE, 'w') as f:
        for line in lines:
            f.writelines(line)
    return (True, content)

def done_todo(id):
    flag, content = delete_todo(id)
    if not flag:
        return False
    curr_date = date.today().strftime('%Y-%m-%d')
    content = f'x {curr_date} ' + content
    prepend_text(content, DONE_FILE)
    return True

# ========= MAIN CODE =========

if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'w') as f:
        pass

if not os.path.exists(DONE_FILE):
    with open(DONE_FILE, 'w') as f:
        pass

args_len = len(sys.argv)

if args_len == 1 or sys.argv[1] == 'help':
  display_help()

elif sys.argv[1] == 'add':
    if args_len == 3:
        prepend_text(sys.argv[2], TODO_FILE)
        print(f'Added todo: "{sys.argv[2]}"', end='')
    else:
        print('Error: Missing todo string. Nothing added!', end='')
    print()

elif sys.argv[1] == 'ls':
    display_todos()

elif sys.argv[1] == 'del':
    if args_len == 2:
        print('Error: Missing NUMBER for deleting todo.', end='')
    else:
        id = int(sys.argv[2])
        flag, content = delete_todo(id)
        if flag:
            print(f'Deleted todo #{id}', end='')
    print()

elif sys.argv[1] == 'done':
    if args_len == 2:
        print('Error: Missing NUMBER for marking todo as done.', end='')
    else:
        id = int(sys.argv[2])
        flag = done_todo(id)
        if flag:
            print(f'Marked todo #{id} as done.', end='')
    print()

elif sys.argv[1] == 'report':
    pending = check_length(TODO_FILE)
    completed = check_length(DONE_FILE)
    curr_date = date.today().strftime('%Y-%m-%d')
    print(f'{curr_date} Pending : {pending} Completed : {completed}', end='')
    print()

else:
    display_help()