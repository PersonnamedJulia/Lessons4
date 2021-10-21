my_list = [e1 for e1 in range(100, 1001) if e1 % 2 == 0]
from functools import reduce
print(reduce(lambda a, b: a * b, my_list))