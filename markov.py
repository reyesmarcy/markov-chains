"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file = open(file_path).read().replace("\n", " ")
    # print(file)

    return file


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
    first_word = current_key[0]
    second_word = current_key[1]

    sentence_words.append(first_word)
    sentence_words.append(second_word)

    # Set a new randomly selected next word based on the values from the 
    # key pair above and added to list of sentence words
    next_word = random.choice(chains[current_key])
    sentence_words.append(next_word)


# After the first key is taken: 

    # We are updating current key to use for the lookup 
    current_key = (second_word, next_word)

    # While the current key is a valid key
    while current_key in chains: 
    # Randomly select next word and add to list of sentence words
        next_word = random.choice(chains[current_key])
        sentence_words.append(next_word)
        # Update current key to use for lookup 
        current_key = (current_key[1], next_word)

    # Turn the list into a string
    return " ".join(sentence_words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)
