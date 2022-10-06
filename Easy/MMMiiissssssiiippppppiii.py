#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    
    
def paper_doll(text):
    text_duplicate = str()
    # for each letter in the list, add it to itself
    for char in text:
        text_duplicate += char + char + char
    return text_duplicate
