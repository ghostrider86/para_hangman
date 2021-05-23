import random
class Word:
    """
    This class is intended to generate a random word for the game to operate with.
    This class will also check the word and perform updates on the puzzle
    """
    def __init__(self):
        """
        Creating variables for this class to share. Mainly inporting the word base list and
        setting true or false values for a correct guess.
        """
        self.file = open('word_bank.txt', 'r')
        self.word_list = self.file.read()
        self.word_bank = self.word_list.splitlines()
        self.word_bank_len = len(self.word_bank) - 1

        # self.list = ["Python", "Java", "Programming"] #This was for initial testing. No longer needed

        self.puzzle_word = ""
        self.hidden_puzzle = []
        self.correct_guess = False
        self.get_puzzle()

    def get_puzzle(self):
        """
        Initialize the random word and generate the hidden puzzle text to be sent back to director.
        ***Should only be run once or else the word will change***
        """
        i = 0
        self.puzzle_word = self.word_bank[random.randint(0, self.word_bank_len)]
        while i != len(self.puzzle_word):
            self.hidden_puzzle.append("_") #CHECK THIS TO MAKE SURE IT APPENDS CORRECTLY *******************
            i += 1

        return self.hidden_puzzle
    
    def send_updated_puzzle(self):
        """
        Will send the current hidden puzzle to director.
        """
        return self.hidden_puzzle

    def guess(self, guess):
        """
        This will evaluate the user's guess and compare it to the puzzle word. If it's incorrect, return false.
        If correct, return True and update hidden puzzle.
        Arg:
        word(self)
        guess: This is the letter (char) which the user inputed to be compared to the puzzle.
        """
        self.correct_guess = False
        for letter in range(len(self.puzzle_word)):
            if self.puzzle_word[letter] == guess:
                self.hidden_puzzle[letter] = guess #CHECK THIS TO MAKE SURE THE CORRECT AREA IS REPLACED ******************
                self.correct_guess = True
        
        return self.correct_guess
    
    def check_finish(self):
        """
        This will check the hidden puzzle to see if there are any blank spaces left.
        If not, the game is completed and the return is True. Otherwise, the return is False.
        """
        # for character in range(len(self.hidden_puzzle)):
        #     if self.hidden_puzzle[character] != "_": #CHECK THIS TO MAKE SURE IT WORKS AS IT OUGHT TO FOR A VICTORY***************
        #         return False
        if "_" in self.hidden_puzzle:
            return False
        else:
            return True