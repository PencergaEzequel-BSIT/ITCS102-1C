halaga = eval(input("Ilagay ang halaga ng ide-deposito: "))

print("\nNarito ang breakdown ng iyong deposito:")

libo = halaga // 1000
halaga %= 1000

limandaang = halaga // 500
halaga %= 500

dalawangdaan = halaga // 200
halaga %= 200

daan = halaga // 100
halaga %= 100

limampu = halaga // 50
halaga %= 50

bente = halaga // 20
halaga %= 20

sampu = halaga // 10
halaga %= 10

lima = halaga // 5
halaga %= 5

isa = halaga // 1
halaga %= 1

print("₱1000: ", libo)
print("₱500: ", limandaang)
print("₱200: ", dalawangdaan)
print("₱100: ", daan)
print("₱50: ", limampu)
print("₱20: ", bente)
print("₱10: ", sampu)
print("₱5: ", lima)
print("₱1: ", isa)
