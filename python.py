# l =[]
# for i in range(10):
#     if i%2:
#         l.append(i)
# print(l)
#
# # list compression
# ls = [i for i in range(10) if i%2]
# print(ls)
#
# # dict
# d = {}
# for i in range(1,10):
#     sqr = i*i
#     d[i] = i*i
# print(d)
#
# d = {n:n*n for n in range(1,10)}
# print(d)
#
# # genearotor
# def sqr(n):
#     for i in range(1,n+1):
#         yield i*1
# a = sqr(4)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#
#
# # iterrator
# _list = iter(['A','B','C'])
# print(next(_list))
# print(next(_list))


# palindrome sring or number
# A. By using split Method

def Palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes! It's Palindrome")
    else:
        print("No!! It's not Palindrome")
s = 'deved'
Palindrome(s)

# By using indexing / suing for loop
def Palindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True
s = 'deved'
print(Palindrome(s))

# By using Inbuilt functions - reversed and join
def Palindrome1(s):
    reverse_s = reversed(s)
    print(reverse_s)
    for i in reverse_s:
        print(i)

import re

text = "The quick brown fox jumps over the lazy dog."

# Find all occurrences of the letter "a" in the text
result = re.findall(r"a", text)

print(result)


def one_letter_off(s1: str, s2: str) -> bool:
    """Return True if the two strings are one letter off, False otherwise.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        A bool indicating whether the two strings are one letter off.
    """
    # Zip the strings and count the number of differences
    diff_count = sum(c1 != c2 for c1, c2 in zip(s1, s2))

    # Return True if the difference count is 1, False otherwise
    return diff_count == 1


# Test the function
print(one_letter_off("cat", "bat"))  # Output: True
print(one_letter_off("cat", "dog"))  # Output: False
print(one_letter_off("cat", "cat"))  # Output: False


