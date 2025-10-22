animes = []

while True:
    title = input("Type an anime title (or enter 'exit' to stop): ")
    if title.lower() == "exit":
        break
    animes.append(title)
    print(f"Added '{title}' to your list.")

print("\nYou’ve left the anime input program.")
print("Here are the animes you listed:")
for item in animes:
    print(f"- {item}")
