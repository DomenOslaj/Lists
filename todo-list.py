print "Welcome to the TODO task management program!"

todo_list = []
print todo_list

while True:
    task = raw_input("Please enter a TODO task: ")

    todo_list.append(task)  # this way we add the task to todo_list

    print "Your newest task is " + task

    print todo_list

    new = raw_input("Would you like to enter another task? yes/no ")

    if new.lower() == "no":
        print "Your todo list looks like that:"
        for item in todo_list:                # for loop prints each variable in a list on a separate line
            print item
        break


