# Lab 12 - Document Analysis System

sentence = input("Enter a sentence: ")

print("="*50)
print("      DOCUMENT ANALYSIS REPORT")
print("="*50)
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

# Initialize counters
words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

vowel_list = "aeiouAEIOU"

# Analyze each character
for ch in sentence:
    if ch.isalpha():
        if ch in vowel_list:
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        # anything that isn't letter, digit, or space
        special += 1

print("\n--- Character Breakdown ---")
print(f"Words:                {words}")
print(f"Vowels:               {vowels}")
print(f"Consonants:           {consonants}")
print(f"Digits:               {digits}")
print(f"Spaces:               {spaces}")
print(f"Special characters: {special}")

# Summary
total_letters = vowels + consonants
vowel_percent = 0
if total_letters > 0:
    vowel_percent = (vowels / total_letters) * 100

print("\n--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percent:.1f}%")

print("\n" + "="*50)
print("Analysis Complete!")
print("="*50)