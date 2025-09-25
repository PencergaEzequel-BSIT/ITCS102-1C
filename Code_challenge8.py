print("✨ MULTIPLICATION TABLE GENERATOR ✨")

number = int(input("🔢 Enter a number to see its magic table: "))

print(f"\n📊 Here’s the multiplication table for {number}:\n")

for i in range(1, 11):
    product = number * i
    print(f"👉 {number} × {i} = {product}")

print("\n🌟 Done! Now you’re a multiplication master! 🌟")
