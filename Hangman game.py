import random

lives = 9
words = ['pizza', 'japan', 'cheek', 'shall', 'flung', 'senator', 'capacity', 'although', 'nevertheless', 'expect', 'wriggled', 'whitelie', 'pitfall', 'branched', 'skyscrappers', 'loudest', 'counterpoint',
                 'hangup', 'tracks', 'driveway', 'flue', 'pyramids', 'tired', 'eternity', 'kindle', 'scramble', 'platinum', 'cleanser', 'violin', 'english', 'japanese', 'aircraft', 'spain', 'relaxed', 'cherries',
                 'complain', 'workout', 'gym', 'titan', 'abomination', 'basement' , 'databaase', 'accelerator', 'frighten', 'destructive', 'waste', 'catastrophe', 'poor', 'adjust', 'fabric', 'handrail', ]

secret_word = random.choice(words)

clue = list('?' * len(secret_word))

heart_symbol = u'\u2764'

guessed_word_correctly = False
guessed_letters = [ ]

def update_clue (guessed_letter, secret_word, clue):
    index = 0
    
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            
            
        index += 1    
            
while lives > 0:
        print(clue)
        print('Lives left: ' + heart_symbol * lives)
        guess = input('Guess a letter or the whole word: ')

        if guess == secret_word:
            guessed_word_correctly = True
            break
        
        if guess in guessed_letters:
               print('You already guessed that letter. Try another one!')
               continue
               guessed_letters.append(guess)

        if guess in secret_word:
            update_clue(guess, secret_word, clue)

            if '?' not in clue:
               guessed_word_correctly = True
               break

       
 
        else:
            print('Incorrect. You lost a life')
            lives = lives - 1

if guessed_word_correctly:
             print('You won! The secret word was ' +  secret_word)
             
else:
         print('You lost ! The secret word was ' + secret_word)
             
