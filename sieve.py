# Sieve of Eratosthenes

n = 120
list_of_numbers = [i for i in range(2, n+1)]

for number1 in list_of_numbers:
    for number2 in list_of_numbers:
        if number1 != number2:
            if number2 % number1 == 0:
                list_of_numbers.remove(number2)
print(list_of_numbers)
