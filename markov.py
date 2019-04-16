"""Generate Markov text from text files."""

from random import choice


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

    # make list of tuples
    word_pairs = []

    # loop over list of words by index thru len - 1

    chains = {}

    for i in range(len(words) - 1):

        first_word = words[i]
        second_word = words[i+1]

        pair = (first_word, second_word)

        # if index of second word is not the last word in list:
        if i + 1 != (len(words) - 1):

            third_word = words[i+2]

            chains[pair] = chains.get(pair, [])
            chains[pair].append(third_word)

        # if key (first_word, second_word) not in chains, add it
        # if there is a third word, add that to the  key's list
        # if no third word, add the first word in words list 
        # word_pairs.append((first_word, second_word))


    # add each word pair tuple as a key in chains dict 
    # with val of empty list
   

    # for pair in word_pairs:
    #     chains[pair] = []

    # look for would 
        # for each time - look for whether followed by you
            # add the word after you to list 

    # for i in range(len(words) - 1):
    #     if words[i:i+2] == 


    # for chain in chains:
           

    print(chains)
    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
