# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
        
def change_alphabet(letter, alphabet):
    alphabet = alphabet.replace(letter, '')
    return alphabet

def change_displayed(letter, word, displayed_word):
    # Takes guessed letter, word, and changes displayed word    
    for i in range(0,len(word)):
            if word[i] == letter:
                displayed_word[i] = letter
    return displayed_word

def hangman():
    #The main body of the program, controls the text, while loop, and win lose conditions
    
    word = choose_word(wordlist)
    guesses = 10
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    displayed_word = ['_']*len(word)

    print displayed_word

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ', len(word), ' letters long'
    print 'The word is ', word
    
    while guesses > 0:
        print '------------'
        print 'You have ', guesses, ' guesses left'
        print 'Available letters: ', alphabet
        letter = raw_input('Please guess a letter: ')
        alphabet = change_alphabet(letter, alphabet)

        if letter in word:
            displayed_word = change_displayed(letter, word, displayed_word)    
            print 'Good guess: ', ''.join(displayed_word)
            if ''.join(displayed_word) == word:
                print '------------'
                print 'Congratulations, you won!'
                break
        else:
            print 'Oops! That letter is not in my word: ', ''.join(displayed_word)
            guesses -= 1
            
    if guesses == 0:
        print 'Sorry, you lost. Try again'
        

hangman()
