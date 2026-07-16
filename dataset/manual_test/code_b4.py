def count_vowels(sentence):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}

    total_vowels = sum(
        1 for character in sentence.lower()
        if character in vowel_set
    )

    return total_vowels


user_input = input("Enter a string: ")

result = count_vowels(user_input)

print(f"Number of vowels: {result}")