def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt<3:
        if guess.lower() == answer.lower():
            print("correct Answer")
            score = score+1
            still_guessing = False 
        else:
            if attempt<2:
                guess = input("sorry wrong answer,try again")
            attempt = attempt+1
    if attempt == 3:
        print("The correct answer is:",answer)
score = 0
guess1 = input("What is the furthest planet from the Sun?")

check_guess(guess1,"Neptune")

guess2 = input("What animal has the highest blood pressure?")

check_guess(guess2,"Giraffe")

guess3 = input("What's the smallest country in the world?")

check_guess(guess3,"Vatican")

guess4 = input("Name Disney's First film?")

check_guess(guess4,"Snow White")

guess5 = input("Which is the largest animal?")

check_guess(guess5,"Blue Whale")

print("Your Score is "+str(score))