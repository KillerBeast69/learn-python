def count_vowels(text):
    vowels = set('a', 'e', 'i', 'o', 'u')
    vowels_cap = set('A', 'E', 'I', 'O', 'U')
    count = 0
    found = set()
    for letter in text:
        if letter in vowels or vowels_cap:
            count += 1
            found.add(letter)
    return count, found