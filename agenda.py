import json

from base import Base

from sqlite_controller import SQLiteController
from pandas_controller import PandasController

from exceptions import InvalidHour

from utils import validate_input


class Agenda(Base, SQLiteController, PandasController):
    def __init__(self):
        self.db_cadastros = SQLiteController()
        super().__init__()
    
    def __disponibility(self):
        def show_hours(date):
            with open("horarios.json", "r", encoding='utf-8') as r:
                data = json.load(r)
                print(f"{'='*34}HORAS PARA LOCAÇÃO{'='*34}")
                for index, hour in enumerate(data[date], start=1):
                    print(f'\033[1;34m{index}º:\033[1;m {hour} Horas.')
                response = validate_input(input(), valid_options=[num+1 for num in range(len(data[date]))], raise_exception=InvalidHour('Horário selecionado é invalido.'))
                hour_choose = data[date][response-1]
                return hour_choose
            
        print(f"""
{'='*34}DIAS PARA LOCAÇÃO{'='*34}

1- Terça-Feira
2- Quarta-Feira
3- Quinta-Feira
4- Sexta-Feira
5- Sábado
6- Domingo
7- Voltar
    """)
        dates = {
            1: 'Terça',
            2: 'Quarta',
            3: 'Quinta',
            4: 'Sexta',
            5: 'Sábado',
            6: 'Domingo'
        }
        day_response = validate_input(input(), valid_options=[1,2,3,4,5,6,7])
        if day_response == 7:
            self.__main_menu()
        else:
            hour_response = show_hours(dates.get(day_response))
            return self.get_rents(dates.get(day_response), hour_response)

    def __rent(self):
        print('ALUGOU PATRÃO')
        
    def __login_menu(self):
        print(f"""
{'='*34}LOGIN{'='*34}
              """)
    
    def __main_menu(self):
        while True:
            print(f"""
    {'='*34}AGENDA{'='*34}

    1- Verificar disponibilidade.
    2- Arrendar quadra.
    3- Finalizar.
        """)
            
            # Pegando input do usuario e validando se é uma opção válida.
            response = validate_input(input(), valid_options=[1,2,3])
            
            # Caso queria verificar disponibilidade
            if response == 1:
                disponibility = self.__disponibility()

                print(f"Pessoas que usarão a quadra no dia e horario especifico:")
                
                peoples_using = [people for people in disponibility.iloc[0].split('|') if people]
                print("\n".join(peoples_using))
                
                if len(peoples_using)<4:
                    print('\033[1;32mTa disponivel\033[1;m')
                else:
                    print(f"\033[1;31mEsse horário já está locado.\033[1;m")
                    #raise InvalidHour(f'Não existe esse horario disponivel no dia em questão.')

            # Caso queria alugar a quadra
            elif response == 2:
                self.__rent()
            
            # Caso queria sair, finalizar script.
            elif response == 3:
                break
    
    def execute(self):
        self.__main_menu()
