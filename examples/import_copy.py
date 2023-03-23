from copy import copy, deepcopy

list1 = [[1, 2], [3, 4]]
list2 = deepcopy(list1)

list2[0][0] = 0

print(list1)  # [[1, 2], [3, 4]]
print(list2)  # [[1, 2], [3, 4]]


list1 = [[1, 2], [3, 4]]
list2 = copy(list1)
list3 = list1.copy()

list2[0][1] = 0

print(list1)  # [[1, 2], [3, 4]]
print(list2)  # [[1, 2], [3, 4]]
print(list3)  # [[1, 2], [3, 4]]
