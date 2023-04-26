vowels = ('a', 'e', 'i', 'o', 'u')

while True:
    letter = input('Enter any letter. Enter Q to quit: ')

    if letter.isalpha() == False:
        print('Please only enter letters.')
        continue

    elif letter.lower() == 'q':
        break

    elif letter.lower() == 'y':
        print('Y can be both a vowel and consonant.')
    
    elif letter.lower() in vowels:
        print(letter + ' is a vowel')
    
    else:
        print(letter + ' is a consonant')
