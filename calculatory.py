#x = input("What's x?")
#y = input("What's y?")

#Convert the return value into an int that use the + operator
# z = x + y will concatenate the two str to give an incorrect value
#z = int(x) + int(y)

#print(z)

## This is a more elegant way of sloving our problem. We convert the input directly into an int
#x = int(input("What's x?"))
#y = int(input("What's y?"))

#print(x + y)

#We can support float numbers numbers with decimal points by calling float on our input
#x = float(input("What's x?"))
#y = float(input("What's y?"))

#print(x + y)

# Adding support for rounding the float
# How round works round(number[, ndigits]) 
#x = float(input("What's x?"))
#y = float(input("What's y?"))

#z = round(x + y)
#print(z)

#Add formating with commas American Standard great for really large values
#x = float(input("What's x?"))
#y = float(input("What's y?"))
#z = round(x + y)
#print(f"{z:,}")

#Let's divide 
x = float(input("What's x?"))
y = float(input("What's y?"))

z = x / y
# .2f is a special formatting for floats out to a certain number point here we are using 2
print(f"{z:.2f}")
