#   Q.1

# Create a list
numbers = [10, 5, 8, 2, 15]
# Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
# Add elements
numbers.append(20)
numbers.insert(2, 12)
print("After adding elements:", numbers)
# Remove elements
numbers.remove(5)
numbers.pop()
print("After removing elements:", numbers)
# Sort list
numbers.sort()
print("Sorted list:", numbers)


#Q.2
# Create sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Access elements
print("Set1:", set1)
print("Set2:", set2)
# Union
union_set = set1.union(set2)
print("Union of sets:", union_set)
# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)


#Q.3
# Create tuple
tup = (1, 2, 3, 4)
print("Tuple:", tup)
# Access elements
print("First element:", tup[0])
print("Last element:", tup[-1])
# Nested tuple
nested_tup = (tup, (5, 6, 7))
print("Nested Tuple:", nested_tup)
# Repetition of tuple
repeated_tup = tup * 3
print("Repeated Tuple:", repeated_tup)


#Q.4
# Create dictionary
student = {
    "name": "Alisha",
    "roll_no": 101,
    "marks": 85
}
# Access elements
print("Name:", student["name"])
print("Marks:", student["marks"])
# Update dictionary
student["marks"] = 90
student["grade"] = "A"
print("Updated Dictionary:", student)
# Remove elements
student.pop("roll_no")
print("After removing roll_no:", student)
# Merge dictionaries
extra_info = {"course": "BTech CSE", "year": 1}
merged_dict = student | extra_info
print("Merged Dictionary:", merged_dict)
