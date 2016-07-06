def decode(s):
    """ Decode a string.

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

    # index = 0

    # # Initialize an empty string for the new string
    # string = ""

    # for i in s:
    #     index += 1

    #     # Check if i is an integer, and add letter at an index that many spots
    #     # ahead of the current index to the string
    #     if i.isdigit():
    #         string += s[index + int(i)]

    # return string

    string = ""
    i = 0

    while i < len(s):
        how_many_to_skip = int(s[i])
        i += how_many_to_skip + 1

        string += s[i]

        i += 1

    return string


def pig_latin(phrase):
    """ Turn a phrase into pig latin.

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


def binary_search(val):
    """ Using a binary search, find val in a range of 1-100. Return # of guesses.

    Construct a list of 1-100 (inclusive). Write a binary search that searches
    for val in that list (val will always be a number between 1 and 100).

    Return the number of searches it took to find val. For a proper binary search
    of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """

    # Initialize the number of guesses at 0
    num_guesses = 0

    # Set the bounds, which in this case is 1 to 100 inclusively
    left = 0
    right = 101
    guess = None

    # While we have not guessed val, increase the number of guesses and
    # reset the bounds
    while guess != val:
        num_guesses += 1
        guess = (right - left)/2 + left

        if val > guess:
            left = guess

        if val < guess:
            right = guess

    return num_guesses


class Node(object):
    """ Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

    def reverse_linked_list(self):
        """ Given LL head node, return head node of new, reversed linked list.

        >>> ll = Node(1, Node(2, Node(3)))
        >>> ll.reverse_linked_list().as_string()
        '321'
        """

        nodes = []
        n = self

        #traverse nodes and put nodes into a list
        while n.next is not None:
            nodes.append(n)
            n = n.next

        nodes.append(n)
        # reassign elements in list, nodes right now is [A, B, C]
        nodes.reverse()
        for i, node in enumerate(nodes):
            if i != (len(nodes) - 1):
                node.next = nodes[i + 1]

            else:
                node.next = None

        # Return the head node
        return nodes[0]


def remove_node(node):
    """ Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.

    For example::

    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> three_node = ll.next.next
    >>> remove_node(three_node)
    >>> ll.as_string()
    '1245'

    It's possible to remove the first node::

    >>> ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    >>> one_node = ll
    >>> remove_node(one_node)
    >>> ll.as_string()
    '2345'

    This will never be asked to remove the tail node.
    """

    node.data = node.next.data
    node.next = node.next.next


def recursive_index(needle, haystack):
    """ Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

    """
    # Base case
    if len(haystack) == 0:
        return None

    if haystack[0] == needle:
        return 0

    is_this_none = recursive_index(needle, haystack[1:])

    # If the list contains items, add 1 and call the function
    if is_this_none is not None:
        return 1 + is_this_none
    else:
        return None


def reverse_linked_list_in_place(lst):
    """ Given linked list, reverse the nodes in this linked list in place."""

    # Set the current node's properties
    current = lst.head
    previous = None

    # The loop will end when current.next is None, and rebinds each node
    while current.next is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    lst.head = previous


def print_recursively(lst):
    """ Print items in the list, using recursion.

    For example::

    >>> print_recursively([1, 2, 3])
    1
    2
    3

    """

    # If lst > 0, print the first item in the list and
    # call the function on the rest of the list
    if lst:
        print lst[0]
        print_recursively(lst[1:])


def split(astring, splitter):
    """ Split astring by splitter and return list of splits."""

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

    return list_of_splits

split("that is which is that which is that", " that ")


def sort_ab(a, b):
    """ Given already-sorted lists, `a` and `b`, return sorted list of both.

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


def missing_number(nums, max_num):
    """ Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """

    # List of "False" as long as the max number
    new_list = [False] * max_num

    # Change everything to True
    for num in nums:
        new_list[num - 1] = True

    # Find where the remaining False is
    return new_list.index(False) + 1


def count_recursively(lst):
    """ Count items in a list recursively.

    For example:

    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3

    """

    # Base case: if the list contains no items
    if not lst:
        return 0

    # Return 1 and call the function using a sliced list
    return 1 + count_recursively(lst[1:])


def print_digits(num):
    """ Given int, print each digit in reverse order, starting with the ones place.

    For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

    """

    # Turn num into a string
    num = str(num)

    # Print numbers starting backwards
    for n in num[::-1]:
        print n


def show_evens(nums):
    """ Given list of ints, return list of *indices* of even numbers in list.

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


def make_change(num):
    """ Given a change amount, how many of each coin to give to customer?

    >>> make_change(.96)
    [3, 2, 0, 1]
    """
    num = int(num * 100)

    # [quarters, dimes, nickels, pennies]
    coin_amounts = [25, 10, 5, 1]
    coin_list = [0, 0, 0, 0]

    # if (num / 25) > 0:
    #     coin_list[0] = (num / 25)
    #     new_amount = (num % 25)

    # if (new_amount / 10) > 0:
    #     coin_list[1] = (new_amount / 10)
    #     new_amount = (new_amount % 10)

    # if (new_amount / 5) > 0:
    #     coin_list[2] = (new_amount / 5)
    #     new_amount = (num % 5)

    # if new_amount < 10:
    #     coin_list[3] = new_amount

    index = 0
    for amount in coin_amounts:
        coin_list[index] = (num / amount)
        num = (num % amount)
        index += 1

    return coin_list


def is_anagram_of_palindrome(word):
    """ Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("racecar")
    True

    >>> is_anagram_of_palindrome("ajshgdjh")
    False
    """

    # {Key: value} - {letter: frequency}
    seen = {}

    for letter in word:
        count = seen.get(letter, 0)
        seen[letter] = count + 1

    is_an_odd = 0

    for count in seen.values():
        if count % 2 != 0:
            is_an_odd += 1

    if is_an_odd > 1:
        return False

    else:
        return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ROCK!\n"
