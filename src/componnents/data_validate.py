import pandas as pd
import re

class ExpReg:
    def __init__(self, nameColumn, contain):
        self.nameColumn = nameColumn
        self.contain = contain

#main function
def validate_row(row, first_row_types, regex_rules):
    errors = []
    error_columns = []

    for col, value in row.items():
        if pd.isna(value):
            errors.append(f"{col}: NULL VALUE")
            error_columns.append(col)
            print(f"NULL VALUE IN: '{col}'")
        else:
            regex_rule_list = regex_rules.get(col, [])
            type_mismatch = pd.api.types.infer_dtype([value]) != first_row_types[col]
            regex_mismatch = any(not rule.matches(str(value)) for rule in regex_rule_list)

            if type_mismatch or regex_mismatch:
                if type_mismatch:
                    errors.append(f"{col}: incorrect data type")
                    print(f"INCORRECT DATA TYPE IN: '{col}'")
                if regex_mismatch:
                    for rule in regex_rule_list:
                        if not rule.matches(str(value)):
                            errors.append(f"{col}: Does not match regex '{rule.pattern}'")
                            print(f"REGEX MISMATCH IN: '{col}'")
                error_columns.append(col)

    return errors, error_columns


# Data validate
def validate_dataframe(df, regex_rules):
    first_row_types = df.iloc[0].apply(lambda x: pd.api.types.infer_dtype([x]))
    errors_and_columns = df.apply(lambda row: validate_row(row, first_row_types, regex_rules), axis=1)
    errors_list = errors_and_columns.apply(lambda x: x[0])
    error_columns_list = errors_and_columns.apply(lambda x: x[1])
    valid_rows = df[errors_list.str.len() == 0]
    invalid_rows = df[errors_list.str.len() > 0]
    error_columns = error_columns_list[errors_list.str.len() > 0]
    return valid_rows, invalid_rows, first_row_types, error_columns


# Save and write excel file
def save_invalid_rows(invalid_rows, file_path, original_df, first_row_types, error_columns):
    invalid_rows = invalid_rows.copy()
    invalid_rows['Error Columns'] = error_columns.apply(lambda cols: ', '.join(cols) if isinstance(cols, list) else '')

    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        original_df.to_excel(writer, sheet_name='Errors', index=False)
        workbook = writer.book
        worksheet = writer.sheets['Errors']
        format1 = workbook.add_format({'bg_color': '#FFCCCC'})

        for index in invalid_rows.index:
            worksheet.set_row(index + 1, None, format1)

        error_col_idx = len(original_df.columns)
        worksheet.write(0, error_col_idx, 'Error Columns')

        for row_idx in invalid_rows.index:
            worksheet.write(row_idx + 1, error_col_idx, invalid_rows.at[row_idx, 'Error Columns'])
