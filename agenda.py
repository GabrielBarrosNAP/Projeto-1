from sqlite_controller import SQLiteController
from pandas_controller import PandasController
from base import Base

class Agenda(Base, SQLiteController, PandasController):
    def __init__(self):
        super().__init__()
    
    def disponibility(self, day, hour):
        return self.get_rents(day, hour)

    def rent(self):
        print('ALUGOU PATRÃO')

        
client = Agenda()
