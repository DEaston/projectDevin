def avgNums(numCount):
    total = 0

    for i in range(int(numCount)):
        print('Enter number ' + str(i + 1))
        number = int(input())
        total = total + number
    
    average = total / int(numCount)
    print(average)

keepGoing = True
while(keepGoing):
    
    print('Hello! This program will average any amount of numbers you want.')
    print('How many numbers do you want to average?')

    count = input()
    avgNums(count)

    print('Do you want to continue averaging numbers? Y/N')
    answer = input()
    
    if answer == 'Y' or answer == 'y':
        keepGoing = True
    else:
        keepGoing = False
        print('Thanks for using this program!')