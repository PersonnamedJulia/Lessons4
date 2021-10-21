my_list = list(input().split())
my_list_new = [int(my_list[e1 - 1]) for e1 in range(2, len(my_list), 1) if my_list[e1 - 1] != my_list[e1]]
print(my_list_new)