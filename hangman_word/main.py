import random


def main():
    attempts = 0
    text = load_text()
    listChar = [i for i in text]
    hidden = ["_" for _ in range(len(listChar))]

    while attempts < 11:
        if "_" not in hidden:
            print(f"You win! The word was: {text}")
            break
        print(hidden, end=f" attempts: {attempts}")
        user_t = input("\nEnter any character: ")

        if user_t in listChar:
            if user_t in hidden:
                print("You already guessed that character")
            else:
                for ind, char in enumerate(listChar):
                    if char == user_t:
                        hidden[ind] = user_t
        else:
            print("Wrong guess")
            attempts += 1

    if "_" in hidden:
        print(f"You lose! The word was: {text}")


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


if __name__ == "__main__":
    print("Welcome to the word guessing game!")
    main()
