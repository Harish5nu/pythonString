"""Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''"""
letter='''Dear <|Name|>,
you are selected<|Date|>'''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", " 24 sept 2068"))