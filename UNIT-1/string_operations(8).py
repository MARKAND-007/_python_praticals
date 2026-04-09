# Program to perform various string operations

text = input("Enter a string: ")
vowels = "aeiou"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

length = 0
for ch in text:
    length += 1
print("Length of string:", length)


reversed_string = ""
for ch in text:
    reversed_string = ch + reversed_string
print("Reversed string:", reversed_string)

find_word = input("Enter word to find: ")
replace_word = input("Enter word to replace with: ")
new_text = text.replace(find_word, replace_word)
print("String after replace:", new_text)

cleaned_text = ""
for ch in text:
    if ch != " ":
        cleaned_text += ch.lower()

reverse_check = ""
for ch in cleaned_text:
    reverse_check = ch + reverse_check

if cleaned_text == reverse_check:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")
