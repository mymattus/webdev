import math        #Import the Python Math functionality
 
first = "Matt"     #Fname
last  = "Schmidt"  #Lname
 
sideA = 12.55      #Triangle side A
sideB = 17.85      #Triangle side B
 
sideAsqrd = round(float(sideA**2),2) # Square and round results to 2 places
sideBsqrd = round(float(sideB**2),2)
 
sideC = (sideAsqrd) + (sideBsqrd)    # Sum the 2 sides
sqrtC = round(math.sqrt(sideC),2)    # Find the length of Side C via square root

operand1 = 95      # Assignment line 16
operand2 = 64.5
 
print first, last  # Print my name
 
print "Length of Side C is: ", sqrtC 
 
print operand1,"+",operand2,"=", operand1+operand2  # Add them
print operand1,"-",operand2,"=", operand1-operand2  # Subtract them
print operand1,"*",operand2,"=", operand1*operand2  # Multiply them
print operand1,"/",operand2,"=", operand1/operand2  # Divide them
print operand1,"%",operand2,"=", operand2/operand1  # Percentage of them
 
# For the Operand assignment (#16) I kept it simple so if an OPERATION required
# modification it would require 2 changes to the line.  The first to the 
# descriptive side of the equation and the second to the equation itself.

# Should one of the Operands require changing it would require a single change
# to the code.  That being where the Operand variable is set.
