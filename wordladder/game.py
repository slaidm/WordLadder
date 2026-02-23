from .dataset import load_dataset, prune
from .core import pretty_print, test, calculate_changes
import random

"""
Game:

1. Get the size of the word ladder
2. Load the dataset
3. Prune the dataset
4. Choose 2 random words for start / end
5. Print out size, and 2 words
6. Loop until user forms a word ladder between start and end
7. Print out the word ladder

"""
def game():
    size = int(input("Enter size of word ladder: "))
    number_of_guesses = 10
    number_of_changes = 1

    if not isinstance(size, int):
        raise Exception("Size must be a number")

    # org_dataset = load_dataset("google-10000-english-usa.txt", 'text')
    org_dataset = load_dataset("unigram_freq.csv", 'csv')
    ds = prune(size, org_dataset)

    #Get the first and last word
    word_ladder = random.sample(ds, 2)

    print(f"""
  STARTING WORD LADDER OF SIZE {size}
  {pretty_print(word_ladder)}
  """)

    old_word = word_ladder[0]
    target = word_ladder[1]
    for guess in range(number_of_guesses):
        new_word = input("Enter new word or CTRL-C to give up: ").lower()

        # Add some checks to input

        if test(old_word, new_word, number_of_changes, set(ds)):
            word_ladder.insert(len(word_ladder) - 1, new_word)
            old_word = new_word
            print(pretty_print(word_ladder))

        if calculate_changes(old_word, target) == number_of_changes:
            print("Word Ladder Completed!")
            break
