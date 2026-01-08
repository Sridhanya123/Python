initial_items=["milk","bread","eggs"]

def add_item(item):
    initial_items.append(item)

def remove_item(item):
    initial_items.pop()

def display_item(item):
    return lambda item:print("item:",item)

def count(item):
    if len(item)==0:
       return 0
    else:
        return len(item[0])+len(item[1:])
    print

