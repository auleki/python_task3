from random import randint

guess = input(f"What is your guess? \n> ")

def guessNumber(user_guess):
    attempts = 4
    start = True
    val = int(user_guess)
    random = randint(0, 10)
    if (val == random):   
        print("Congratulations, you won!")
    else:      
        while start:  
            val = int(input(f"Guess again? {attempts} attempt(s) left \n> "))          
            if (val != random):
                attempts -= 1            
            else: 
              print("Congratulations, you won!") 
              break
            if(attempts == 0):
                print("Sorry you lost the game, try again")
                break
            
  
def guessNow(range, tries, max_tries, start, random):
    print(random)
    while start:            
            print(random)
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
            random_range = '1 - 10'
            print('This is the EASY level')
            print(f"You get to guess a number between {random_range}, for {max_tries} tries")
            guessNow(random, tries, max_tries, start, random)
            
        elif(choice == 2):
            start = True
            tries = 1
            max_tries = 4
            random = randint(1, 20)
            random_range = '1 - 20'
            print('This is the MEDIUM level')
            print(f"You get to guess a number between {random_range}, for {max_tries} tries")
            guessNow(random, tries, max_tries, start, random)
                
            
        elif(choice == 3):
            start = True
            tries = 1
            max_tries = 4
            random = randint(1, 50)
            random_range = '1 - 50'
            print('This is the HARD level')
            print(f"You get to guess a number between {random_range}, for {max_tries} tries")
            guessNow(random, tries, max_tries, start, random)
            
            
        elif(ValueError):
            print("Please pick a number")
        else:
            print("No such option exists")
    except ValueError:
        print("Your choice needs to be a number")



