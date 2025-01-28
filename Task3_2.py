# Task 3_2: Count and create a list of prime numbers

prime_numbers = []
number = [10, 105, 22, 37, 100, 999, 87, 351, 2, 5]
if len(number) < 2:
    print("Not a prime")
elif len(number) > 1:
    for num in number:
        if num % 2 == 0:
            prime_numbers.append(num)
print("Prime numbers from the given list: ",prime_numbers)
print("Count of Prime numbers in the list: ",len(prime_numbers))