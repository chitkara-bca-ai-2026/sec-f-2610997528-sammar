print("="*50)
print("          TEXT PROCESSING TOOL")
print("="*50)

# 1. Accept a sentence
sentence = input("Enter a sentence: Hello World\nEnter a sentence: ")
# If you want it simple, use just:
# sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# 2. Display character at specific position using indexing
pos = int(input("Enter position for indexing: "))
# Handle invalid position
if pos < len(sentence):
    char_at_pos = sentence[pos]
    print(f"Character at position {pos}   : '{char_at_pos}'")
else:
    print("Position out of range!")

# 3. Extract portion using slicing
start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
sliced = sentence[start:end]
print(f"Sliced string [{start}:{end}]          : '{sliced}'")

# 4. Convert to uppercase
upper_case = sentence.upper()
print(f"Uppercase                     : {upper_case}")

# 5. Convert to lowercase
lower_case = sentence.lower()
print(f"Lowercase                     : {lower_case}")

# 6. Replace a specified word
old_word = input("Enter word to replace         : ")
new_word = input("Enter replacement word        : ")
replaced_sentence = sentence.replace(old_word, new_word)
print(f"After replace                 : {replaced_sentence}")

# 7. Find length
length = len(sentence)
print(f"Length of sentence            : {length}")

print("\n" + "="*50)
print("Analysis Complete!")
print("="*50)