restaurant_ratings = {}

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


sort_restaurant_ratings("scores.txt")