import random
import time

def choose_word(difficulty):
    easy_words = ["python", "hangman", "code", "developer", "computer"]
    medium_words = ["programming", "challenge", "software", "debugging", "learning"]
    hard_words = ["machinelearning", "encryption", "javascript", "webdevelopment", "algorithm"]

    if difficulty == "easy":
        return random.choice(easy_words).lower()
    elif difficulty == "medium":
        return random.choice(medium_words).lower()
    elif difficulty == "hard":
        return random.choice(hard_words).lower()
    else:
        return random.choice(easy_words + medium_words + hard_words).lower()

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def display_score(score, total_attempts, total_time):
    print("\nCurrent Score:", score)
    print("Words Guessed Correctly / Total Attempts:", score, "/", total_attempts)
    print("Total Time Elapsed: {:.2f} seconds".format(total_time))

def hangman():
    print("Welcome to Hangman!")

    score = 0
    total_attempts = 0
    total_time = 0
    max_hints = 2  # maximum number of hints per game

    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Setting to easy.")
            difficulty = "easy"

        word = choose_word(difficulty)
        original_word_set = set(word)
        guessed_letters = set()
        attempts = 6  # default number of attempts
        hints_used = 0
        start_time = time.time()

        print("Here's a hint: The word has", len(word), "letters.")

        while attempts > 0:
            print("\nAttempts left:", attempts)
            print(display_word(word, guessed_letters))
            display_score(score, total_attempts, time.time() - start_time)
            print("Hints left:", max_hints - hints_used)

            action = input("Guess a letter (type 'hint' for a hint, 'quit' to quit): ").lower()

            if action == "quit":
                print("Quitting the game. Your final score:", score)
                return
            elif action == "hint":
                if hints_used < max_hints:
                    hint = random.choice(list(original_word_set - guessed_letters))
                    guessed_letters.add(hint)
                    hints_used += 1
                    print("Hint:", hint)
                else:
                    print("You've used all available hints.")
                continue

            if len(action) != 1 or not action.isalpha():
                print("Please enter a single letter.")
                continue

            if action in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(action)

            if action not in word:
                attempts -= 1
                print("Incorrect guess!")

            if set(word) <= guessed_letters:
                score += len(word)  # score is based on the length of the word
                total_attempts += 1
                total_time += time.time() - start_time
                print("Congratulations! You guessed the word:", word)
                break

        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was:", word)
            total_attempts += 1
            total_time += time.time() - start_time
            display_score(score, total_attempts, total_time)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Your final score:", score)
            break

if __name__ == "__main__":
    hangman()
