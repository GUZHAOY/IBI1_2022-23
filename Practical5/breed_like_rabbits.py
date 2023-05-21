# Start with two rabbits
rabbits = 2
# Initialize generation counter
generation = 1

# Keep breeding until there are at least 100 rabbits
while rabbits < 100:
    # Calculate the number of rabbits in this generation
    rabbits = rabbits * 2
    # Increment the generation counter
    generation += 1

# Output the number of generations it took to exceed 100 rabbits
print("It takes " + str(generation) + " generations to have at least 100 rabbits.")

