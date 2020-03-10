sentence ="I love Coding"
# Displays the Data type
print(type(sentence))
# Extract and Displays the specific character
print(sentence[4])
# Displays displays from first character choosen to the last
print(sentence[2:6])
# Declaring Variables and printing the types of variables
Number1 = 5           # integer data type
Number2 = 5.8         # float data type
Number3 = 3e10j       # complex data type
# checking whether the data type is what I said it is .
print(type(Number1), type(Number2), type(Number3))
#using list
mylist = [23, 82 , 67, 12, 56]     # Numbers
mylist.insert(4,21)                # Insert in position 4, number 21
print(mylist)                      # Printing the new list
mylist.reverse()                   # Reverses my list from the last to the first
print(mylist)
# Testing the Different data types: The difference is (Curly Bracket and normal bracket)
cars = {"Aston Martin", "VW", "Ford", "BMW", "Nissan"}
print(type(cars))                                           #Data Type = Set
cars = ("Aston Martin", "VW", "Ford", "BMW", "Nissan")
print(type(cars))                                           # Data Type = Tuple