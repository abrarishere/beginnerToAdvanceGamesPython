import random


def main():
    attempts = 0
    print('You have to guess the word in less than 10 attempts') 
    print('\n')
    while True:
        word_to_guess = load_text()
        print('The word has {} letters'.format(len(word_to_guess)))
        print('\n')
        guessed_word = ['_'] * len(word_to_guess)
        print(' '.join(guessed_word))
        print('\n')
        while attempts < 10:
            letter = input('Enter a letter: ').strip()
            if letter in word_to_guess:
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == letter:
                        guessed_word[i] = letter
                print(' '.join(guessed_word))
                print('\n')
                if '_' not in guessed_word:
                    print('Congratulations! You have guessed the word!')
                    break
            else:
                attempts += 1
                print('Wrong letter! You have {} attempts left'.format(10 - attempts))
                print('\n')
        if input('Do you want to play again? (Y/N)') != 'Y':
            break





def load_text():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()



if __name__ == '__main__':
    print("Welcome to the word guessing game!")
    if input("Do you want to play? (Y/N)").strip().upper() != 'N':
        main()
