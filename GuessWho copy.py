
import random

deck = {
    "Al": ["is_male", "has_beard", "has_glasses", "has_green_eyes"],
    "Amy":["is_white", "has_glasses", "has_brown_eyes"],
    "Ben": ["is_male", "is_white", "has_glasses", "has_brown_eyes"],
    "Carmen": ["has_white_hair", "has_earrings", "has_brown_eyes"],
    "Daniel": ["is_white", "is_male", "has_beard", "has_blue_eyes", "has_mustache"],
    "David": ["is_male", "is_white", "has_mustache", "has_hat", "has_brown_eyes"],
    "Emma": ["is_white", "has_long_hair", "has_brown_eyes"],
    "Eric": ["is_male", "is_white", "has_blue_eyes"],
    "Joe": ["is_male", "has_glasses", "has_brown_eyes"],
    "Jordan": ["is_male", "has_beard"],
    "Farah": ["has_long_hair", "has_blue_eyes", "has_ponytail"],
    "Gabe": ["is_male", "has_brown_eyes"],
    "Katie": ["is_white", "has_blue_eyes", "has_ponytail"],
    "Laura": ["has_long_hair", "has_earrings", "has_green_eyes"],
    "Leo": ["is_male", "has_white_hair", "has_brown_eyes"],
    "Lily": ["has_green_eyes", "has_long_hair"],
    "Liz": ["is_white", "has_white_hair", "has_long_hair", "has_blue_eyes", "has_glasses"],
    "Mia": ["has_long_hair", "has_brown_eyes"],
    "Mike": ["is_male", "is_white", "has_hat", "has_brown_eyes"],
    "Nick": ["is_white", "is_male", "has_earrings", "has_brown_eyes"],
    "Olivia": ["has_ponytail" ,"has_brown_eyes"],
    "Rachel": ["has_long_hair", "is_white", "has_glasses", "has_blue_eyes"],
    "Sam" : ["is_male", "has_beard", "has_hat", "has_green_eyes"],
    "Sofia": ["has_green_eyes", "has_earrings"],
}



def run_game():

    win_florian = 0
    win_oceanne = 0
    no_win = 0

    c = pick_character()
    neq_florian = guess_by_florian(c)
    neq_oceanne = 5

    if neq_florian == neq_oceanne:
        print("It is a tie!")
        no_win += 1

    if neq_florian < neq_oceanne:
        print("Florian wins!")
        win_florian += 1

    if neq_florian > neq_oceanne:
        print("Oceanne wins!")
        win_oceanne += 1

    return(win_florian, win_oceanne, no_win)

def pick_character():
    # CHARACTER TO GUESS
    names = deck.keys()
    name = random.choice(list(names))
    return(name)

def guess_by_florian(name_to_guess):
    # print("Character to guess:", namee_to_guess)
    # ATTRIBUTES OF THAT CHARACTER
    is_male = "is_male" in deck[name_to_guess]
    # print("is_male is ", is_male)
    is_white = "is_white" in deck[name_to_guess]
    # print("is_white is ", is_white)
    has_beard = "has_beard" in deck[name_to_guess]
    # print("has_beard is", has_beard)
    has_mustache = "has_mustache" in deck[name_to_guess]
    # print("has_mustache is", has_mustache)
    has_glasses = "has_glasses" in deck[name_to_guess]
    # print("has_glasses is", has_glasses)
    has_hat = "has_hat" in deck[name_to_guess]
    # print("has_hat is", has_hat)
    has_white_hair = "has_white_hair" in deck[name_to_guess]
    has_earrings = "has_earrings" in deck[name_to_guess]
    has_long_hair = "has_long_hair" in deck[name_to_guess]
    has_green_eyes = "has_green_eyes" in deck[name_to_guess]
    has_blue_eyes = "has_blue_eyes" in deck[name_to_guess]
    has_ponytail = "has_ponytail" in deck[name_to_guess]
    noq = 0

    # Descision Tree
    if is_male:
        noq = noq + 1
        if is_white:
            noq = noq + 1
            if has_hat:
                noq = noq + 1
                if has_mustache:
                    noq = noq + 1
                    guess = 'David'
                else:
                    noq = noq + 1
                    guess = 'Mike'
            else:
                noq = noq + 1
                if has_glasses:
                    noq = noq + 1
                    guess = 'Ben'
                else:
                    noq = noq + 1
                    if has_beard:
                        noq = noq + 1
                        guess = 'Daniel'
                    else:
                        noq = noq + 1
                        if has_earrings:
                            noq = noq + 1
                            guess = 'Nick'
                        else:
                            noq = noq + 1
                            guess = 'Eric'
        else:
            noq = noq + 1
            if has_glasses:
                noq = noq + 1
                if has_beard:
                    noq = noq + 1
                    guess = 'Al'
                else:
                    noq = noq + 1
                    guess = 'Joe'
            else:
                noq = noq + 1
                if has_beard:
                    noq = noq + 1
                    if has_hat:
                        noq = noq + 1
                        guess = 'Sam'
                    else:
                        noq = noq + 1
                        guess = 'Jordan'
                else:
                    noq = noq + 1
                    if has_white_hair:
                        noq = noq + 1
                        guess = 'Leo'
                    else:
                        noq = noq + 1
                        guess = 'Gabe'
    else:
        noq = noq + 1
        if is_white:
            noq = noq + 1
            if has_glasses:
                noq = noq + 1
                if has_white_hair:
                    noq = noq + 1
                    guess = 'Liz'
                else:
                    noq = noq + 1
                    if has_long_hair:
                        noq = noq + 1
                        guess = 'Rachel'
                    else:
                        noq = noq + 1
                        guess = 'Amy'
            else:
                noq = noq + 1
                if has_ponytail:
                    noq = noq + 1
                    guess = 'Katie'
                else:
                    noq = noq + 1
                    guess = 'Emma'
        else:
            noq = noq + 1
            if has_earrings:
                noq = noq + 1
                if has_green_eyes:
                    noq = noq + 1
                    if has_long_hair:
                        noq = noq + 1
                        guess = 'Laura'
                    else:
                        noq = noq + 1
                        guess = 'Sofia'
                else:
                    noq = noq + 1
                    guess = 'Carmen'
            else:
                noq = noq + 1
                if has_ponytail:
                    noq = noq + 1
                    if has_blue_eyes:
                        noq = noq + 1
                        guess = 'Farah'
                    else:
                        noq = noq + 1
                        guess = 'Olivia'
                else:
                    noq = noq + 1
                    if has_green_eyes:
                        noq = noq + 1
                        guess = 'Lily'
                    else:
                        noq = noq + 1
                        guess = 'Mia'

    if name_to_guess == guess:
        print("You found the right character! It was", guess, name_to_guess)
    else:
        print("You've guessed the wrong character. The character was", name_to_guess, ". We guessed", guess, ".")
    
    print(noq)

    return(noq)


def guess_by_oceanne(name_to_guess):
    return


def main():
    wins_florian = 0
    wins_oceanne = 0
    ties = 0

    for x in range(100):
        win_florian, win_oceanne, no_win = run_game()
        wins_florian += win_florian
        wins_oceanne += win_oceanne
        ties += no_win

    print(f"Florian won {wins_florian} games")
    print(f"oceanne won {wins_oceanne} games")
    print(f"Number of ties {ties} games") 


main()