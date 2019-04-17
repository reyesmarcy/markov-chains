"""Generate Markov text from text files."""

import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path).read()
    bad_characters = ["@", ",", ":", ";","--", "-", "*","(", ")", "^", "+", "_", "~"]
    
    sentence_ending_punctuation = [".", "?", "!"]

    for char in bad_characters:
        file = file.replace(char, "")
        print("replaced:", char)



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


def make_chains(text_string, n = 2):
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

    # loop over list of words by index thru len - n
    chains = {}

    for i in range(len(words) - n):
        # Used slicing to create a n-gram tuple key from i:i+(n-1)
        tuple_key = (tuple(words[i:(i + n)]))
        # Get the word at the nth index to add to the keys' corresponding list of values
        word_to_add_to_list = words[i + n]

        # Add keys and values to dictionary 
        chains[tuple_key] = chains.get(tuple_key, [])
        chains[tuple_key].append(word_to_add_to_list)


    return chains


def make_text(chains, output_length = 200):
    """Return text from chains."""
    # Create empty list to add words to 
    # sentence_words = []

    # We are adding to the list, a randomly selected pair of words from the 
    # chains dictionary keys to start our new sentence 
    current_key = random.choice(list(chains.keys()))

    print(current_key)
    print()

    sentence_words = list(current_key)

    # first_word, second_word = current_key

    # sentence_words.append(first_word)
    # sentence_words.append(second_word)

    # While the current key is a valid key

    # uncomment to control length
    sentence_length = len(sentence_words)
    while current_key in chains and sentence_length < output_length: 

    # while current_key in chains: 
    # Randomly select next word and add to list of sentence words
        next_word = random.choice(chains[current_key])
        sentence_words.append(next_word)

        # Update current key to use for lookup 
        current_key = list(current_key[1:])
        current_key.append(next_word)
        current_key = tuple(current_key)
        
        print(current_key)
        print()
        sentence_length = len(sentence_words) # uncomment for control length

    # Turn the list into a string
    return " ".join(sentence_words)


# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

input_text = combine_files()

# Get a Markov chain
chains = make_chains(input_text, 3)
# print(chains)
print()
# # Produce random text
random_text = make_text(chains)

print(random_text)
