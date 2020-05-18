def welcome():
    print('''
Bem vindo à calculadora! :) 
''')

def calcular():
    operacao = input('''
Por favor, digite qual operação matemática você deseja:
+ para soma
- para subtração
* para multiplicação
/ para divisão
% para módulo
''')

    numero1 =int(input('Entre com um primeiro número: ')) #convertendo a variavel para tipo int
    numero2 = int(input('Entre com um segundo número: '))

    #soma
    if operacao == '+':
        print('{} + {} = '.format(numero1, numero2))
        print(numero1 + numero2) 

    elif operacao == '-':
    #Subtração
        print('{} - {} = '.format(numero1, numero2))
        print(numero1 - numero2) 

    elif operacao == '*':
    #Multiplicação
        print('{} * {} = '.format(numero1, numero2))
        print(numero1 * numero2) 

    elif operacao == '/':
    #Divisão
        print('{} / {} = '.format(numero1, numero2))
        print(numero1 / numero2) 
    
    elif operacao == '%':
    #Módulo
        print('{} % {} = '.format(numero1, numero2))
        print(numero1 / numero2) 

    else:
        print('Desculpe, digite um operador válido! Execute o programa novamente por favor! :)')

     # Add novamente() função para calcular() função 
    novamente()

# Define novamente() função que pergunta ao usuario se ele quer usar novamente a calculadora
def novamente():

    calc_novamente = input('''
Quer realizar mais cálculos?
Por favor, digite S para SIM, e N para NÃO.
''')

    # se o usuario digitar S, roda função calcular() novamente
    if (calc_novamente.upper() == 'S') or (calc_novamente.upper() ==  'SIM'): #upper para transformar o que o usuario entrar, para maísculo :)
        calcular()

    # Se o usuario digitar N, encerra o programa.
    elif (calc_novamente.upper() == 'N') or (calc_novamente.upper() =='NAO'): #caso o usuario digite NAO
        print('Saindo da Calculadora!')

    # Se o usuario digitar outra tecla, roda a função novamente
    else:
        novamente()


#chama a função calcular()
welcome()
calcular()