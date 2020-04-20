#Christina Aragon
# Guessing Game with a Calculator

   
#16 Lines
##### THE STARTING TEXT ######
def main():
    print("Welcome to the Guessing Game of the century! All characters are case sensitive so watch out!")
    useranswer = input("Are you ready to play? Yes, No? If a Calculator is needed type Calculator.  Type Choice Here:")

####### VARIABLES ########

    YouLose = "You Lose! Better Luck Next Time!"

###### VARIABLES FOR SPORTS TRIVIA ######

    answerSport1 = "Kansas City Chiefs"
    answerSport2 = "4"

###### VARIABLES FOR TECH TRIVIA ######

    answerTech2 = "2025"
    answerTech1 = "Elon Musk"

##### IF GUEST CONTINUES WITH TRIVIA ######

    if useranswer == "Yes":
        start = print("Lets Begin! ")
    
        input("Topic Choices: Sports Trivia or Technology Fun Facts? Press Enter to continue ")
        topic1 = "Sports Trivia"
        topic2 = "Technology Fun Facts"
        topic3 = "National Park Trivia"
        topic = ""
        topic = input("Enter Topic Choice: ")
    
###### IF GUEST CHOOSES SPORTS TRIVIA ######
        # Ryan the TA guided me on using the else/if statements
    #FIRST QUESTION
        sportquestion1 = input("Who won the most recent Superbowl? Press Enter to beign. ")
        answerSport1 = "Kansas City Chiefs" or "The Chiefs" or "Chiefs"

        ##SET UP THE GUESSES
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != answerSport1 and not(out_of_guesses):
            if guess_count < guess_limit:
                guess = input("Enter guess: ")
                guess_count += 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            print(YouLose)
        else:
            print("Good Job!")
            
#### SECOND QUESTION (SPORTS) ######

            if guess == answerSport1:
                sportquestion2 = input("The Olympics are held every how many years? Press Enter to Beign. ")
                answerSport2 = "4" or "4 years" or "4 Years"

            #GUESS SET UP
                guess = ""
                guess_count = 0
                guess_limit = 3
                out_of_guesses = False

                while guess != answerSport2 and not(out_of_guesses):
                    if guess_count < guess_limit:
                        guess = input("Enter guess: ")
                        guess_count += 1
                    else:
                        out_of_guesses = True
    
                if out_of_guesses:
                    print(YouLose)
                else:
                    print("You Won! ")

###################### END OF SPORTS TRIVIA #######################
            if topic == "Sports Trivia":
                SportsTrivia()

###### BEGIN TECHNOLOGY TRIVIA ####
    #FIRST QUESTON

    elif topic == "Technology Fun Facts":
        techQuestion1 = input("Who owns Space X and Tesla? Press Enter to continue. ")
        answerTech1 = "Elon Musk"

        #GUESS SET UP
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
#   
        while guess != answerTech1 and not(out_of_guesses):
            if guess_count < guess_limit:
                guess = input("Enter guess: ")
                guess_count += 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            print(YouLose)
        else:
            print("Good Job!" + "You are doing amazing sweetie!")

##### SECOND QUESTION (TECH) ########

            if guess == answerTech1:
                techquestion2 = input("When are we suppose to go to the Mars? Press Enter to Beign. ")
                answerTech2 = "2025"

            #GUESS SET UP
                guess = ""
                guess_count = 0
                guess_limit = 3
                out_of_guesses2 = False

                while guess != answerTech2 and not(out_of_guesses):
                    if guess_count < guess_limit:
                        guess = input("Enter guess: ")
                        guess_count += 1
                    else:
                        out_of_guesses = True

                if out_of_guesses2:
                    print(YouLose)
                else:
                    print("You Won! " + "Have a great day!")

########################### END OF TECH TRIVIA ########################
                        
###### CALCULATOR ######
        # POGILS were useful in figuring out the code for this one

## Welcome Page ##

    elif useranswer == "Calculator":
        print("Welcome to the Calculator. ")
        function = input("What Function would you like to do? Add, Subtract, Multiply, Divide.")

    #Add
        if function == "Add":
            print("Now enter your two values.. ")
            
            num1=int(input("First Number: "))
            num2=int(input("Second number: "))
            
            sum= float(num1) + float(num2)
            print('The Total of {0} and {1} is {2}'.format(num1, num2, sum))

    ## End of Addition##

    #Subrtraction

        elif function == "Subtract":
            print("Now enter your two values.. ")
            
            num1=int(input("First Number: "))
            num2=int(input("Second number: "))
            
            sum= float(num1) - float(num2)
            print('The Value of {0} and {1} is {2}'.format(num1, num2, sum))

    ## End of Subtraction ##

    #Multiply
        elif function == "Multiply":
            print("Now enter your two values.. ")
            
            num1=int(input("First Number: "))
            num2=int(input("Second number: "))
            
            sum= float(num1) * float(num2)
            print('The Value of {0} and {1} is {2}'.format(num1, num2, sum))

    ## End of Multiplication ##

    #Division

        elif function == "Divide":
            print("Now enter your two values.. ")
            
            num1=int(input("First Number: "))
            num2=int(input("Second number: "))
            
            sum= float(num1) / float(num2)
            print('The value of {0} and {1} is {2}'.format(num1, num2, sum))
        else:
            print("It was nice knowing you! ")
    ## End of Division ##

############# END OF CALCULATOR ################

    else:
        print("Come Back Soon!")

####### CALL TO MAIN ######
main()

