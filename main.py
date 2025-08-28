import random as r
import time as t


class Hangman:

    def __init__(self):
        self.trials = 0
    def generate_secret_word(self):
        secret_words = ['apple','cherry','functionality','testing']
        rand_index = r.randint(0, len(secret_words)-1)
        return secret_words[rand_index]
    def hanged(self, trial_index):
        HANGMANPICS = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']
        return HANGMANPICS[trial_index];
    def check_win(self):
        print("You win")
    def draw_board(self,data):
        board = ""
        for i in range(0, len(data)):
            board += "*"
        return board

    def replace_board(self,data,at,new_ch):
        new_board=""
        for i in range(0,len(data)):
            if i == at:
                if data[i] == "*":
                    new_board += new_ch
            else:
                new_board+=data[i]
        return new_board
    def start_game(self):

        print("***Welcome to Hangman Game...****")
        print("---------------------------------")
        print("  Prepare to play to the death")
        print("---------------------------------")
        print()
        MAX_TRIALS = 7
        greetings = 0
        game_result = False
        print("You are given a maximum of ",MAX_TRIALS," trials, Try not to misuse.!!!")
        print()
        print("You are required to find the secret word, Don't try to lose....")
        choice = input("Type 'begin' to start game or 'rule' to note game rules...")
        print()

        if choice == 'begin':
            print("Generating secret word....")
            t.sleep(1)

            print("Find the word, you can start now..")
            secret_word = self.generate_secret_word()
            board = self.draw_board(secret_word)
            print(board+" [Fill Up The Field] - Unknown Characters...")

            while self.trials < MAX_TRIALS:
                data = input("Enter Your Character: ")
                if len(data) == 1:
                    #code functionality
                    for i in range(0,len(secret_word)):
                        if secret_word[i] == data:
                            board = self.replace_board(board,i,data)
                    print(board)
                    if data not in secret_word:
                        self.trials+=1
                        #print("yoooo")
                        print(self.hanged(self.trials-1))
                    else:
                        #greets users while playing...
                        match greetings:
                            case 0:
                                print("Nice Try...")
                            case 2:
                                print("This is amazing you can do it!!!")
                            case 4:
                                print("Pray not to get hanged!!! hahahaha")
                            case 5:
                               if self.trials == MAX_TRIALS:
                                   print("Sorry, You Lost!!!!")
                            case _:
                                if game_result is True:
                                   print("You did it!!! Hahaha")
                        greetings+=1
                else:
                    print("Enter valid character length: Just pass in a single character")
                    print(board)
                    #checks if total inputs matches secret word
                if board == secret_word:
                    self.check_win()
                    break
            if board != secret_word:
                print("You Lose!!!")
        else:
            print("Below are the game rules:")
            print("1. You are given a maximum of 5 trials, find the guess number within those trials,\n the more you lose, the more your trials reduces")
            print("2. For repeated characters once you get just one out of the repeated characters the system auto fills the rest.")
            print("Let's play to the death.. Enjoy")
        return 0


hangman = Hangman()
hangman.start_game()