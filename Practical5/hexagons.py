#For each value of n in the range from 1 to 5, do the following:
#Calculate h using the formula 2n(2*n-1)/2
#Convert h an integer using the int() function
#Print the value of j to the console.

for n in range(1,6): #This is tell us it will compute n from 1 to 5.
    h=2*n*(2*n-1)/2
    print(int(h)) #If int() isn't used, it will print like 1.0/6.0....
#Result
#1
#6
#15
#28
#45
 
