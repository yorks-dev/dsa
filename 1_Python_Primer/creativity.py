from random import randint


# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
def reverseList(arr):
    reversedlist = []
    for i in range(len(arr) - 1, -1, -1):
        reversedlist.append(arr[i])
    # if(arr.reverse() == reversedlist):
    #     return reversedlist


# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
def hasOddPair(intArr):
    oddPair = []
    for num in intArr:
        if num % 2 != 0:
            oddPair.append(num)
    print(oddPair)
    return True if len(oddPair) > 1 and len(oddPair) % 2 == 0 else False


# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def isDistinct(n):
    distinctEl = {}
    for num in n:
        if distinctEl.get(num):
            return False
        else:
            distinctEl[num] = True
    return True


# C-1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?

# Answer: In python if you try to mutate an immutable types like int, python creates a new object and store the new value in it and refer the current variable to the it, and the original reference  isn't refererd by any other variable so it gets garbage collected.

data1 = [5, 6, 7, 8, 9]
import copy


def func(data):
    data_x = data[:]  # shallow copy make a new copy and mimics pass by value
    # data_x = copy.deepcopy(data)  # DEEP copy for nested and stuff
    data_x[0] *= -1
    print(data_x)


func(data1)
print(data1)

# C-1.17 Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
#     for val in data:
#         val = factor
# Explain why or why not.

# Answer: line 2 should be replaced by
# for j in range(len(data)):
#   data[j] *= factor

# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
comprehension = [i * (i + 1) for i in range(10)]

# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.
strComprehension = [chr(i) for i in range(97, 97 + 26)]

# C-1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.


def shuffle(data=[1, 2, 3, 4, 5, 2, 9]):
    for i in range(len(data) - 1):
        randomNo = randint(0, len(data) - 1)
        data[i], data[randomNo] = data[randomNo], data[i]

    # print(data)


# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
def readFileInReverse():
    fp = open("demo.txt")
    print(*fp.readlines()[::-1])


# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
def dotProduct(a, b):
    dotProductSum = 0  # dot product of a and b
    if len(a) == len(b):
        for i in range(len(a)):
            dotProductSum += a[i] * b[i]
    return dotProductSum


# C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”
def catchBufferOverflow(arr=[1, 2, 3, 4, 5]):
    try:
        arr[5]
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")


# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.
def vowelsCount(str):
    vowelCount = 0
    vowels = ["a", "e", "i", "o", "u"]
    for s in str:
        if s in vowels:
            vowelCount += 1
    return vowelCount


# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".
def rmPunctuation(s="Let's try, Mike."):
    return s.replace(",", "").replace("'", "").replace(".", "")


# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”


def arithmeticCheck():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))

    if a + b == c:
        return True
    elif a == b - c:
        return True
    elif a * b == c:
        return True
    else:
        return False


# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance advantages.


def factors(n):  # generator that computes factors

    stack = []
    k = 1
    while (k * k) < n:
        if n % k == 0:
            yield k
            stack.append(n // k)
        k += 1

    if k * k == n:  # special case if n is perfect square
        print(k)

    while len(stack) > 0:
        yield stack.pop()


def printFactor(n):
    factor = factors(n)
    try:
        while True:
            print(next(factor))
    except StopIteration:
        return


# printFactor(100)

# C-1.28 The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as

#                        ||v|| = p under root √v^p 1 + v^p 2 + .... + v^p n

# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
# Euclidean norm of √
# 42 +32 = √16+9 = √
# 25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.


def norm(v, p=2):
    vectorSquaredSum = 0
    for vector in v:
        vectorSquaredSum += vector**p
    rootOfP = vectorSquaredSum ** (1 / p)
    print(rootOfP)


# norm([4,3])
