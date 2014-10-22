
def is_prime(x):
    #This function, given a postive number
    #iterates through the value to determine if it is prime
    count = 2
    if x == 1 or x <=0:
        return False
    elif x == 2:
        return True
        
    while count < x:
        if (x % count) == 0:
            return False
            break
        elif (count == x-1):
            return True
        else:
            count += 1
            
        
        
print is_prime(11)

def reverse(text):
    # This function takes a string and reverses
    # it completely
    # ex: 'abcd' becomes 'dcba'
    reversed_text = []
    for i in range(len(text)-1,-1,-1):
        reversed_text.append(text[i])
    return ''.join(reversed_text)
        
print reverse('abcd')


def anti_vowel(text):
    #This function removews all vowels from strings
    #code_academy "Practice makes perfect 8/15
    count = 0
    no_vowel = text
    
     for letter in no_vowel:
        if letter in "aeiouAEIOU":
            no_vowel = no_vowel.replace(letter,"")
    return no_vowel

text = "kill dill bililili TAB bab aeiouAEIOU"

print anti_vowel(text)


def purify(sequence):
    # Takes a list and pulls copies all the
    # even numbers to another list
    # new_list = new_list.append(sequence[i])
    # originally returned none, that is why it
    # is just: new_list.append(stuff)???
    new_list = []
    
    for i in range(0, len(sequence)):
        print 'index of seq ', sequence[i]
        if sequence[i] % 2 == 0:
            new_list.append(sequence[i])
    return new_list

print purify([6, 5, 4, 3, 2, 1])


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    # for a given string, the function looks up the
    # point value associated with the letters and
    #adss them all. 
    word = word.lower()
    points = 0
    
    for letter in word:
        if letter in score:
            points += score[letter]
    return points

print scrabble_score("Helix")

def censor(text,word):
    # A function that looks at the text of a sentence and
    # repalces any words that match the second arguement
    # with **** that is as long as teh word.
    if text in word:
        word = word.replace(text,len(text)*"*")
        print word

censor( 'hack', 'hack sack back hack dack lack' )

def count(sequence, item):
    # A function that determines the number
    # of "items" in a list "sequence"
    count = 0
    
    for i in sequence:
        print i
        if i == item:
            count += 1
            #print count
    return count

print count([1, 2, 1, 1, 3, 4, 5, 1, 1], 5)

def product(values):
    # Takes a list of values and computers their product
    
    product = 1
    
    for i in values:
        product = product * i
    return product

print product([ 4, 5, 5])


def remove_duplicates(values):
    # Takes a list of values and weeds out the 
    # duplicates returning a list with only
    # unique numbers
    removed = []

    for i in values:
        if removed.count(i) == 0:
            removed.append(i)
    return removed

print remove_duplicates([1,1, 1, 3, 5,2,2])


