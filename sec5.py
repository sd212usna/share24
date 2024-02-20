# Add a few lines of code to do something ONLY under your own
# function name.
# Your code can do whatever you like, but it should PRINT something
# at the very least (and not do anything dangerous or super-slow!)
#
# When you run this whole .py file, it will print out the names
# of all the functions and run them one at a time.

def catabolic_galangal():
    # YOUR CODE HERE!
    pass

def clerical_truncation():
    # YOUR CODE HERE!
    pass

def liveable_shellac():
    # YOUR CODE HERE!
    pass

def minded_floor():
    # YOUR CODE HERE!
    pass

def mythical_phrontistery():
    # YOUR CODE HERE!
    print()
    phron = 'What is a phrontistery? Great question! No idea!\nI looked it up, though, and heres what I found:\n\n\tA phrontistery can by any place ideal for thinking - including puplic\n\tlibraries and museums, as well as parks, forests, and any other places\n\twhere meditation comes easily.'
    print(phron)
    print()
    pass

def obsessed_disorganization():
    # YOUR CODE HERE!
    pass

def ruly_yellowhammer():
    # YOUR CODE HERE!
    pass

def strategic_citron():
    # YOUR CODE HERE!
    pass

def summary_wakening():
    # YOUR CODE HERE!
    pass

def taboo_cup():
    # YOUR CODE HERE!
    pass

def unbolted_toea():
    # YOUR CODE HERE!
    pass

def ungoverned_muishond():
    # YOUR CODE HERE!
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
