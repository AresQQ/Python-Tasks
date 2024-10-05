#Create two lists with 5 names each. Ensure some names are repeated (i.e., present in both lists). Display the repeated names.
list1 = ["Alice", "Bob", "Charlie", "David", "Emily"]
list2 = ["Charlie", "Fiona", "Alice", "George", "Emily"]

common_list = set(list1) & set(list2)
common_list_set = list(common_list) #we change set to make print look better
print("Powtarzające się imiona to", ", " .join(common_list_set)) #
