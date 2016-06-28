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


def binary_search(val):
    """Using a binary search, find val in a range of 1-100. Return # of guesses.

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

    num_guesses = 0

    left = 0
    right = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (right - left)/2 + left

        if val > guess:
            left = guess

        if val < guess:
            right = guess

    return num_guesses


class Node(object):
    """Class in a linked list."""

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
        """Given LL head node, return head node of new, reversed linked list.

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
    """Given a node in a linked list, remove it.

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
    """Given list (haystack), return index (0-based) of needle in the list.

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
    if len(haystack) == 0:
        return None

    if haystack[0] == needle:
        return 0

    is_this_none = recursive_index(needle, haystack[1:])

    if is_this_none is not None:
        return 1 + is_this_none
    else:
        return None


def print_recursively(lst):
    """Print items in the list, using recursion.

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


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    current = lst.head
    previous = None

    while current.next is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    lst.head = previous


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

    return list_of_splits

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


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

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
