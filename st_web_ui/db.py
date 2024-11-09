import sqlite3
import csv
import pandas as pd
from typing import Dict

class SQLiteManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self._create_db_and_table()

    def _create_db_and_table(self):
        """Create the SQLite database and table if they do not exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create table schema with specified columns
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            created_at TEXT,
            status TEXT,
            device TEXT,
            failure_point TEXT,
            serial_number TEXT,
            topic TEXT,
            description TEXT
        )
        ''')
        conn.commit()
        conn.close()

    def init_db_from_csv(self, csv_file: str):
        """Initialize the database by loading specified columns from a CSV file."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Define the columns to extract
        desired_columns = ['created_at', 'status', 'Тип оборудования', 'Точка отказа',
                           'Серийный номер', 'Тема', 'Описание']
        
        # Map CSV columns to database columns
        column_mapping = {
            'created_at': 'created_at',
            'status': 'status',
            'Тип оборудования': 'device',
            'Точка отказа': 'failure_point',
            'Серийный номер': 'serial_number',
            'Тема': 'topic',
            'Описание': 'description'
        }
        
        # Read CSV and insert only desired columns into the database
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Extract the necessary fields based on column_mapping
                extracted_data = {db_col: row[csv_col] for csv_col, db_col in column_mapping.items() if csv_col in row}
                
                cursor.execute('''
                INSERT INTO tasks (created_at, status, device, failure_point, serial_number, topic, description)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    extracted_data['created_at'], extracted_data['status'], extracted_data['device'],
                    extracted_data['failure_point'], extracted_data['serial_number'],
                    extracted_data['topic'], extracted_data['description']
                ))
        
        conn.commit()
        conn.close()

    def add_row(self, data: Dict):
        """Add a new row to the database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO tasks (created_at, status, device, failure_point, serial_number, topic, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (data['created_at'], data['status'], data['device'], data['failure_point'], 
              data['serial_number'], data['topic'], data['description']))
        
        conn.commit()
        conn.close()

    def fetch_all(self):
        """Fetch all rows from the tasks table."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()
        
        conn.close()
        return rows
    

    def load_to_dataframe(self) -> pd.DataFrame:
        """Load the contents of the tasks table into a pandas DataFrame."""
        conn = sqlite3.connect(self.db_name)
        query = "SELECT * FROM tasks"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df