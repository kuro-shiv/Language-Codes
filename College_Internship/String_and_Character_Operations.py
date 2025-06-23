#Print all characters of a string

def print_characters(s):
    if not s:
        print("The string is empty.")
        return
    for char in s:
        print(char, end=' ')
    print("\n")

#Print ASCII value of each character in a string
def print_ascii_values(s):
    if not s:
        print("The string is empty.")
        return
    for char in s:
        print(f"ASCII value of '{char}': {ord(char)}")
    print("\n")

#Count vowels and consonants in a string
def count_vowels_and_consonants(s):
    if not s:
        print("The string is empty.")
        return
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    print("\n")


#Reverse a string
def reverse_string(s):
    if not s:
        print("The string is empty.")
        return
    reversed_s = s[::-1]
    print(f"Reversed string: {reversed_s}")
    print("\n") 


#calling all functions
if __name__ == "__main__":
    s = input("Enter a string: ")
    
    print("Characters in the string:")
    print_characters(s)
    
    print("ASCII values of characters:")
    print_ascii_values(s)
    
    print("Counting vowels and consonants:")
    count_vowels_and_consonants(s)
    
    print("Reversing the string:")
    reverse_string(s)

   