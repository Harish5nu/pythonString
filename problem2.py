<<<<<<< HEAD
"""Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''"""
letter='''Dear <|Name|>,
you are selected<|Date|>'''
=======
letter='''Dear <|Name|>,
you are selected<|Date|>'''
>>>>>>> d59ea504d779ff119b73d44e77bec3371ca7b465
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", " 24 sept 2068"))