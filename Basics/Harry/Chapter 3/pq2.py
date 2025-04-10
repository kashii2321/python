# write a program to fill in a letter template given below with name and date 
letter = '''Dear <|Name|>,
                You are selected! 
                <|Date|>'''

print(letter.replace("<|Name|>)", "Yuvraj").replace("<|Date|>", "21 sept 2025"))

# pehle puri string mein replace krwaya name ko fir replaced string mein dobara replace krwaya date ko replace krne ke liye
