import random


def play_game(target=None, max_attempts=None):
    if target is None:
        target = random.randint(1, 100)

    valid_guesses = 0

    while True:
        if max_attempts is not None and valid_guesses >= max_attempts:
            print(f"  Game over! You ran out of attempts. The number was {target}.") 
            break

        user_input = input("guess a number between 1 and 100: ")
        try:
            guess = int(user_input)
        except ValueError:
            print("  invalid input. enter a whole number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("  invalid input. enter a whole number between 1 and 100.")
            continue

        valid_guesses += 1

        if guess > target:
            print("  too high")
        elif guess < target:
            print("  too low")
        else:
            print(f"  correct! you got it in {valid_guesses} guesses")
            break

    try:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ["yes", "y"]:
            play_game(max_attempts=max_attempts)
    except Exception:
        pass


# Do not modify below this line
if __name__ == "__main__":
    play_game()
