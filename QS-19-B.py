"""
Question (B) : Implementing programs using string (palindrome)
"""

usr_input = input("Enter an String: ")
rev_input = usr_input[::-1]

if usr_input == rev_input:
    print("This is an Palindrome")
else:
    print("This isn't an Palindrome")


"""
OUTPUT 1:
-----
Enter an String: mam
This is an Palindrome

OUTPUT 2:
-----
Enter an String: mama
This isn't an Palindrome

"""