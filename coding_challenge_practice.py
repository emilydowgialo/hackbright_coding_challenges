def decode(s):
    """Decode a string.

    A valid code is a sequence of numbers and letter, always starting with a number
    and ending with letter(s).

    Each number tells you how many characters to skip before finding a good letter.
    After each good letter should come the next next number.

    For example, the string "hey" could be encoded by "0h1ae2bcy". This means
    "skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

    A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
    """

    index = 0

    # Initialize an empty string for the new string
    string = ""

    for i in s:
        index += 1

        # Check if i is an integer, and add letter at an index that many spots
        # ahead of the current index to the string
        if i.isdigit():
            string += s[index + int(i)]

    return string


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # List of pig latin-ified words
    pigified = []

    # Split the input phrase on spaces
    phrase = phrase.split()

    # Pig latin-ify words in the phrase
    for word in phrase:
        if word[0] in 'aeiou':
            pigified.append(word + 'yay')

        else:
            pigified.append(word[1:] + word[0] + 'ay')

    # Return the pig latin string
    return (" ").join(pigified)


# def binary_search(val):
#     """Using a binary search, find val in a range of 1-100. Return # of guesses.

#     Construct a list of 1-100 (inclusive). Write a binary search that searches
#     for val in that list (val will always be a number between 1 and 100).

#     Return the number of searches it took to find val. For a proper binary search
#     of 1-100, this should never be more than 7.

#     >>> binary_search(50)
#     1

#     >>> binary_search(25)
#     2

#     >>> binary_search(75)
#     2

#     >>> binary_search(31) <= 7
#     True

#     >>> max([binary_search(i) for i in range(1, 101)])
#     7
#     """

#     num_guesses = 0

#     return num_guesses


def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    list_of_splits = []
    index = 0

    while index <= len(astring):
        current_index = index
        index = astring.find(splitter, index)

        if index != -1:
            list_of_splits.append(astring[current_index:index])
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            list_of_splits.append(astring[current_index:])
            break

    print list_of_splits

split("that is which is that which is that", " that ")


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

    Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
    """

    # Instantiate a new list
    c = []

    # While list a or b are londer than 0, compare items at index 1 and
    # append the smaller of the 2 to the new list
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b.pop(0))

        else:
            c.append(a.pop(0))

    # Extend list c by the remaining list
    c.extend(b)
    c.extend(a)

    return c

a = [1, 3, 5, 7]
b = [2, 6, 8, 10]
sort_ab(a, b)


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list.

    For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

    """

    # Initiate empty list for indexes
    indexes = []

    # If number is divisible by 0, add to list of indexes
    for index, num in enumerate(nums):
        if num % 2 == 0:
            indexes.append(index)

    return indexes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ROCK!\n"
