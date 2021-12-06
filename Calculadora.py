from Classes_calculadora import *

first_number = int(input("Digite o seu primeiro valor: "))
second_number = int(input("Digite seu segundo valor: "))

case = input("""
==============================
    BEM VINDO A CALCULADORA!
    
ESCOLHA A OPERAÇÃO QUE DESEJA:
[1] - SOMA
[2] - SUBTRAÇÃO
[3] - DIVISÃO
[4] - MULTIPLICAÇÃO
[5] - TODAS AS OPERAÇÕES
[6] - SAIR
DIGITE O NUMERO DA OPERAÇÃO AQUI:  """)

def Switch(case):
    calculadora = Calculadora(first_number, second_number)
    if case == '1':
        return calculadora.Soma()
    elif case == '2':
        return calculadora.Subtraçao()
    elif case == '3':
        return calculadora.Divisao()
    elif case == '4':
        return calculadora.Multiplica()
    elif case == '5':
        calculadora.Soma()
        calculadora.Subtraçao()
        calculadora.Divisao()
        calculadora.Multiplica()
    elif case == '6':
        exit()

Switch(case)