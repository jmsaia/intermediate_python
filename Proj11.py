#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj11.py
'''
Among other things, this project requires you to 
 Read a csv file containing a large amount of stock market data.
 Extract specific values over a specific time period.
 Process the data.
 Display the processed data as colored lines on a line graph.

Revised 02/21/23 to terminate with an error message
if the user fails to enter six command-line
arguments in the format a,b,c,d,e,f.
'''

from Proj11Runner import Runner
import sys

# Check if the user has entered six command-line arguments
if len(sys.argv) != 2 or len(sys.argv[1].split(',')) != 6:
    print("Error: You must enter exactly six command-line")
    print("arguments in the format 'a,b,c,d,e,f'.")
    sys.exit()

#Create and display a list of command-line arguments
args = sys.argv[1].split(",")
print()
print('args = ',args)
print()

print("Output from student code begins here.")
#Call the run method in the student's file passing
#the args list as a parameter.
Runner.run(args)



