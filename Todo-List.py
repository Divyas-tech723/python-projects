todo_list = []

def add(text):
    todo_list.append(item)
    print("item added")

def delete(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index-1)
        print(f"deleted: {removed}")
    else:
        print("invalid input")

def show_result():
    if not todo_list:
        print("no tasks yet")
    else:
        for i,task in enumerate(todo_list,1):
            print(f"{i}.{task}")

while True:

    print("1.Add item\n 2.delete item\n 3.show item\n4.exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("enter item to add : ")
        add(item)

    elif choice == 2:
        show_result()

        try:
          idx = int(input("enter task no. to delet: "))
          delete(idx)

        except ValueError:
            print('please enter valid no.')

    elif choice == 3:
        show_result()

    elif choice == 4:
        break

    else:
        print("invalid input")