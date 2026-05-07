"""
Write a program to fill in a letter template given below with name and date.
letter='''
    Dear <|NAME|>,
    You are selected!
    <|DATE|>
    '''
"""
letter='''
Dear <|NAME|>,
    You are selected!
    <|DATE|>
    '''
print(letter.replace("<|NAME|>","Disha").replace("<|DATE|>","20/06/2024"))


