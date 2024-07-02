def count_letter_types_with_feedback(guess, feedback):
    letter_types = {}
    for i, letter in enumerate(guess):
        fb = feedback[i]
        if letter not in letter_types:
            letter_types[letter] = []
        letter_types[letter].append(fb)
    return letter_types


def filter_solutions(word_list, guesses, feedbacks):
    possible_words = word_list
    for guess, feedback in zip(guesses, feedbacks):
        filtered_words = []
        letter_types = count_letter_types_with_feedback(guess, feedback)

        for word in possible_words:
            match = True
            for i in range(5):
                if feedback[i] == 'G' and word[i] != guess[i]:
                    match = False
                    break
                elif feedback[i] == 'Y' and (word[i] == guess[i] or guess[i] not in word):
                    match = False
                    break
                elif feedback[i] == 'B':
                    if guess[i] in word and 0 == (letter_types[guess[i]].count('G') + letter_types[guess[i]].count('Y')) or guess[i] == word[i]:
                            match = False
                            break
            if match:
                filtered_words.append(word)

        possible_words = filtered_words

    return possible_words