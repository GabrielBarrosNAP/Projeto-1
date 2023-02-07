import sqlite3
import pandas as pd

from os.path import exists
from os import makedirs

class Base:
    def __init__(self):
        self.validate_files()
    
    def validate_files(self):
        def verify_registers_database():
            conn = sqlite3.connect('registers.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS REGISTERS (NAME TEXT NOT NULL, PHONE INTEGER NOT NULL)")
        
        # def verify_calendar_database():
        #     conn = sqlite3.connect('calendar.db')
        #     c = conn.cursor()
        #     c.execute("CREATE TABLE IF NOT EXISTS CALENDAR ()")
        
        def verify_dataframe_exists():
            if not exists('files/teste.csv'):
                makedirs('files', exist_ok=True)
                
                df = pd.DataFrame(
                    columns=['Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
                    index=[f'{hour}h - {hour+1}h' for hour in range(9, 22)],
                    data=[]
                )
                
                df.to_csv('files/teste.csv', sep=';')
                
        verify_dataframe_exists()
        verify_registers_database()
        # verify_calendar_database()
        
        self.df = pd.read_csv('files/teste.csv', delimiter=';')
