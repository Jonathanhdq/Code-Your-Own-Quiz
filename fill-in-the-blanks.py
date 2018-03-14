easy_level = '''A string is a ___1___ of characters. Strings are basically just a bunch of words. You can specify
strings using single or double ___2___. Triple ___2___ are used to speify multi-line strings. Strings are
___3___, once you created a string, you cannot change it. However, you can "update" an existing string by
___4___ a variable to another string'''

medium_level = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___ by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

hard_level = '''The main goal of ___1___ research is to identify cause-and-effect relationships among variables.
___2___ and ___3___ research normally precedes cause-and-effect relationship studies. In ___1___ studies,
researchers typically have an expectation about the ___4___ to be explained, such as a ___5___ about the influence of price, advertising
and the like on sales. A typical causal study has management change one ___6___ (for example, advertising)
and then observe the effect on another ___6___ (such as sales).'''

easy_answers = ["sequence", "quotes", "immutable", "reassigning"] # Answers, in order, for the easy level quiz
medium_answers = ["function", "arguments", "none", "list"] # Answers, in order, for the medium level quiz
hard_answers = ["causal", "exploratory", "descriptive", "relationship", "prediction", "variable"] # Answers, in order, for the hard level quiz
blanks_to_fill_1 = ["___1___", "___2___", "___3___", "___4___"] # Blanks-to-fill for both the easy and medium level quiz
blanks_to_fill_2 = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"] # Blanks-to-fill for the hard level quiz
number_of_chances = ["1", "2", "3", "4", "5"] # The minimum and maximum number of chances a user is allowed to select per problem
quiz_difficulty_levels = ["easy", "medium", "hard"] # To ensure the user picks and appropriate quiz level
select_quiz_difficulty = "Please type in a difficulty level: Easy, Medium or Hard "
wrong_difficulty = "Please key in an appropriate quiz level: Easy, Medium or Hard "

def difficulty(level, user_input):
    '''Allows users to select and solve an appropriate quiz level
    Input(s): Quiz difficulty levels and the quiz users asks for, limited to easy, medium and hard
    Output(s): The selected quiz difficulty level'''
    while user_input not in level:
            user_input = raw_input(wrong_difficulty)
    if user_input == "easy":
        return easy_level
    elif user_input == "medium":
        return medium_level
    else:
        return hard_level

def answer_bank(quiz_level):
    '''Selects answer bank for use
    Input(s): Quiz level selected by user
    Output(s): The answers for the selected quiz level'''
    if quiz_level == easy_level:
        return easy_answers
    elif quiz_level == medium_level:
        return medium_answers
    else:
        return hard_answers

def blanks(quiz_level):
    '''Selects a blanks-to-fill bank based on the quiz difficulty level selected
    Input(s): Quiz level selected by user
    Output(s): The blanks to fill list to be used for matching purposes later on'''
    if quiz_level == easy_level or quiz_level == medium_level:
        return blanks_to_fill_1
    else:
        return blanks_to_fill_2

def greeting(quiz_level):
    '''Changes the greeting according to the quiz selected
    Input(s): Quiz level selected by user
    Output(s): The greeting displayed to users'''
    if quiz_level == easy_level:
        print "You have selected the easy quiz!"
    if quiz_level == medium_level:
        print "You have selected the medium quiz!"
    if quiz_level == hard_level:
        print "You have selected the hard quiz!"

def right_answer(right_answer, user_input_answer):
    '''Determines if the user answer is correct by matching it against the answer bank
    of the respective quizzes
    Input(s): The user answers and matches it against the actualquiz answers by calling the answer_bank function
    Output(s): Whether the answer is correct or not'''
    if user_input_answer == right_answer:
        return "Correct"
    else:
        return None

def play_again():
    '''Allows users to play again
    Input(s): None
    Output(s): Option for users to play again'''
    user_replay = raw_input("Would you like to play again? Yes or No: ").lower()
    while True:
        if user_replay == "yes":
            play_game()
            break
        elif user_replay == "no":
            print "Thank you for playing!"
            break
        else:
            user_replay = raw_input("Please only key in yes or no: ")

def chances():
    '''Allows the user to select. from 1 to 5. an appropriate number of chances
    Input(s): None
    Output(s): The number of chances per problem; Users select on their own'''
    user_chances = raw_input("From 1-5 please type in the number of chances you woud like to have per problem: ")
    while user_chances not in number_of_chances:
        user_chances = raw_input("Please only type in a number from 1 to 5: ")
    print "You will have " + user_chances + " chance(s) per problem!"
    return int(user_chances)

def answers_and_replace(level_selected, quiz_answer_bank, blanks_to_fill, user_input_chances):
    '''Essential function that checks user answers againsts the appropriate quiz answer bank as well as blanks to fill,
    also determines if the game has been won or lost
    Input(s): 1) Quiz selected by user, 2) Quiz answer bank, 3) Quiz blanks to fill, 4) Number of chances as specified by user
    Output(s): Replacement of blanks if user keys in the right answer; Minusing of chances if a wrong answer
    is keyed; Determining of user has won or lost the game, with option of replay'''
    blanks_index = 0
    answer_index = 0
    index = user_input_chances
    index_reuse = 0
    to_be_replaced = level_selected
    while blanks_index < len(blanks_to_fill):
        print ""
        user_answer = raw_input("What is the answer for " + blanks_to_fill[blanks_index] + " ? ").lower()
        if right_answer(quiz_answer_bank[answer_index], user_answer) == "Correct":
            index += index_reuse
            to_be_replaced = to_be_replaced.replace(blanks_to_fill[blanks_index], user_answer)
            print "That is correct! Good job!" + "\n"
            print "The quiz is now as follows: " + "\n"
            print "You have " + str(index) + " chances(s) left" + "\n"
            print to_be_replaced
            blanks_index += 1
            answer_index += 1
            index_reuse = 0
        else:
            index -= 1
            if 0 < index:
                print "That is incorrect! You have " + str(index) + " chance(s) left!" + "\n"
                print "The quiz is now as follows: " + "\n"
                print to_be_replaced
                index_reuse += 1
            else:
                if index == 0:
                    print "You have run out of chances!"
                    replay = play_again()
                    break
    if blanks_index == len(blanks_to_fill):
                print "Congratulations! You Win!"
                replay = play_again()

def play_game():
    '''Runs the quiz, asks users for the number of chances they want and
    prompts users to fill in their answers
    Input(s): None
    Output(s): Starting the quiz'''
    print "Welcome to my quiz!"
    user_input_difficulty = raw_input(select_quiz_difficulty).lower()
    level_selected = difficulty(quiz_difficulty_levels, user_input_difficulty)
    greeting_displayed = greeting(level_selected)
    quiz_answer_bank = answer_bank(level_selected)
    blanks_to_fill = blanks(level_selected)
    user_input_chances = chances()
    print "The quiz is now as follows: " + "\n"
    print level_selected + "\n"
    question_and_answer = answers_and_replace(level_selected, quiz_answer_bank, blanks_to_fill, user_input_chances)

play_game()
