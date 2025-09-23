numbers = [1.2, 4.0, 3.5, 8.6, 7.1, 2.0, 10.4, 9.9, 6.2, 5.3]

even_numbers = [num for num in numbers if num % 2 == 0]

if even_numbers:
    max_even = max(even_numbers)
    print("Жұп элементтердің максимумы:", max_even)
else:
    print("Жұп элементтер жоқ")


A = [
    [1, -2, 3, 4, -5, 6, -7, 8, 9, -10],
    [-1, 2, -3, 4, 5, -6, 7, -8, 9, 10],
    [1, 2, -3, -4, 5, 6, -7, 8, -9, 10],
    [-1, -2, 3, 4, -5, 6, 7, -8, 9, 10],
    [1, 2, 3, -4, -5, 6, 7, 8, -9, -10]
]

positive_count = 0
negative_count = 0

for row in A:
    for num in row:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

print("Оң сандар саны:", positive_count)
print("Теріс сандар саны:", negative_count)

if positive_count > negative_count:
    print("Оң сандар көбірек")
elif negative_count > positive_count:
    print("Теріс сандар көбірек")
else:
    print("Оң және теріс сандар саны тең")
