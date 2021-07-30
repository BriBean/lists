# name:
# author:

# -------------------- Section 1 ------------------------- #
# ------------------ List Creation ----------------------- #
print('# ------------- Section 1 --------------- #')
print('Creating an Empty List \n')

# 1. Creating an Empty List
# --------------------------------------------------------
# Instructions
#   1. Create empty lists using the following methods.
#       a. via List Displays
#       b. via the list() function.
#   2. Print the lists.
#
# WRITE CODE BELOW
list0 = []
list1 = list() # calling a list function
print(list0)
print(list1)
print('\n' 'Creating a Pre-Populated List' '\n')
#Creating a Pre-Populated List
#------------------------------------------------------------
# Instructions
#   1. Create the following pre-populated lists:
#       a. A list filled with 5 integers.
#       b. A list filled with 5 floats.
#       c. A list filled with 3 boolean values (True / False)
#       d. A list of three animals
#       e. A list with of 3 objects, that are all different data types.
#       f. Convert the string of the name of a star to a list via the list() function.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
list2 = [1, 15, -4, -26, 34]
list3 = [15.23, 4.5, 7.8, 6.0, 30.9]
list4 = [4 == 4, 2.5 > 3.4, 20 == 20]
list5 = ['okapi', 'alpaca', 'otter']
list6 = [100, 2.5, 'bear']
name = input('star: ')
name = list(name)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print('\n')
# you are able to choose whatever datatype you want, the list doesn't always have to be consistent.
print('# -------------- Section 2 ---------------- #')
#List Modification
print('Accessing and Modifying a List' '\n')
# 1. Accessing and Modifying a List
#-------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Replace the item at position 2 with a new number.
#       b. Floats --> Replace the item at position 4 with a new number.
#       c. Booleans --> Replace the item at position 0 with itself negated. (not)
#       d. Animals --> Replace one of the animals with a new animal.
#       e. Objects --> Replace one of the items within the list with a new one.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
list2[2] = 44
list3[4] = 2.1
list4[2] = not list4[2]
list5[0] = 'frog'
list6[1] = -200
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print('\n' 'Append, Insert, and Remove' '\n')
# 2. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Append a new number to the list.
#       b. Floats --> Append a new float to the list.
#       c. Booleans --> Remove one of the items from the list
#       d. Animals --> Insert a new animal at the beginning of the list.
#       e. Objects --> Insert a new object at the middle of the list.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
list2.append(25)
list3.append(10.5)
list4.remove(20 == 20)
list5.insert(0, 'cat')
list6.insert(2, 20.2)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print('\n' 'List Concatenation' '\n')
# 3. List Concatenation ------------------------------------------------------------
#
# Lists like Strings can Concatenate with other Lists using the + operator. They can also be duplicated by
#   multiplying the list.
#
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Concatenate the lists holding the integers and floats together, and save the result to a new variable.
#       d. Duplicate the list holding animals 3 times, and save the result to a new variable.
#   2. Print the new lists.
#
#   Examples are below for reference
#
# WRITE CODE BELOW
example_concatenation = [1, 2, 3] + ['cat', 'dog']
example_duplication = ['cat'] * 5

print(
    '\n'
    f'example_concatenation | {example_concatenation}' '\n'
    f'example_duplication | {example_duplication}' '\n'
 )

concatenation = list2 + list3
print(concatenation)
duplication = list5 * 3
print(duplication)
# ------------- Section 3 -------------- #
# --------------------- Looping -------------------------- #
print('\n' '# ------------- Section 3 ------------- #') 
print('Looping' '\n')
# 1. Looping
# ------------------------------------------------------------
# Instructions
#   1. Create a loop that prints out the contents of the two of the lists you have already created, using the
#       methods below.
#       a. via in range()
#       b. via direct access
#
#   An example has been shown below:
#
# WRITE CODE BELOW
for i in range(len(list6)): # in range ()
    print(list6[i])
for item in list4: # direct access
    print(item)

# -------------------- Section 4 ------------------------- #
# ------------------ Comprehension ----------------------- #
print('\n' '# ------------- Section 4 ------------- #') 
print('Dice - Statistics' '\n')

# 1. Dice - Statistics
# ------------------------------------------------------------
# Preface
#   When we roll a dice, the side it lands on is random. However, since a dice has multiple sides that are equivalent
#       in chance of falling, then we say a side has a 1/6 chance of happening, or 16.7% chance. Lets test to see if
#       that's true!
#
# 1. Create multiple for loops to run 5, 10, 100, and 1000 times.
#   a. Within the loops, roll a dice and append the roll to a list that is keeping track of all the rolls.
# 2. After the loop has finished rolling, print the number of times each face appeared, as well as the rate of
#   rate of appearance.
#
# The beginning of the loop running 5 times has been done for you. Be sure to finish it.
#
# WRITE CODE BELOW
from random import randint

def print_rolls(rolls_, size_):
   print(f'rolls | {rolls}')
   print(f'1\t| total - {rolls.count(1)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(1) / size)}')

