shopping_list = ["apples", "bread", "milk"]

# append() is a method that adds an item to the end of a list
shopping_list.append("cheese")
print("Appended list : ", shopping_list) 

# insert() is a method that adds an item to a specific index in a list
shopping_list.insert(1, "eggs")
print("Inserted list : ", shopping_list)

# del is a keyword that deletes an item from a list
del shopping_list[0]
print("Deleted list : ", shopping_list)

# remove() is a method that removes an item from a list
shopping_list.remove("bread")
print("Removed list : ", shopping_list)

# pop() is a method that removes an item from a list at a specific index
shopping_list.pop(1)
print("Popped list : ", shopping_list)

# copy() is a method that creates a copy of a list
new_list = shopping_list.copy()
print("Copied list : ", new_list)

# sort() is a method that sorts a list in ascending order
numbers = [4, 2, 3, 1]
numbers.sort()
print("Sorted Number list : ", numbers)
#string list
string_list = ["banana", "cherry", "apple"]
string_list.sort()
print("Sorted string list : ", string_list)

# reverse() is a method that reverses the order of a list
numbers.reverse()
print("Reversed Number list : ", numbers)

# clear() is a method that removes all items from a list
numbers.clear()
print("Cleared Number list : ", numbers)

# count() is a method that returns the number of times an item appears in a list
print("Count of apples : ", shopping_list.count("apples"))

# index() is a method that returns the index of the first occurrence of an item in a list
print("Index of apples : ", shopping_list.index("apples"))

# extend() is a method that adds the elements of a list to the end of another list
shopping_list.extend(["bread", "milk"])
print("Extended list : ", shopping_list)

# len() is a function that returns the number of items in a list
print("Length of list : ", len(shopping_list))

# max() is a function that returns the largest item in a list
numbers = [4, 2, 3, 1]
print("Max of numbers : ", max(numbers))

# min() is a function that returns the smallest item in a list
print("Min of numbers : ", min(numbers))

# sum() is a function that returns the sum of all items in a list
print("Sum of numbers : ", sum(numbers))

# in is a keyword that checks if an item is in a list
print("Is apples in list : ", "apples" in shopping_list)

# not in is a keyword that checks if an item is not in a list
print("Is apples not in list : ", "apples" not in shopping_list)


