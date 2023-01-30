import random

num_digits = 3
max_guesses = 10

def main():
    print('''This is a guessing game : 
    I am thinking of a {}-digit number and you need to guess it within {} guesses
    Here are some rules to play the game :
    When i say          which means
        Cow             One digit is correct but in wrong position
        Bull            One digit is correct and is in the correct position
        None            No correct digits are present
        For example if the number is 172 and you guessed 245 then the clue will be Cow, 
        if you guess 145 then the clue will be Bull, and if you guess 456 then the clue will be None'''.format(num_digits,max_guesses))

    while True:
        Sec_num = getSecretNum()
        print("I have chosen a number, Let's see if you can guess it!")

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}'.format(num_guesses))
                guess = input('> ')

            clues = getClues(guess, Sec_num)
            print(clues)
            num_guesses += 1

            if guess == Sec_num:
                break
            if num_guesses > max_guesses:
                print("You ran out of guesses, Better luck next time!")
                print("The number is {}".format(Sec_num))

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thank you for playing!")

def getSecretNum():
    nums = list('0123456789')
    random.shuffle(nums)

    Sec_num = ''
    for i in range(num_digits):
        Sec_num += str(nums[i])
    
    if Sec_num[0] == '0':
        Sec_num = Sec_num[1:] + Sec_num[0]

    return Sec_num

def getClues(guess, Sec_num):
    if guess == Sec_num:
        return "Great! You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == Sec_num[i]:
            clues.append('Bull')
        elif guess[i] in Sec_num:
            clues.append('Cow')
    
    if len(clues) == 0:
        return 'None'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
