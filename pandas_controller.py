from os.path import exists
from os import makedirs

import pandas as pd

class PandasController:
    def __init__(self):
        pass
    
    def get_rents(self, day, hour):
        return self.df.query(f"Horarios == {hour}")[day]
