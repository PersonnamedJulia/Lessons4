my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_new = [my_list[e1] for e1 in range(1, len(my_list)) if my_list[e1] > my_list[e1 - 1]]
print(my_list_new)