name = input("Hello! What’s your name? → ")

print("++++++++++++++++++")
print()
print("ODD NUMBER CHECKER — type 0 to end the program")
print()
print("++++++++++++++++++")

number = int(input("Enter any number → "))
total = 0
odd_numbers = ""

while number != 0:
    if number % 2 != 0:
        print(f"{number} is an ODD number.")
        total += number
        odd_numbers += str(number) + " "
    else:
        print(f"{number} is an EVEN number.")

    number = int(input("Enter another number → "))

print(f"\nHi {name}, the sum of all odd numbers is {total}.")
print(f"The odd numbers you entered were: {odd_numbers}")
