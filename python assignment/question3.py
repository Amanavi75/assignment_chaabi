#Column Sorting, yay!
#Given a list of dicts, write a program to sort the list according to a key given in input.
#E.g.
#Input f([
#{"fruit": "orange", "color": "orange"},
#{"fruit": "apple", "color": "red"},
#{"fruit": "banana", "color": "yellow"},
#{"fruit": "blueberry", "color": "blue"}
#], "fruit")
#Should Output
#[
#{"fruit": "apple", "color": "red"},
#{"fruit": "banana", "color": "yellow"},
#{"fruit": "blueberry", "color": "blue"},
#{"fruit": "orange", "color": "orange"}



def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

input_list1 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

input_list2 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list1 = sort_list_of_dicts(input_list1, "fruit")
sorted_list2 = sort_list_of_dicts(input_list2, "color")

print(sorted_list1)
print(sorted_list2)
