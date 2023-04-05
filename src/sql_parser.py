# -*- coding: utf-8 -*-

import sqlparse
import re
from sqlparse.sql import Function, Identifier

def extract_function_name(token_list):
    for token in token_list:
        if isinstance(token, Function):
            for subtoken in token.tokens:
                if isinstance(subtoken, Identifier):
                    return subtoken.value
    return ""

def extract_function_body(statement):
    regex = r'(?:LANGUAGE .*? AS \$_?\$(.*?)\$_?\$)'
    match = re.search(regex, statement.value, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def parse_sql_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    parsed_sql = sqlparse.parse(content)

    data = []

    instructions = [
        'SELECT', 'INSERT', 'DELETE', 'UPDATE', 'COPY', 'EXEC',
        'ALTER', 'DROP', 'TRUNCATE', 'LOCK', 'GRANT',
        'REVOKE', 'REPLACE', 'SECURITY DEFINER', 'CREATE'
    ]

    for statement in parsed_sql:
        if statement.get_type() == "CREATE":
            token_list = statement.tokens
            func_name = extract_function_name(token_list)

            if func_name:
                row = {
                    'Función': func_name
                }

                func_body = extract_function_body(statement)

                for instr in instructions:
                    row[instr] = 'Sí' if re.search(r"(?<!')\b" + instr + r"\b(?!')", func_body, re.IGNORECASE) else 'No'

                copy_path = re.search(r"(?<!')\bCOPY\b(?!').*?\"(.*?)\"", func_body, re.IGNORECASE)
                row['Ruta copy'] = copy_path.group(1) if copy_path else 'No'

                data.append(row)

    return data

