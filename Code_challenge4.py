print("Welcome to Manga Recommender!")
print("Choose your preference:")

genre = input("Pick a genre (romance, action, horror): ").lower()
era = input("Pick an era (90s, 2000s, 2010s): ").lower()

if genre == "romance":
    if era == "90s":
        print("Recommendation: Boys Be... (1991)")
    elif era == "2000s":
        print("Recommendation: Lovely★Complex (2001)")
    elif era == "2010s":
        print("Recommendation: Ao Haru Ride (2011)")
    else:
        print("No romance manga found for that era.")

elif genre == "action":
    if era == "90s":
        print("Recommendation: Rurouni Kenshin (1994)")
    elif era == "2000s":
        print("Recommendation: Naruto (1999-2014)")
    elif era == "2010s":
        print("Recommendation: Attack on Titan (2009)")
    else:
        print("No action manga found for that era.")

elif genre == "horror":
    if era == "90s":
        print("Recommendation: Uzumaki (1998)")
    elif era == "2000s":
        print("Recommendation: Goth (2002)")
    elif era == "2010s":
        print("Recommendation: Ajin (2012)")
    else:
        print("No horror manga found for that era.")

else:
    print("Sorry, I don't recognize that genre.")
