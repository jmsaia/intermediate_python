#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj12.py
#Revised: 02/25/23
'''
This assignment requires you to demonstrate much of
what you have learned throughout this and the
prerequisite course. It may also require you to do
online research beyond that which is explicitly covered
in the Study Guide.

If there is anything that you don't understand about
the requirements or the code in this file, please ask
for clarification well in advance of the due date.
However this assignment is an end-of-semester assessment
of what you have learned. Please don't ask me to provide
you with the required code for the file named
Proj12Runner.py.

You should study and make sure you understand all the
code in this file and the assignment specifications
before you begin writing the code for the file named
Proj12Runner.py.
'''

import sys
from Proj12Runner import Runner
import matplotlib.pyplot as plt

# Check if the user has entered two positive command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 2:
    print("Error: You must enter exactly two command-line")
    print("arguments in the format 'FileName,NumberRowsToPlot")
    sys.exit()

#Create and display a list of command-line arguments
args = sys.argv[1].split(",")
if int(args[1]) <= 0:
    print("Negative or zero argument is not allowed.")
    sys.exit()

#Display the command-line arguments
print()
print('args = ',args)
print()

#Run the program
ax = Runner.run(args)

#Set the size of the plot and make it visible
fig = plt.gcf()
fig.set_size_inches(7,4)
plt.tight_layout()
plt.show()

#Note, the following statement won't be executed until you dismiss
#the graph by clicking the X in the upper-right corner.
print("Goodbye")
#The End

