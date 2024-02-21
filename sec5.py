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
    print("reese has six toes (total)")
    pass

def liveable_shellac():
    print('That looked a little Mahomey')
    print('But a can of soup, you can really put some power behind that.')
    pass

def minded_floor():
    # YOUR CODE HERE!
    print('01110111 01100001 01110011 01110100 01100101 00100000 01110100 01101001 01101101 01100101')
    print('unbound-meaninglessness')
    pass

def mythical_phrontistery():
    # YOUR CODE HERE!
    print()
    phron = 'What is a phrontistery? Great question! No idea!\nI looked it up, though, and heres what I found:\n\n\tA phrontistery can by any place ideal for thinking - including puplic\n\tlibraries and museums, as well as parks, forests, and any other places\n\twhere meditation comes easily.'
    print(phron)
    print()
    pass

def obsessed_disorganization():
    print('I love Roblox. Roblox is my life. Im going into debt because I cant quit buying robux. My name is Dan Prather.')
    pass

def ruly_yellowhammer():
    # YOUR CODE HERE!
    pass

def strategic_citron():
    # YOUR CODE HERE!
    pass

def summary_wakening():
    print("What am I doing here?")
    pass

def taboo_cup():
    print('live laugh love')
    pass

def unbolted_toea():
    # YOUR CODE HERE!
    pass

def ungoverned_muishond():
    print('ungoverned???')
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
