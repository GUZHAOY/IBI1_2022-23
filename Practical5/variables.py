# Store longitudes of Edinburgh, Los Angeles, and Haining in variables
a = -3.19
b = -118.24
c = 116.39

# Calculate longitude distance travelled to Los Angeles
d = abs(a - b)

# Calculate longitude distance travelled to Haining
e = abs(a - c)

# Compare d and e to determine which distance is greater
if d > e:
    print("Rob travelled further to Los Angeles.")
else:
    print("Rob travelled further to Haining.")
#The answer is "Rob travelled further to Haining."
# Create Boolean variables X and Y
X = True
Y = False

# Create Boolean variables W and Z
W = X and Y
Z = X or Y

# Print the values of W and Z
print("The value of W is:", W)
print("The value of Z is:", Z)
#The answer is 
#The value of W is: False
#The value of Z is: True
