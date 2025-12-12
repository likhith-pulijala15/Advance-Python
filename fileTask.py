vowel_count = 0
consonant_count = 0
word_freq = {}   
vowels = "aeiou"

# with open("task.txt", "w") as f:
#     lines = ["Hello\n","Java\n","Python\n","HTML\n","CSS\n","JavaScript\n","Java\n","CSS\n"]
#     f.writelines(lines)

with open("task.txt", "r") as f:
    data = f.read()

# Word Count
words = data.split()
word_count = len(words)
print(f"Word Count: {word_count}")

# Word Frquency
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\n--- Word Frequency ---")
for w, frq in word_freq.items():
    print(w, ":", frq)

# Vowels and consonants
for ch in data:
    if ch.isalpha():
        if ch.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"\nVowel Count: {vowel_count}")
print(f"Consonant Count: {consonant_count}")