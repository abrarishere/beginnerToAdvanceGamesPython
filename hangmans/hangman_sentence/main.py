# Hangman game to guess the sentences 
import random
import string


def main():
    print("Welcome to Hangman game!")
    play_game = True
    while play_game:
        play_hangman()
        play_game = input("Do you want to play again? (yes/no): ").lower() == "yes"

def play_hangman():
    list_of_sentences = ["python is a programming language", "hangman is a word guessing game", "programming is fun"]
    sentence = random.choice(list_of_sentences).lower()
    print("Sentence to guess: " + sentence)
    sentence = sentence.replace(" ", "")
    guessed_letters = set()
    print("Guess the sentence:")
    print(display_sentence(sentence, guessed_letters))
    attempts = 0
    while attempts < 2:
        letter = input("Guess a letter: ").lower()
        if letter in guessed_letters:
            print("You have already guessed this letter")
            continue
        if letter in sentence:
            guessed_letters.add(letter)

            print(display_sentence(sentence, guessed_letters))



            if not '_' in display_sentence(sentence, guessed_letters):
                print("Congratulations! You have guessed the sentence.")
                break


        else:
            attempts += 1
            print("Wrong guess. You have " + str(6 - attempts) + " attempts left.")


def display_sentence(sentence, guessed_letters):
    result = ""
    for letter in sentence:
        if letter in guessed_letters:
            result += letter + " "
        elif letter == " ":
            result += "  "
        else:
            result += "_ "
    return result

if __name__ == "__main__":
    main()
