nameList = []
colorList = []
animalList = []
import random

print('Please enter names (one at a time, please) to fill our list. Enter a blank message to quit.')

while True:
    name = input()
    if name == '':
        break
    nameList += [name]

print('Please enter colors (one at a time, please) to fill our list. Enter a blank message to quit.')

while True:
    color = input()
    if color == '':
        break
    colorList += [color]

print('Please enter animals (one at a time, please) to fill our list. Enter a blank message to quit.')

while True:
    animal = input()
    if animal == '':
        break
    animalList += [animal]

for i in range(10):
    print('Sorry I was late ' + random.choice(nameList) + '. I spilled mustard on my ' + random.choice(colorList) + ' pants and my pet ' + random.choice(animalList) + ' took a bite out of them!')