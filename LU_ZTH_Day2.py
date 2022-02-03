'''
PROJECT :
Let's say, you are in a lottery competition. A group of words has been given to you and you are asked to select any one
character(only alphabets) which will get you a prize. You are a smart person and you thought of a way to select a
character that will have maximum chances of winning a prize i.e. select the highest occurring character from the words.
Given this situation you are required to write a code in Python that will select a character from the words that occurs
the most.

Note:
Prizes may be allotted to the characters in any manner (sequential or alternate or any other way). Some characters may
not be entitled for any prize.
Ignore spaces and other special character. Consider only alphabets for prizes.
Assume that all characters will be in lowercase.

Example:
Word Given: hello coders
If Index of characters assigned with prize are as below: 0, 1, 4, 6, 8
Then if you choose the characters at the above indices, only then you will win a prize.
Selecting any of the following characters 'h' or 'e' or 'o' or 'c' or 'd' will only get you a prize.

'''
# Assignment : Program
a = "hello coders"
x = input("Enter a character: ")
if x == a[0].lower() or x == a[1].lower() or x == a[4].lower() or x == a[6].lower() or x == a[8].lower():
    print("Congratulations!! You Won a lottery Prize")
else:
    print("Oops!! Sorry It was a wrong guessing")