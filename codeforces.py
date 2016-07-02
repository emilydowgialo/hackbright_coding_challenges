# http://codeforces.com/problemset/problem/1/A
def theatre_square(stuff):
    """
    For example::

    >>> theatre_square("50 5 4")
    26

    >>> theatre_square("6 6 4")
    4

    """

    # Split string
    stuff_split = stuff.split()

    # Bind variables
    n = int(stuff_split[0])
    m = int(stuff_split[1])
    a = int(stuff_split[2])

    # Call helper function to get how many tiles per side are needed
    side_m = side_measurer(m, a)
    side_n = side_measurer(n, a)

    # Return num tiles per side multiplied to get the total
    return (side_m * side_n)


def side_measurer(side, a):
    """ Helper function for theatre_square """

    # This gives the number of tiles per side
    num_tiles = (side / a)

    # If there are any remaining, because we can go over the area, we add 1
    if (side % a) > 0:
        num_tiles += 1

    return num_tiles
