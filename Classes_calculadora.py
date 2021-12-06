class Calculadora:
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    def Soma(self):
        soma = self.number_one + self.number_two
        return print(f'A soma entre {self.number_one} e {self.number_two} é de {soma}')

    def Subtraçao(self):
        while True:
            controller = input("Deseja inverter os valores? [S/N]: ")
            if controller.lower() == 's':
                subtracao = self.number_two - self.number_one
                return print(f'A subtração entre {self.number_two} e {self.number_one} é de {subtracao}')
            elif controller.lower() == 'n':
                break
            else:
                print('Erro tente de novo')
            subtracao = self.number_one - self.number_two
        return print(f'A subtração entre {self.number_one} e {self.number_two} é de {subtracao}')

    def Divisao(self):
        while True:
            controller = input("Deseja inverter os valores? [S/N]: ")
            if controller.lower() == 's':
                divisao = self.number_two / self.number_one
                return print(f'A divisão entre {self.number_two} e {self.number_one} é de {divisao}')
            elif controller.lower() == 'n':
                break
            else:
                print('Erro tente de novo')
        divisao = self.number_one / self.number_two
        return  print(f'A divisão entre {self.number_one} e {self.number_two} é de {divisao}')

    def Multiplica(self):
        multi = self.number_one * self.number_two
        return print(f'A multiplicação entre {self.number_one} e {self.number_two} é de {multi}')


