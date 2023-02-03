def validate_input(response):
    VALID_OPTIONS = [1,2,3,4]
    while True:
        if not str(response).isdigit():
            print('É você um bocó????!!?\nTu é?')
        elif int(response) not in VALID_OPTIONS:
            print('Opção inválida amigão!')
        else:
            return int(response)
        response = input()
