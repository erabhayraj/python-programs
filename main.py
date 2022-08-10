def main_menu():
    print("\nPress...")
    print("[1] Write data")
    print("[2] Access data")
    print("[x] Exit")
    return input("Enter command: ")


def person():
    print("\nChoose...")
    print("[1] Harry")
    print("[2] Rohan")
    print("[3] Abhay")
    print("[x] Exit")
    return input("Enter command: ")


def plan():
    print("\nChoose...")
    print("[1] Diet Plan")
    print("[2] Exercise Plan")
    print("[x] Exit")
    return input("Enter command: ")


def getdate():
    import datetime
    return datetime.datetime.now()


def add_diet_exercise(date_of_diet, diet_exercise, filename):
    f = open(filename, "a")
    f.write(str(date_of_diet))
    writable_diet_exercise = "    " + diet_exercise + "\n"
    f.write(writable_diet_exercise)
    print("Saved Successfully!!")
    f.close()


def add():
    command2 = person()
    while command2 != 'x':
        if command2 == '1':
            add_plan_of_person("harry")
        elif command2 == '2':
            add_plan_of_person("rohan")
        elif command2 == '3':
            add_plan_of_person("abhay")
        elif command2 != 'x':
            print("Invalid command")
        command2 = person()


def add_plan_of_person(name_of_person):
    command3 = plan()
    command3 = command3.upper()
    while command3 != 'x':
        print(command3)
        if command3 == '1':
            date = getdate()
            file_name = name_of_person + "diet.txt"
            new_diet_exercise = input("Enter your diet: ")
            add_diet_exercise(date, new_diet_exercise, file_name)
        elif command3 == '2':
            date = getdate()
            file_name = name_of_person + "exercise.txt"
            new_diet_exercise = input("Enter your exercise with no of set: ")
            add_diet_exercise(date, new_diet_exercise, file_name)
        elif command3 != 'x':
            print("Invalid command")
        command3 = plan()


def access_fitness(date_of_access, filename):
    find = False
    f = open(filename, "r")
    read_data = f.read(10)
    while read_data != "":
        if read_data == date_of_access:
            find = True
            f.seek(f.tell() - 10)
            print(f.readline(), end="")
        else:
            f.seek(f.tell() - 10)
            f.readline()
        read_data = f.read(10)
    if find == 0:
        print("No data exists!!")
    f.close()


def access():
    command2 = person()
    while command2 != 'x':
        if command2 == '1':
            access_plan_of_person("harry")
        elif command2 == '2':
            access_plan_of_person("rohan")
        elif command2 == '3':
            access_plan_of_person("abhay")
        elif command2 != 'x':
            print("Invalid command")
        command2 = person()


def access_plan_of_person(name_of_person):
    command3 = plan()
    command3 = command3.upper()
    while command3 != 'x':
        if command3 == '1':
            date = input("Enter the date of which you want to access (yyyy-mm-dd): ")
            file_name = name_of_person + "diet.txt"
            access_fitness(date, file_name)
        elif command3 == '2':
            date = input("Enter the date of which you want to access (yyyy-mm-dd): ")
            file_name = name_of_person + "exercise.txt"
            access_fitness(date, file_name)
        elif command3 != 'x':
            print("Invalid command")
        command3 = plan()


print("-----Health Management System-----")
command = main_menu()
while command != 'x':
    if command == '1':
        add()
    elif command == '2':
        access()
    elif command != 'x':
        print("Invalid command")
    command = main_menu()
print("Thanks for visiting!!!")
