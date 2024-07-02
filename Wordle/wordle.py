from Dictionary import words
from helpers import filter_solutions


num_guesses = int(input("Enter the number of guesses: "))
possible_words = words
guesses = []
feedbacks = []

for i in range(num_guesses):
    guess = input(f"Enter guess {i+1}: ").strip().lower()
    feedback = input(f"Enter feedback for guess {i+1} (G for green, Y for yellow, B for black/grey): ").strip().upper()
    guesses.append(guess)
    feedbacks.append(feedback)

possible_solutions = filter_solutions(possible_words, guesses, feedbacks)
print("Possible solutions are:", possible_solutions)