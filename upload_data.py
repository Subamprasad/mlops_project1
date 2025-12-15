import pandas as pd
import sqlite3
import os

def import_data_to_sqlite(csv_file_path, db_name="student.db", table_name="student_performance"):
    try:
        # Create a connection to the SQLite database
        # This will create the file if it doesn't exist
        connection = sqlite3.connect(db_name)
        print(f"Connected to SQLite database: {db_name}")
        
        # Read CSV
        df = pd.read_csv(csv_file_path)
        print(f"Read CSV file: {csv_file_path}")
        print(f"Columns: {df.columns.tolist()}")
        print(f"Number of rows: {len(df)}")
        
        # Write the data to a sqlite table
        # if_exists='replace' will drop the table if it already exists and recreate it
        df.to_sql(table_name, connection, if_exists='replace', index=False)
        
        print(f"Successfully inserted {len(df)} rows into `{table_name}` table in {db_name}")
        
        # Verify
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Verification: Table now has {count} rows.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    csv_path = "student-por.csv"
    import_data_to_sqlite(csv_path)
