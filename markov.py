"""Generate Markov text from text files."""

import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file = open(file_path).read().replace("\n", " ")
    # print(file)

    return file


def combine_files():

    files_count = len(sys.argv) 

    all_text = ""

    i = 1 

    while i < len(sys.argv):
    # for i in range(files_count):

        all_text = all_text + open_and_read_file(sys.argv[i])

        i += 1

    #     file1_text = open_and_read_file(file_path1)
    #     file2_text = open_and_read_file(file_path2)

    # all_text = file1_text + file2_text

    return all_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # split text string into list of words
    words = text_string.split()

    # loop over list of words by index thru len - 1

    chains = {}

    for i in range(len(words) - 2):

        first_word = words[i]
        second_word = words[i+1]

        pair = (first_word, second_word)

        third_word = words[i+2]

        chains[pair] = chains.get(pair, [])
        chains[pair].append(third_word)

    return chains


def make_text(chains):
    """Return text from chains."""
    # Create empty list to add words to 
    sentence_words = []

    # We are adding to the list, a randomly selected pair of words from the 
    # chains dictionary keys to start our new sentence 
    current_key = random.choice(list(chains.keys()))
    first_word, second_word = current_key

    sentence_words.append(first_word)
    sentence_words.append(second_word)

    # While the current key is a valid key

    # uncomment to control length
    sentence_length = len(sentence_words)
    while current_key in chains and sentence_length < 200: 

    # while current_key in chains: 
    # Randomly select next word and add to list of sentence words
        next_word = random.choice(chains[current_key])
        sentence_words.append(next_word)
        # Update current key to use for lookup 
        current_key = (current_key[1], next_word)

        sentence_length = len(sentence_words) # uncomment for control length

    # Turn the list into a string
    return " ".join(sentence_words)


# input_path = "gettysburg.txt"
# input_path = "green-eggs.txt"
# input_path = "blank_space.txt"

# input_path1 = sys.argv[1]
# input_path2 = sys.argv[2]

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

input_text = combine_files()

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)
