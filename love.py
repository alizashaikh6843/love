import random

def love_calculator():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter the first person's name: ").lower()
    name2 = input("Enter the second person's name: ").lower()

    # Combine the two names and count the number of occurrences of 'true' and 'love'
    combined_name = name1 + name2
    true_count = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
    love_count = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

    # Calculate the love score
    love_score = int(str(true_count) + str(love_count))

    print(f"Your Love Score is: {love_score}%")

    if love_score < 10 or love_score > 90:
        print("Not a good match.")
    elif 40 <= love_score <= 60:
        print("You have a decent chance.")
    else:
        print("You are a great match!")

if __name__ == "__main__":
    love_calculator()
