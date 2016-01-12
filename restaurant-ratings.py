def sort_restaurant_ratings(filename):
    """Takes in restaurant ratings file and returns alphabetized list."""

    restaurant_ratings = {}

    file_name = open(filename)
    for line in file_name:
        line = line.rstrip()
        words = line.split(":")

        restaurant, rating = words

        restaurant_ratings[restaurant] = rating

    restaurant_names = restaurant_ratings.keys()
    sorted_restaurant_names = sorted(restaurant_names)

    for restaurant in sorted_restaurant_names:
        print restaurant + " is rated at " + restaurant_ratings[restaurant] + "."


sort_restaurant_ratings("scores.txt")
