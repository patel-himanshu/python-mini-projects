# Todo App (CLI-based)

This program was created as a part of programming task for CoronaSafe Engineering Fellowship. The following content was mentioned in the specifications given by CoronaSafe in their problem statement.

Here's a demo of the Todo app as desired by CoronaSafe.
[![Todo-CLI](https://res.cloudinary.com/sv-co/image/upload/v1607935139/fullstack-CEF/Todo-CLI/play-video-demo_fp50wp.png)](https://vimeo.com/490621534)

## Usage

### 1. Help

Executing the command without any arguments, or with a single argument `help` prints the CLI usage.

```
$ ./python todo.py help
Usage :-
$ ./python todo.py add "todo item"  # Add a new todo
$ ./python todo.py ls               # Show remaining todos
$ ./python todo.py del NUMBER       # Delete a todo
$ ./python todo.py done NUMBER      # Complete a todo
$ ./python todo.py help             # Show usage
$ ./python todo.py report           # Statistics
```

### 2. List all pending todos

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo should be displayed first.

```
$ ./python todo.py ls
[2] change light bulb
[1] water the plants
```

### 3. Add a new todo

Use the `add` command. The text of the todo item should be enclosed within double quotes (otherwise only the first word is considered as the todo text, and the remaining words are treated as different arguments).

```
$ ./python todo.py add "the thing i need to do"
Added todo: "the thing i need to do"
```

### 4. Delete a todo item

Use the `del` command to remove a todo item by its number.

```
$ ./python todo.py del 3
Deleted todo #3
```

Attempting to delete a non-existent todo item should display an error message.

```
$ ./python todo.py del 5
Error: todo #5 does not exist. Nothing deleted.
```

### 5. Mark a todo item as completed

Use the `done` command to mark a todo item as completed by its number.

```
$ ./python todo.py done 1
Marked todo #1 as done.
```

Attempting to mark a non-existed todo item as completed will display an error message.

```
$ ./python todo.py done 5
Error: todo #5 does not exist.
```

### 6. Generate a report

Use the `report` command to see the latest tally of pending and completed todos.

```
$ ./python todo.py report
yyyy-mm-dd Pending : 1 Completed : 4
```