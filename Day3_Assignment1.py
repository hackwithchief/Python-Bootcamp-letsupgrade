# Write a Python program to find whether a given number (accept from the user) is even or odd

#First we are taking an input from the user and converting it into an integer
a=int(input("Enter a number: "))

#Here we are checking that is we divide a from 2 then if remainder is 0, if it is then it is even
if(a%2==0):
    print("Given number is even")
#Otherwise it is a odd number
else:
    print("Given number is odd")
