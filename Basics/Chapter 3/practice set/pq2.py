# write a program to fill in a letter template given below with name and date 
Letter = '''Dear <|Name|>,
                You are selected! 
                <|Date|>'''

print(Letter.replace("<|Name|>)", "Yuvraj").replace("<|Date|>", "21 sept 2025"))