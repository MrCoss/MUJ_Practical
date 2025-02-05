# Use a lambda function inside sorted() to sort a list of tuples based on the second value in each tuple.


# List of tuples
tuples_List =[(1,2),(3,4),(1,4),(1,1)]
sorted_list=sorted(tuples_List, key=lambda x:x[1])
print(sorted_list)