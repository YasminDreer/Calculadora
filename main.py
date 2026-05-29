import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        result = num1 % num2

    return result

def calculadora2(num1: float, num2: float, operador: str) -> float:
    operacoes = {
        '+':  lambda a, b: a + b,
        '-':  lambda a, b: a - b,
        '*':  lambda a, b: a * b,
        '/':  lambda a, b: a / b,
        '**': lambda a, b: a ** b,
        '%':  lambda a, b: a % b,
    }
    if operador not in operacoes:
        return float("nan")
    return operacoes[operador](num1, num2)

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            num1 = float(input('Introduza o primeiro número: '))
            num2 = float(input('Introduza o segundo número: '))
            print('\nOperações disponíveis: +  -  *  /  **  %')
            operador = input('Introduza o operador: ').strip()
            resultado = calculadora(num1, num2, operador)
            if resultado != resultado:
                print('Operador inválido! -> Tente novamente!')
                time.sleep(2)
                continue
            print(f'\nResultado: {num1} {operador} {num2} = {resultado}')
        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)
            continue
        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            continue
        resposta = input('\nDeseja efectuar outra operação? (s/n): ').strip().lower()
        if resposta in ('n', 'não', 'nao'):
            break
    print('\nVolte sempre!\n')
