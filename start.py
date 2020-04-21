from random import randint

guess = input(f">What is your guess? \n")

def guessNumber(user_guess):
    val = int(user_guess)
    random = randint(0, 10)
    if (val != random):
        print("Not correct")
    else:
        print("Correct")
  
def guessNow(range, tries, max_tries, start, random):
    while start:            
            try:                         
                guess_input = int(input("Your guess \n> "))
                print(f"{tries} out {max_tries} attempts")
                if(guess_input == random):
                    print("Congratulations, you won!")
                    break
                if(tries == max_tries):
                    print("Sorry you lost, you can always try again by restarting the program.")
                    start = False
                    break                
                tries += 1
            except ValueError:
                print("Only numbers are allowed")     


try:
    guessNumber(guess)
    


except ValueError:
    try:
        print("There are 3 levels EASY, MEDIUM, HARD") 
        choice = int(input(">Pick 1 for EASY, 2 for MEDIUM, 3 for HARD \n"))
        #use a switch to select based on input
        
        if(choice == 1):
            start = True
            tries = 1
            max_tries = 6
            random = randint(1, 10)
            range = '1 - 10'
            print(f"You get to guess a number between {range}, for {max_tries} tries")
            guessNow(random, tries, max_tries, start, random)
            
        elif(choice == 2):
            print('This is the MEDIUM level')
            print("You get to guess a number between 1 - 20, for 4 tries")
            start = True
            tries = 1
            max_tries = 4
            random = randint(1, 20)
            range = '1 - 20'
            guessNow(random, tries, max_tries, start, random)    
            
        elif(choice == 3):
            print("Hard")
            print('You get to guess a number between 1 - 50, for 3 tries')
            start = True
            tries = 1
            max_tries = 4
            random = randint(1, 50)
            range = '1 - 50'
            guessNow(random, tries, max_tries, start, random)
            
        elif(ValueError):
            print("Please pick a number")
        else:
            print("No such option exists")
    except ValueError:
        print("Your choice needs to be a number")



