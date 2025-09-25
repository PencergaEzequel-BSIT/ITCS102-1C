print("ODD NUMBER SUM CALCULATOR")
print("Please enter 10 numbers. I will add up only the odd ones!\n")

odd_total = 0

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    
    if number % 2 != 0:
        odd_total += number

print(f"\nThe total sum of all odd numbers is: {odd_total}")
