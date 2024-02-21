# Add a few lines of code to do something ONLY under your own
# function name.
# Your code can do whatever you like, but it should PRINT something
# at the very least (and not do anything dangerous or super-slow!)
#
# When you run this whole .py file, it will print out the names
# of all the functions and run them one at a time.

def appressed_encrustation():
    # YOUR CODE HERE!
    pass

def awnless_wineskin():
    print("Tyrese Maxey is the best PG is the east.")
    pass

def bedded_domain():
    # YOUR CODE HERE!
    pass

def lxxviii_thrombin():
    print('I did the homework!')
    pass

def overnice_chorus():
    # YOUR CODE HERE!
    pass

def poor_derivation():
    print("Hello World")
    pass

def shamanistic_hooter():
    # YOUR CODE HERE!
    pass

def slim_zero():
    # YOUR CODE HERE!
    pass

def sustained_objection():
    # YOUR CODE HERE!
    pass

def unconverted_threat():
    # YOUR CODE HERE!
    print("doodlebob rulz")
    pass

def ungoverned_dolichocephalic():
    print("Done")
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
