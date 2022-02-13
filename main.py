import random
import math

#taking inputs

Start = int(input("Enter the start Number : "))
End = int(input('Enter the End Number : '))

num = random.randint(Start,End)
print('\n\t you have only ', round(math.log(End-Start+1,2)), 'chances to guess the integer!! \n')

count = 0

while count< math.log(End-Start+1,2):
    count +=1
    guess = int(input('Guess a Number: '))

    if num == guess:
        print(f'Congratulation {count} try')
        break
    elif num > guess:
        print('You have guessed small Number ')
    elif num< guess:
        print("Number is Larger")
    else:
        print('Invalid Number')

if count >= math.log(End-Start+ 1,2):
    print(f"\n the number is {num}")
    print('\t better luck next time ')


