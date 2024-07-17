from src.componnents.ExpReg import ExpReg


"""
How to add expressions?
- Add the name of the column and the data it should contain. By separating with "," we can add more
data that the column should contain. An example of an email column that requires the data "@" and "."
 It would be like this: 'email': [ExpReg('email', r'@'), ExpReg('email', r'\.')]
"""

regex_rule = {
    'Email': [ExpReg('Email', r'@'), ExpReg('Email', r'\.')],
    'email': [ExpReg('email', r'@'), ExpReg('email', r'\.')],
    #add more expre..
}

# Other Example:
#   'cuil': [ExpReg('cuil', r'7'), ExpReg('cuil', r'_')]