print "Welcome to the TODO task management program!"

todo_list = []
print todo_list

while True:
    task = raw_input("Please enter a TODO task: ")

    todo_list.append(task)

    print "Your newest task is " + task

    print todo_list

    new = raw_input("Would you like to enter another task? yes/no ")

    if new.lower() == "no":
        break

    elif new.lower() != "no" and new.lower() != "yes":
        print "Yes or no only"

    else:
        continue

