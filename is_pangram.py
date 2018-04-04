def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    # START SOLUTION

    used = {}

    for char in sentence.lower():
        if char.isalpha():
            used[word] = used.get(char, 0) + 1

    return len(used) == 26