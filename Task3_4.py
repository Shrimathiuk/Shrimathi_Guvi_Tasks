# Task 3_4: Sum of the first and last digit of an integer
print("\n\nSum of the first and last digit of an integer\n")

digit = ''
def Sum_of_FirstandLastDigitOf(numer):
    digit = str(numer)
    sum = int(digit[0]) + int(digit[-1])
    return sum

num = 12345
print(f"Sum of the ( {str(num)[0]} ) first and ( {str(num)[-1]} ) last digit of an integer is : ", Sum_of_FirstandLastDigitOf(num))
