
## Imagine you are on the Fog Owl with Cedric... ##
############ PROBLEM 1 #########################################

def find_average(nums):
    """
    The Flux Capacitor on the Fog Owl breaks.
    Make a function to calculate the average of an array of numbers
    (they may not all be integers, i.e. some may be floats).

    Args:
    nums: List[]

    Returns:
    An integer that is the average of the array.
    """
    sum=0
    count = 0
    for x in nums:
        sum += x
        count += 1
    return sum / count


def test_q1():
    assert find_average([3,4,5]) == 4

def test_q1_2():
    assert find_average([4,6,7,2]) == 4.75

def test_q1_3():
    assert find_average([3,4,5,5.899]) == 4.47475

############ PROBLEM 2 #########################################
# don't print given year
def find_leap_years(year):
    """
    Cedric is trying to plan his upcoming vacations with his future kids and grandkids.
    Create a function that prints the next 20 leap years given an input year.
    
    Args:
    year: int

    Returns:
    No return, only a print statement.
    """
    year += 1
    i = 0
    while year % 4 != 0:
        year += 1
    while i < 20:
        if (year % 100 != 0 or year % 400 == 0):
            print(year)
        year += 4
        i += 1


def test_q2_1(capfd):
    find_leap_years(1970)
    out, err = capfd.readouterr()
    assert out == '1972\n1976\n1980\n1984\n1988\n1992\n1996\n2000\n2004\n2008\n2012\n2016\n2020\n2024\n2028\n2032\n2036\n2040\n2044\n2048\n'

def test_q2_2(capfd):
    find_leap_years(2000)
    out, err = capfd.readouterr()
    assert out == '2004\n2008\n2012\n2016\n2020\n2024\n2028\n2032\n2036\n2040\n2044\n2048\n2052\n2056\n2060\n2064\n2068\n2072\n2076\n2080\n'

############ PROBLEM 3 #########################################

def sum_integers(string):
    """
    Cedric likes to play with numbers.
    Sometimes he is given a string containing numbers and characters,
    which he does not like.
    Write a function to help Cedric play with numbers that takes in a string and
    computes the sum of the integers embedded in the string. Does not need
    to account for negative numbers.

    Args:
    string: str

    Returns:
    An integer that is the sum of the integers in the input string.
    """
    sum = 0
    rev = reversed(string)
    pow = 1
    for c in rev:
        if c >= '0' and c <= '9':
            sum += pow * int(c)
            pow *= 10
        else:
            pow = 1
    return sum

def test_q3_1():
    assert sum_integers("123abc45def") == 168

def test_q3_2():
    assert sum_integers("24lol3bb100") == 127

############ PROBLEM 4 #########################################

def get_average_xp(xp, operators):
    """
    Cedric helps a lot of Operators learn to code in TwilioQuest.
    He wants to know the average XP earned by an Operator at an event.
    Write a function that takes in 2 integers: the first is the total XP earned by
    Operators during one event, and the second integer is the number of Operators at the event.
    The function should divide the first by the second, but there's a catch--
    Cedric's programming gets mixed up by the "%" and "/" keys, so you cannot use them.
    
    Args:
    xp: int
    operators: int

    Returns:
    An integer that is the average XP.
    """
    quotient = 0
    sum = 0
    while sum < xp:
        sum += operators
        quotient += 1
    if (sum > xp):
        quotient -= 1
    return quotient


def test_q4_1():
    assert get_average_xp(500, 10) == 50

def test_q4_2():
    assert get_average_xp(900, 30) == 30


############ EOF #########################################
