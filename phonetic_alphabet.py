phonetic_dict = {'a': 'Alpha', 'b': 'Beta', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo'
                 , 'f': 'Foxtrot', 'G': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett'
                 , 'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar'
                 , 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango'
                 , 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee'
                 , 'z': 'Zulu'}

def convert_phonetic(char):
    letter = char.lower()
    phonetic = phonetic_dict.get(letter, letter)
    print(phonetic, end=' ')

while True:
    user_word = input("\n\nEnter a word to see the phonetic alphabet version.\nq to quit\n-=> ")
    print()
    if user_word.lower() == 'q': break
    for char in user_word:
        convert_phonetic(char)
        if char == " ":
            print()
