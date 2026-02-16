#Q2 reate a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

# solution:-
def greet(name):
    #Good Luck (like you need it)
    
    return (f"Hello, {name} how are you doing today?")

#Q1 Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# solution:
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1