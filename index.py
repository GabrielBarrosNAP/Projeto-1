import pandas as pd

from agenda import Agenda
from utils import validate_input


if __name__ == '__main__':
    print("""
    1- Verificar disponibilidade.
    2- Arrendar quadra.
        """)

    client = Agenda()
    response = validate_input(input())
    
    if response == 1:
        disponibility = client.disponibility("Quarta", 9)
        if disponibility:
            print('Ta disponivel')
        else:
            print('Num ta não')
    elif response == 2:
        client.rent()
