print("🎬 Welcome to the Movie Recommender!")
print("Answer a few quick questions to find a good movie.\n")

genre = input("What do you feel like watching? (action, comedy, drama): ").lower()
mood = input("Do you want something short, medium, or long?: ").lower()
decade = input("Do you want a movie from the 1990s, 2000s, or 2010s?: ").lower()

if genre == "action":
    if mood == "short" and decade == "1990s":
        print("\nRecommendation: 'Rush Hour' (1998)")
    elif mood == "medium" and decade == "2000s":
        print("\nRecommendation: 'The Dark Knight' (2008)")
    else:
        print("\nRecommendation: 'Avengers: Endgame' (2019)")

elif genre == "comedy":
    if mood == "short" and decade == "2000s":
        print("\nRecommendation: 'School of Rock' (2003)")
    elif mood == "medium" and decade == "2010s":
        print("\nRecommendation: 'The Big Sick' (2017)")
    else:
        print("\nRecommendation: 'Dumb and Dumber' (1994)")

elif genre == "drama":
    if mood == "medium" and decade == "1990s":
        print("\nRecommendation: 'The Shawshank Redemption' (1994)")
    elif mood == "long" and decade == "2000s":
        print("\nRecommendation: 'Gladiator' (2000)")
    else:
        print("\nRecommendation: 'La La Land' (2016)")

else:
    print("\n❌ Sorry, I don’t have a recommendation for that choice.")

