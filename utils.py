def validate_input(response, valid_options, raise_exception: Exception = False):
    # While True até a pessoa selecionar uma opção válida
    while True:
        # Verifica se é um número (int) 
        if not str(response).isdigit():
            if raise_exception:
                raise raise_exception
            print('É você um bocó????!!?\nTu é?')
            
        # Verifica se não é uma opção válida
        elif int(response) not in valid_options:
            if raise_exception:
                raise raise_exception
            print('Opção inválida amigão!')
        # Caso seja válido, retorna o input do usúario
        else:
            return int(response)
        # Input para uma nova tentativa
        response = input()
