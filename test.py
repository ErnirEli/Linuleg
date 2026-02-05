# import math
# from time import time

# n = int(input())
# for k in range(1, n + 1):
#     start_time = time()
#     ernir = 0
#     for l in range(n):
#         ernir += 1

#     end_time = time()
    

#     print(f'{k}: {end_time-start_time:.9f}')
#     if end_time-start_time > 1:
#         break


# a = [1, 2]
# a.insert(-1, 99)
# print(a)

# a = [[1, 2]]*3
# a[0][3] = 1

# print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a.remove(min(a))
a.remove(min(a))
print(min(a))