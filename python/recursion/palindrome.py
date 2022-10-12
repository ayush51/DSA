from ast import Str
from posixpath import abspath


def palindrome(str: Str, l):
    n = len(str)
    if l >= n//2:
        return
    if str[l] == str[n-l-1]:
        palindrome(str,l+1)
        print("True")
    else:
        print("False")
    

palindrome('abac', 0)

