


# This program counts the vowels in any given/entered string

name = input("Enter your name: ")
vowel_count = 0

for letter in name:                   # `letter` is just a variable
    if letter in "aeiouAEIOU":        # if the loop finds that the value of `letter` is in the string `aeiouAEIOU`   
        vowel_count += 1              # it updates the `vowel_cuont`, and keeps looping until all letters in the entered string have been checked.

print("Vowels", vowel_count)