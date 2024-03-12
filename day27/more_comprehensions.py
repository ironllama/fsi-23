# Generate your own lists of numbers, sentences, and strings for these
#  exercises and use several permutations to verify that they work
#  as intended!

# 1. Given a list of numbers, write a list comprehension that produces a
#     list of strings of each number that is divisible by 5.
nums = [234, 55, 3, -15, 223, 60, -4, 34, 10]
print("1:", [n for n in nums if n % 5 == 0])


# 2. Given a sentence, produce a list of the lengths of each word in the
#     sentence, but only if the word is not 'the'.
sentence = "The boys are in the championship wrestling match."
print("2:", [len(word) for word in sentence.split() if word.lower() != "the"])


# 3. Given a string representing a word, write a list comprehension that
#     produces a list of all the vowels in that word.
word = "destroyed"
print("3:", [char for char in word if char in 'aeiou'])


# 4. Given a string representing a word, write a set comprehension that
#     produces a set of all the vowels in that word.
print("4:", {char for char in word if char in 'aeiou'})


# 5. Given a sentence, return the sentence with all vowels removed.
sentence = "The giant worm terrified him."
# print("5:", "".join(filter(lambda char: char not in 'aeiou', sentence)))
print("5:", "".join([char for char in sentence if char not in 'aeiou']))


# 6. Given a list of numbers, return the list with all even numbers doubled,
#     and all odd numbers turned negative.
nums = [234, 55, 3, -15, 223, 60, -4, 34, 10]
print("6:", [(n + n) if n % 2 == 0 else -n for n in nums])


# 7. Given a sentence, return a new sentence with all its letters transposed
#     by 1 letter right in the alphabet, but only if the new letter is
#     between b and y, inclusive.
sentence = "The chandelier swayed in the breeze, sending dust drifting over the tables."
alpha = "abcdefghijklmnopqrstuvwxyz"
# print("7:", "".join([
#         alpha[alpha.find(char) + 1]   # Transpose one letter
#             if char in alpha[1:-2]    # If between b-y inclusive
#             else char                 # Else leave as is
#         for char in sentence.lower()  # For each character in lowercased sentence
#     ]))

# Same, on one line.
print("7:", "".join([alpha[alpha.find(c) + 1] if c in alpha[1:-2] else c for c in sentence.lower()]))


# 8. Given a list of floats and ints, remove the floats (numbers with decimals).
nums = [234, 5.5, 3.0, -15.333333, 60, -4, 34.2, 10]
print("8:", [n for n in nums if isinstance(n, int)])
