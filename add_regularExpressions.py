from src.componnents.ExpReg import ExpReg

"""Examples:
    'Email': [ExpReg('Email', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'SSN': [ExpReg('SSN', r'^\d{3}-\d{2}-\d{4}$')], # Formato: 123-45-6789
    'Phone': [ExpReg('Phone', r'^\(\d{3}\) \d{3}-\d{4}$')], # Formato: (123) 456-7890
    'Phone': [ExpReg('Phone', r'^\d{3}-\d{3}-\d{4}$')], # Formato: 123-456-7890
    'ZIP': [ExpReg('ZIP', r'^\d{5}(-\d{4})?$')], # Formato: 12345 o 12345-6789
    'Date': [ExpReg('Date', r'^\d{4}-\d{2}-\d{2}$')], # Formato: MM/DD/YYYY
    'Date': [ExpReg('Date', r'^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD
    'IPv4': [ExpReg('IPv4', r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')],
    'CreditCard': [ExpReg('CreditCard', r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$')], # Formato: 1234-5678-9876-5432 o 1234567898765432
    'URL': [ExpReg('URL', r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')],
    'TIN': [ExpReg('TIN', r'^\d{2}-\d{7}$')], # Formato: 12-3456789
    'CUIL': [ExpReg('CUIL', r'^\d{2}-\d{8}-\d{1}$')], # Formato: 20-12345678-9
"""


# The column name must be the same as the one in Excel!
regex_rule = {
    'Email': [ExpReg('Email', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'EMAIL': [ExpReg('EMAIL', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'MAIL': [ExpReg('MAIL', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'mail': [ExpReg('mail', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],
    'email': [ExpReg('email', r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')],

    'SSN': [ExpReg('SSN', r'^\d{3}-\d{2}-\d{4}$')], # Formato: 123-45-6789
    'ssn': [ExpReg('ssn', r'^\d{3}-\d{2}-\d{4}$')], # Formato: 123-45-6789

    'Phone': [ExpReg('Phone', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890
    'PHONE': [ExpReg('PHONE', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890
    'tel': [ExpReg('tel', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890
    'phone': [ExpReg('phone', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890
    'PhoneNumber': [ExpReg('PhoneNumber', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890
    'PHONENUMBER': [ExpReg('PHONENUMBER', r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$|^\+?[1-9]\d{1,14}$')], # Formato: (123) 456-7890

    'ZIP': [ExpReg('ZIP', r'^\d{5}(-\d{4})?$')], # Formato: 12345 o 12345-6789
    'zip': [ExpReg('zip', r'^\d{5}(-\d{4})?$')], # Formato: 12345 o 12345-6789
    'Date': [ExpReg('Date', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD
    'DATE': [ExpReg('DATE', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD
    'date': [ExpReg('date', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD
    'DateTime': [ExpReg('DateTime', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD
    'DATETIME': [ExpReg('DATETIME', r'^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$')], # Formato: YYYY-MM-DD

    'IPv4': [ExpReg('IPv4', r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')],
    'CreditCard': [ExpReg('CreditCard', r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$')], # Formato: 1234-5678-9876-5432 o 1234567898765432
    'URL': [ExpReg('URL', r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')],
    'url': [ExpReg('url', r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')],
    'TIN': [ExpReg('TIN', r'^\d{2}-\d{7}$')], # Formato: 12-3456789
    'CUIL': [ExpReg('CUIL', r'^\d{2}-\d{8}-\d{1}$')], # Formato: 20-12345678-9
    'CUIT': [ExpReg('CUIT', r'^\d{2}-\d{8}-\d{1}$')], # Formato: 20-12345678-9

}






