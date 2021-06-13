### Original Direction
def john_mary_original(str):
    '''
    Create empty arrays
    Go through the string and find all the indices where each name starts
    Add the indices to the correct array
    See that the array lengths matched to return True
    '''
    JohnArray = []
    Jnum = 0
    MaryArray = []
    Mnum = 0
    while 1:
        index = str.find("John", Jnum)
        if index == -1:
            break
        Jnum = index + 1
        JohnArray.append(index)
    while 1:
        index = str.find("Mary", Mnum)
        if index == -1:
            break
        Mnum = index + 1
        MaryArray.append(index)
    if len(JohnArray) == len(MaryArray):
        return True
    return False

print(john_mary_original('John&Mary&John'))


### Cleaner Solution
import re
def john_mary_new(str):
    #Find the index of the beginning of each match and store it in a new array
    JohnArray = [match.start() for match in re.finditer("john", str.lower())]
    MaryArray = [match.start() for match in re.finditer("mary", str.lower())]
    #Compare the number of matches
    if len(JohnArray) == len(MaryArray):
        return True
    return False

print(john_mary_new('john&Mary'))