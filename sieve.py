# Sieve of Eratosthenes
# create list of numbers - delete multiples of each number one by one - return remaining list
# MAXIMUM SIEVE ACTION

n = 120
numbers = [i for i in range(2, n+1)]
# [numbers.remove(m) for m in [i*j for i in numbers for j in numbers if i*j in numbers] if m in numbers]
for i in numbers:
    multiples = []
    for j in numbers:
        if i*j in numbers:
            multiples.append(i*j)
    for m in multiples:
        numbers.remove(m)
print(numbers)

# Wrong logic below
# n = 120
# list_of_numbers = [i for i in range(2, n+1)]

# for number1 in list_of_numbers:
#     for number2 in list_of_numbers:
#         if number1 != number2:
#             if number2 % number1 == 0:
#                 list_of_numbers.remove(number2)
# print(list_of_numbers)
