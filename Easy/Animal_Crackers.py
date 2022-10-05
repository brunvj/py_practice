#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
    
    
def animal_crackers(text):
    # create a list out of the input string
    l = text.split()
    # check if first char in element 0 in list is equal to first char in element 1
    if l[0][0] == l[1][0]:
    # return True
        return True
    # else return False
    else:
        return False
