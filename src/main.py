from  sql_parser import parse_sql_file
from excel_generator import  create_excel_output
# from read_sql_file import read_sql_file
def main():
  input_file = '/home/diego/Development/sql-files/file.sql'
  output_file = '/home/diego/Development/mapped-aforeglobal-functions/aforeglobal_mapped_functions.xlsx'
  
  parsed_data = parse_sql_file(input_file)
  create_excel_output(parsed_data, output_file)
  # # Parámetros y columnas
  #   input_file_path = "input.sql"
  #   output_file_path = "output.xlsx"
  #   columns = ['Función', 'Dueño', 'SELECT', 'INSERT', 'DELETE', 'UPDATE', 'COPY', 'EXEC', 'ALTER', 'DROP', 'TRUNCATE', 'LOCK', 'GRANT', 'REVOKE', 'REPLACE', 'SECURITY DEFINER', 'CREATE', 'Ruta copy']

  #   # Leer archivo SQL
  #   sql_content = read_sql_file(input_file_path)

  #   # Extraer funciones y sus propiedades
  #   functions = extract_functions(sql_content)

  #   # Extraer instrucciones y propiedades
  #   functions_data = [extract_function_data(f) for f in functions]

  #   # Crear un DataFrame con los datos
  #   df = create_dataframe(columns, functions_data)

  #   # Guardar el DataFrame en un archivo Excel
  #   save_dataframe_to_excel(df, output_file_path)
    
if __name__ == '__main__':
  main()
