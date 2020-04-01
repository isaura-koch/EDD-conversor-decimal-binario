from pilha import Pilha
import os

class ConversorDecimalBinario:
    def __init__(self):
        self.pilha = Pilha()

    def converte_decimal_para_bin(self, numero):
        binario = self.pilha
        while numero is not 0:
            (resultado, resto) = divmod(numero, 2)
            binario.push(resto)
            numero = resultado
        return binario
    
    def limpa_pilha(self, pilha_decimal):
        while len(pilha_decimal) > 0:
            pilha_decimal.pop()
        return pilha_decimal

    def run(self):
        while True:
            print("Bem-vindo(a) ao conversor de decimal para binário!!!")
            numero = int(input("Insira o número que deseja converter para binário: "))
            resultado_binario = self.converte_decimal_para_bin(numero)
            print(resultado_binario)
            self.limpa_pilha(resultado_binario)
            opcao = int(input("Para encerrar o conversor digite 1, para converter outro número digite 2: "))
            if opcao == 1:
                print("Obrigada por utilizar o sistema! Até logo c:")
                break
            os.system('cls' if os.name == 'nt' else 'clear')

conversor = ConversorDecimalBinario().run()