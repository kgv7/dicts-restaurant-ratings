"""Restaurant rating lister."""

open_file=open("scores.txt","r")
ratings_dict={}

def print_restaurant_ratings():

    for line in open_file:
        word=line.rstrip().split(":")
        ratings_dict[word[0]]=int(word[1])
    alphabetized_ratings=sorted(ratings_dict)

    for restaurant in alphabetized_ratings:
        rating=ratings_dict[restaurant]
        print(f'{restaurant} is rated at {rating}')


def input_func():

    rating_options = [1, 2, 3, 4, 5]
    
    restaurant_name=input("What's the restaurant that you want to rate?>>>")

    while True:
        try:
            restaurant_score=int(input("What's the rating?>>>"))
            if restaurant_score not in rating_options:
                print("The score needs to be between 1 and 5.")
                # restaurant_score=input("What's the rating?>>>")
            if restaurant_score in rating_options:
                break
        except ValueError:
            print("Only integers are accepted. The score needs to be between 1 and 5.")
            # restaurant_score=input("What's the rating?>>>")  

    # restaurant_score = int(restaurant_score)

    ratings_dict[restaurant_name]=restaurant_score
    # print_restaurant_ratings()
# input_func()

def user_choices():
    
    while True:
        option = input("""Do you want to see:
            A. Print restaurant ratings
            B. Add a new restaurant
            C. Quit?
            >>> """)
        option = option.upper()
        
        if option == "A":
            print_restaurant_ratings()
        if option == "B":
            input_func()
        if option == "C":
            print("Goodbye!")
            break
user_choices()