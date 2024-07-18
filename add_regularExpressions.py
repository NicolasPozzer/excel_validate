from src.componnents.ExpReg import ExpReg

"""Examples:
    # Email format:
    'Email': [ExpReg('Email', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    # Social Security Number Format: Ex. 123-45-6789
    'SSN': [ExpReg('SSN', r'^\d{3}-\d{2}-\d{4}$')],
    # Phone Number Format: Ex. (123) 456-7890 or 123-456-7890 or +14155552671
    'Phone': [ExpReg('Phone', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')],
    # ZipCode Format: Ex. 12345 or 12345-6789
    'ZIP': [ExpReg('ZIP', r'^\d{5}(-\d{4})?$')],
    # Date Format: Ex. YYYY-MM-DD or MM/DD/YYYY
    'Date': [ExpReg('Date', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')],
    # IPv4 Format:
    'IPv4': [ExpReg('IPv4', r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')],
    # CreditCard Format: Ex. 1234-5678-9876-5432 or 1234567898765432
    'CreditCard': [ExpReg('CreditCard', r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$')], 
    # URL Format:
    'URL': [ExpReg('URL', r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')],
    # TIN Format: Ex. 12-3456789
    'TIN': [ExpReg('TIN', r'^\d{2}-\d{7}$')], 
    # CUIL Format: Ex. 20-12345678-9
    'CUIL': [ExpReg('CUIL', r'^\d{2}-\d{8}-\d{1}$')],
"""


# The column name must be the same as the one in Excel!
regex_rule = {
    'Email': [ExpReg('Email', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'SSN': [ExpReg('SSN', r'^\d{3}-\d{2}-\d{4}$')], # Formato: 123-45-6789
    'Phone': [ExpReg('Phone', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890 o 123-456-7890 o +14155552671
    'ZIP': [ExpReg('ZIP', r'^\d{5}(-\d{4})?$')], # Formato: 12345 o 12345-6789
    'Date': [ExpReg('Date', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD o MM/DD/YYYY
    'IPv4': [ExpReg('IPv4', r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')],
    'CreditCard': [ExpReg('CreditCard', r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$')], # Formato: 1234-5678-9876-5432 o 1234567898765432
    'URL': [ExpReg('URL', r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')],
    'TIN': [ExpReg('TIN', r'^\d{2}-\d{7}$')], # Formato: 12-3456789
    'CUIL': [ExpReg('CUIL', r'^\d{2}-\d{8}-\d{1}$')], # Formato: 20-12345678-9
}






