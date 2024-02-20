# Add a few lines of code to do something ONLY under your own
# function name.
# Your code can do whatever you like, but it should PRINT something
# at the very least (and not do anything dangerous or super-slow!)
#
# When you run this whole .py file, it will print out the names
# of all the functions and run them one at a time.

def advertent_vitrectomy():
    print('Hello World!')
    pass

def contaminative_archbishopric():
    print("Mike Jagdon is a big Drake fan")
    pass

def discriminatory_premiership():
    # YOUR CODE HERE!
    pass

def funky_steriliser():
    # YOUR CODE HERE!
    pass

def gaunt_pounce():
    # YOUR CODE HERE!
    pass

def gushing_hodometer():
    print("I'm writing this on cmod :/")
    pass

def methodical_coax():
    print('    __                 __    ')
    print('   /                     \   ')
    print('     ()               ()     ')
    for x in range(2):
        print('')
    print('  \                       /  ')
    print('   \_____________________/   ')
    print('    \_|_|_|_|_|_|_|_|_|_/    ')
    pass

def paradigmatic_tedium():
    food = input("What is your favorite food? ")
    food = food.lower()
    while food != "eggs":
        food = input("You're wrong! Try Again: ")
    print("Correct!")
    pass

def rightful_unfavorableness():
    print("abc")
    pass

def unchanging_aliquot():
    # YOUR CODE HERE!
    pass

def unretrievable_prosthodontia():
    # YOUR CODE HERE!
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
