import math

print('Binary search algoritm example.')

def binary_search(target_list, item):
    low = 0
    high = len(target_list)-1

    while low <= high:
        mid = math.ceil((low+high)/2)
        guess = target_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

my_list = [1, 3, 4, 5, 9, 12, 15, 17, 22]

print(binary_search(my_list, 3))
print(binary_search(my_list, 1))