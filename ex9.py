# Create a function that checks whether a given string is a palindrome, such as the word madam.

######### SOLUTION #########

def is_palindrome(word):
    backwards = ""

    for i in range(0, len(word)):
        letter = word[- i - 1]
        backwards += letter

    if word == backwards:
        return "This word is a palindrome"

    return "This word is not a palindrome"

test1 = is_palindrome("apple")
print(test1)

test2 = is_palindrome("madam")
print(test2)

test3 = is_palindrome("ball")
print(test3)

test4 = is_palindrome("radar")
print(test4)

test5 = is_palindrome("refer")
print(test5)

# Alternative using python tricks

def is_palindrome_2(word):
    if word == word[::-1]:
        return "This word is a palindrome"
    
    return "This word is not a palindrome"

test6 = is_palindrome_2("madam")
print(test6)