"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1
Kanye West
Kim Kardashian
Example Output 1
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
Example Input 2
Brad Pitt
Jennifer Aniston
Example Output 2
The Love Calculator is calculating your score...
Your score is 73.
Hint
You can check your values against mine using this table:

Name 1	Name 2	Score
Brad Pitt	Jennifer Aniston	73
Prince William	Kate Middleton	67
Ashton Kutcher	Mila Kunis	63
Angela Yu	Jack Bauer	53
David Beckham	Victoria Beckham	45
Mario	Princess Peach	43
Kanye West	Kim Kardashian	42

"""

print("The Love Calculator is calculating your score...")
name1 = input("Write the first full name here: ") # What is your name?
name2 = input("Write the second full name here: ")  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true_word = "true"
love_word = "love"
take_names = name1 + name2
letters = take_names.lower()

true_t = letters.count("t")
print(f"T occurs {true_t} times")
true_r = letters.count("r")
print(f"R occurs {true_r} times")
true_u = letters.count("u")
print(f"U occurs {true_u} times")
true_e = letters.count("e")
print(f"E occurs {true_e} times")

total_true = true_t + true_r + true_u + true_e
print(f"Total: {total_true}")

love_l = letters.count("l")
print(f"T occurs {love_l} times")
love_o = letters.count("o")
print(f"R occurs {love_o} times")
love_v = letters.count("v")
print(f"U occurs {love_v} times")
love_e = letters.count("e")
print(f"E occurs {love_e} times")

total_love = love_l + love_o + love_v + love_e
print(f"Total: {total_love}")

total = str(total_true) + str(total_love)

total_int = int(total)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int > 40 and total_int < 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}")










