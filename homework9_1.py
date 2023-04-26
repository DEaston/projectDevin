import random
from pathlib import Path

mainList = ['Spaghetti', 'Pizza', 'Lasagna', 'Wings', 'Hamburger']
vegList = ['Baked Potato', 'Celery', 'Carrots', 'Steamed Broccoli', 'Squash']
sideList = ['French Fries', 'Tater Tots', 'Onion Rings', 'Rice', 'Side Salad']
treatList = ['Ice Cream', 'Flan', 'Slice of Pie', 'Brownie', 'Cookies']
bevList = ['Water', 'Sweet Tea', 'Lemonade', 'Soda', 'Wine']

menuFile = open(Path.home() / 'menu.txt', 'w')

menuFile.write('Hello! Here is today\'s menu!\n')
menuFile.write('Your main dish is: ' + random.choice(mainList) + '\n')
menuFile.write('Your vegetable is: ' + random.choice(vegList) + '\n')
menuFile.write('Your side is: ' + random.choice(sideList) + '\n')
menuFile.write('Your treat is: ' + random.choice(treatList) + '\n')
menuFile.write('Your beverage is: ' + random.choice(bevList) + '\n')

menuFile.close()