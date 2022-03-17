
import random

deck = {
    "Katie": {
        "is_white" : True,
        "girlblue_eyes" : True,
        "ponytail" : True
    },
    "David": {
        "is_male" : True,
        "is_white" : True,
        "has_mustache" : True,
        "has_hat" : True
    },
    "Al": {
        "is_male" : True,
        "has_beard" : True,
        "has_glasses" : True
    },
    "Joe": {
        "is_male" : True,
        "has_glasses" : True
    },
    "Mike": {
        "is_male" : True,
        "is_white" : True,
        "has_hat" : True
    },
    "Ben": {
        "is_male" : True,
        "is_white" : True,
        "has_glasses" : True
    },
    "Sam" : {
        "is_male" : True,
        "has_beard" : True,
        "has_hat" : True
    },
    "Jordan" : {
        "is_male" : True,
        "has_beard" : True
    },
    "Leo" : {
        "is_male" : True,
        "white_hair" : True
    },
    "Gabe" : {
        "is_male" : True
    },
    "Daniel" : {
        "is_white" : True,
        "is_male" : True,
        "has_beard" : True,
        "has_mustache" : True
    },
    "Nick" : {
        "is_white" : True,
        "is_male" : True,
        "has_earrings" : True
    },
    "Eric" : {
        "is_male" : True,
        "is_white" : True
    },
    "Laura" : {
        "long_hair" : True,
        "has_earrings" : True,
        "girlgreen_eyes" : True
    },
    "Carmen" : {
        "white_hair" : True,
        "has_earrings" : True

    },
    "Sofia" : {
        "girlgreen_eyes" : True,
        "has_earrings" : True
    }, 
    "Farah" : {
        "long_hair" : True,
        "girlblue_eyes" : True,
        "ponytail" : True
    },
    "Olivia" : {
        "ponytail" : True
    },
    "Lily" : {
        "girlgreen_eyes" : True,
        "long_hair" : True
    },
    "Mia" : {
        "long_hair" : True
    },
    "Liz" : {
        "is_white" : True,
        "white_hair" : True,
        "long_hair" : True,
        "girlblue_eyes" : True,
        "has_glasses" : True
    },
    "Amy" : {
        "is_white" : True,
        "has_glasses" : True
    },
    "Rachel" : {
        "long_hair" : True,
        "is_white" : True,
        "has_glasses" : True
    },
    "Emma" : {
        "is_white" : True,
        "long_hair" : True
    }
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
    is_male = deck[name_to_guess].get("is_male", False)
    # print("is_male is ", is_male)
    is_white = deck[name_to_guess].get("is_white", False)
    # print("is_white is ", is_white)
    has_beard = deck[name_to_guess].get("has_beard", False)
    # print("has_beard is", has_beard)
    has_mustache = deck[name_to_guess].get("has_mustache", False)
    # print("has_mustache is", has_mustache)
    has_glasses = deck[name_to_guess].get("has_glasses", False)
    # print("has_glasses is", has_glasses)
    has_hat = deck[name_to_guess].get("has_hat", False)
    # print("has_hat is", has_hat)
    white_hair = deck[name_to_guess].get("white_hair", False)
    has_earrings = deck[name_to_guess].get("has_earrings", False)
    long_hair = deck[name_to_guess].get("long_hair", False)
    girlgreen_eyes = deck[name_to_guess].get("girlgreen_eyes")
    girlblue_eyes = deck[name_to_guess].get("girlblue_eyes", False)
    ponytail = deck[name_to_guess].get("ponytail", False)

    noq = 0
    # Descision Tree
    if is_male == True:
        noq = noq + 1
        if is_white == True:
            noq = noq + 1
            if has_hat == True:
                noq = noq + 1
                if has_mustache == True:
                    noq = noq + 1
                    guess = 'David'
                else:
                    noq = noq + 1
                    guess = 'Mike'
            else:
                noq = noq + 1
                if has_glasses == True:
                    noq = noq + 1
                    guess = 'Ben'
                else:
                    noq = noq + 1
                    if has_beard == True:
                        noq = noq + 1
                        guess = 'Daniel'
                    else:
                        noq = noq + 1
                        if has_earrings == True:
                            noq = noq + 1
                            guess = 'Nick'
                        else:
                            noq = noq + 1
                            guess = 'Eric'
        else:
            noq = noq + 1
            if has_glasses == True:
                noq = noq + 1
                if has_beard == True:
                    noq = noq + 1
                    guess = 'Al'
                else:
                    noq = noq + 1
                    guess = 'Joe'
            else:
                noq = noq + 1
                if has_beard == True:
                    noq = noq + 1
                    if has_hat == True:
                        noq = noq + 1
                        guess = 'Sam'
                    else:
                        noq = noq + 1
                        guess = 'Jordan'
                else:
                    noq = noq + 1
                    if white_hair == True:
                        noq = noq + 1
                        guess = 'Leo'
                    else:
                        noq = noq + 1
                        guess = 'Gabe'
    else:
        noq = noq + 1
        if is_white == True:
            noq = noq + 1
            if has_glasses == True:
                noq = noq + 1
                if white_hair == True:
                    noq = noq + 1
                    guess = 'Liz'
                else:
                    noq = noq + 1
                    if long_hair == True:
                        noq = noq + 1
                        guess = 'Rachel'
                    else:
                        noq = noq + 1
                        guess = 'Amy'
            else:
                noq = noq + 1
                if ponytail == True:
                    noq = noq + 1
                    guess = 'Katie'
                else:
                    noq = noq + 1
                    guess = 'Emma'
        else:
            noq = noq + 1
            if has_earrings == True:
                noq = noq + 1
                if girlgreen_eyes == True:
                    noq = noq + 1
                    if long_hair == True:
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
                if ponytail == True:
                    noq = noq + 1
                    if girlblue_eyes == True:
                        noq = noq + 1
                        guess = 'Farah'
                    else:
                        noq = noq + 1
                        guess = 'Olivia'
                else:
                    noq = noq + 1
                    if girlgreen_eyes == True:
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


wins_florian = 0
wins_oceanne = 0
ties = 0

for x in range(1000):
    win_florian, win_oceanne, no_win = run_game()
    wins_florian += win_florian
    wins_oceanne += win_oceanne
    ties += no_win

print(f"Florian won {wins_florian} games")
print(f"oceanne won {wins_oceanne} games")
print(f"Number of ties {ties} games")