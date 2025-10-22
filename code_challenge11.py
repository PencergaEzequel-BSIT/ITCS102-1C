print("\t\t *", end="")
for a in range(1,11):
    for b in range(11,a,-1):
        print("", end=" ")
    for c in range(1,a):
        print("*", end=" ")
    for d in range(1,a):
        print("*", end=" ")
print()
