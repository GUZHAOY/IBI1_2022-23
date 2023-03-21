# What does this piece of code do?
# Answer:This piece of code generates a random integer between 1 and 100, and stores the largest random integer generated over a loop of 10 iterations. The loop increments a progress counter on each iteration and compares the newly generated random number to the previous stored number. If the new number is larger, it becomes the new stored number. After 10 iterations, the largest generated number is printed.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
