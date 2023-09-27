checklist = []

 # CREATE
def create(item):
    checklist.append(item)
# READ
def read(index):
    return checklist[index]
# UPDATE
def update(index, item):
    checklist[index] = item
# DESTROY
def destroy(index):
    checklist.pop(index)
# LISTING
def list_all_items():
    index = 0
    for list_item in checklist:
        print(list_item)

# def mark_completed(index):
    for list_item in checklist:
        print('√purple sox')

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        # where we want to stop the loop
        return False
    # Catch all
    else:
        print("Unknown Option")
        return True
    
        
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple sox")

    destroy(1)

    print(read(0))

    list_all_items()

    select("R")

    list_all_items()

test()

running = True 
while running:
    selection = user_input(
        "Press C to add to lst, R to read from list, P to display list, and Q to quit")
    running = select(selection)

