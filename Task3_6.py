#Task3_6 Finding duplicates from three list
print("\n\nFind duplicates in three lists\n")

list1 = [14, 22, 33, 54]
list2 = [22, 33, 55, 76]
list3 = [33, 76, 57, 88]

duplicates = set(list1) & set(list2) & set(list3)
print("Duplicates in three lists:", list(duplicates))
