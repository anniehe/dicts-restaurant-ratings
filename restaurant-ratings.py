import random

restaurant_ratings = {}

# Check to see if this goes in a better place
restaurant_names = None 

def sort_restaurant_ratings(filename):
    """Takes in restaurant ratings file and returns alphabetized list."""

    file_name = open(filename)
    for line in file_name:
        line = line.rstrip()
        words = line.split(":")

        restaurant, rating = words

        restaurant_ratings[restaurant] = rating

    get_user_rating()    

    restaurant_names = restaurant_ratings.keys()
    sorted_restaurant_names = sorted(restaurant_names)

    update_restaurant_ratings()

    for restaurant in sorted_restaurant_names:
        print restaurant + " is rated at " + str(restaurant_ratings[restaurant]) + "."


def get_user_rating():
    """Prompts user for new restaurant and rating, and adds this to restaurant_ratings dictionary."""

    new_restaurant = raw_input("Type the name of your favorite restaurant:\n>> ")
    
    while True:
        try:
            new_score = int(raw_input("Give this restaurant a rating from 1 (lowest) to 5 (highest):\n>> "))
            break
        except ValueError:
            print "\n Oops! That wasn't a number. Please try again!"

    restaurant_ratings[new_restaurant] = new_score


def update_restaurant_ratings():
    """Prompts user to update ratings for a random restaurant.

    Takes in a list from which to choose x number of random restaurants to update."""

    random_restaurant = random.choice(restaurant_names)
    print random_restaurant
    # user_name = raw_input("Hello, there! What's your name?\n>> ")
    # user_rating = int(raw_input("Please update this restaurant's rating from 1 (lowest) to 5 (highest):\n>> "))


sort_restaurant_ratings("scores.txt")



# Choose a random restaurant from the list in the file
# import random to select random key from dict

# Tell the user the chosen restaurant and its rating
# print key and rating for randomly generated KV pair

# Ask the user what the new rating should be
# raw input, ask for new rating for random restaurant

# Update the rating
# Overwrite rating for random rest.

# Choose another restaurant, repeat steps 2-4
# All of this should be a while loop while not 'q'

# Continue until the user types q.

