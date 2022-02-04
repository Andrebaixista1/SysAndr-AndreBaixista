import datetime as dt
from time import sleep
import os



lilas = '\033[94m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                '\033[33mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def linha(tam=150):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(150))
    print(linha())


def menu(lista):
    dataHoje = dt.datetime.now()

    cabecalho(f'Sistema de Cadastro (SysAnd)- {dataHoje:%d/%m/%Y %H:%M:%S}')

    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')

    return opc


def abrir_arquivo(nome):
    try:
        a = open(nome, 'rt')  # rt = read text
    except FileNotFoundError:
        print('Erro ao ler o arquivo !')
        menu()
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def BarCharge():
    for c in range(0, 101):
        txt = '  Loading...'
        print(f'{txt}{c}%', end='\r')
        sleep(0.001)
    os.system('cls')
    print('SystemAnd - 2022 © Todos os direitos reservados.')
    sleep(1)
    print('Criado e Desenvolvido por: André Felipe Pinto')
    sleep(1)


def marca(lista):
    dataHoje = dt.datetime.now()
    cabecalho(f'Marca - {dataHoje:%d/%m/%Y %H:%M:%S}')

    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')
    os.system('cls')
    return opc


def modelo(lista):
    dataHoje = dt.datetime.now()
    cabecalho(f'Modelo - {dataHoje:%d/%m/%Y %H:%M:%S}')

    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')
    os.system('cls')
    return opc


def cor(lista):
    dataHoje = dt.datetime.now()
    cabecalho(f'Cor - {dataHoje:%d/%m/%Y %H:%M:%S}')

    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')
    os.system('cls')
    return opc


def status(lista):
    dataHoje = dt.datetime.now()
    cabecalho(f'Status - {dataHoje:%d/%m/%Y %H:%M:%S}')

    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')
    os.system('cls')
    return opc


def situacao(lista):
    dataHoje = dt.datetime.now()
    cabecalho(f'Entrada/Saida - {dataHoje:%d/%m/%Y %H:%M:%S}')
    c = 1
    for item in lista:
        print(f'{lilas}{c}\033[m - {amarelo}{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('Sua Opção: ')
    os.system('cls')
    return opc


def MenuDeAparelhos():
    print(f'{"Data":^20}{"Patrimônio":^15}{"Marca":^20}{azul}{"Modelo":^29}\033[m{"Cor":^30}{amarelo}{"Status":^20}\033[m{"Situação":^20}')
    print(linha())
