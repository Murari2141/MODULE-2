def longest_word_length(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

word_list = input("Enter a list of words (space-separated): ").split()
result = longest_word_length(word_list)
print("Length of the longest word:", result)
