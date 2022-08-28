import random
import time
import sys

minimum = int(input('Enter the minimum number. '))

maximum = int(input('Enter the maximum number. '))

number = random.randint(minimum, maximum)

print('The random number is', number)

print('Press Enter to close the window.')
Quit = sys.stdin.readline()