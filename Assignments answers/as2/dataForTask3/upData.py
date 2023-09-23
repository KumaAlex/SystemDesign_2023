import psycopg2
import pandas as pd

# Database connection parameters
db_params = {
    'host': 'localhost',    # PostgreSQL server address
    'database': 'SystemDesign2023',   # Database name
    'user': 'Alex',     # Database username
    'password': '250871elena'  # Database password
}

# Excel file path
excel_file = 'list_BANKRUPT_KZ_ALL.xlsx'

# Connect to the PostgreSQL database
try:
   connection = psycopg2.connect(**db_params)
   cursor = connection.cursor()

   # Read data from Excel file using pandas
   data = pd.read_excel(excel_file)

   # Infer columns from the Excel data
   column_names = data.columns.tolist()
   column_data_types = [str(data[col].dtype) for col in column_names]

   # Create a table in the database
   create_table_query = {", ".join([f"{col} {data_type}" for col, data_type in zip(column_names, column_data_types)])}
   cursor.execute(create_table_query)

   # Insert data into the database table
   data.to_sql('table', connection, if_exists='replace', index=False)

   # Commit the transaction
   connection.commit()

   print("Data uploaded successfully!")

except (Exception, psycopg2.Error) as error:
   print("Error:", error)
finally:
   # Close the database connection
   if connection:
       cursor.close()
       connection.close()