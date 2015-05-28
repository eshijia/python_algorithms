"""

Author: E Shijia (Jack)

Description: This is the solution to exercises(1-2) in the book, Python Algorithms.

"""


def anagrams(str_a="", str_b=""):
    list_a = sorted(list(str_a))
    list_b = sorted(list(str_b))

    length_a = len(list_a)

    if length_a != len(list_b):
        return False
    else:
        i = 0
        while i < length_a:
            if list_a[i] == list_b[i]:
                i += 1
            else:
                return False
        return True

if __name__ == '__main__':
    test_str1 = "debit card"
    test_str2 = "bad credit"
    print "The two strings are anagrams of each other?", anagrams(test_str1, test_str2)