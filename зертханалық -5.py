my_list = [1, 2, 3, 4, 5]
reversed_list = []

i = len(my_list) - 1
while i >= 0:
    reversed_list.append(my_list[i])
    i -= 1

print("Кері тізім:", reversed_list)

def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

nums = [-10, 5, -3, 7, -1]
print(list_sort(nums))  # [-10, 7, 5, -3, -1]

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [1, 2, 3, 4]
print(change(my_list))  # [4, 2, 3, 1]
