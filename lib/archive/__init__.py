import os
from time import sleep
from lib.interface import *

verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
FundoBrancoLetraBranca = '\033[1;30;47m'


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')

        a.close()
    except FileNotFoundError:
        return False
    else:
        cabecalho(f'O arquivo {verde}{nome}\033[m Carregado!')
        sleep(2)
        os.system('cls')

        return True


def criar_arquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except FileExistsError:
        print(f'Houve um erro na criação do arquivo {nome}.txt')
        sleep(2)
        os.system('cls')
    else:
        cabecalho(f'Arquivo {verde}{nome}\033[m foi criado com sucesso !')
        sleep(5)
        os.system('cls')
        cabecalho('Seja bem vindo a versão 1.3 do Sistema de Cadastro!')
        sleep(5)
        print('Meu nome é André Felipe e eu sou o desenvolvedor do sistema.')
        sleep(5)
        print('Esse sistema está em fase beta, agradeço por estar testando ele')
        sleep(5)
        os.system('cls')
        print(f'Vamos começar! - abrindo {verde}{nome}\033[m')
        BarCharge()
        sleep(2)
        os.system('cls')


# def adicionar_item(arq, data, patrimônio, marca, modelo, cor, status):
#     try:
#         a = open(arq, 'at') # 'at' = append
#     except:
#         print('Houve um erro na abertura do arquivo {}'.format(arq))
#     else:
#         try:
#             arq.write(f'{data};{patrimônio};{marca};{modelo};{cor};{status}')
#             arq.close()
#         except:
#             print('Houve um erro na hora de escrever os dados !')
#         else:
#             print(f'Novo registro de {modelo} adicionado.')
#             a.close()
#             sleep(2)
#             os.system('cls')


def cadastrar(arq, data='-', patrimônio='-', marca='-', modelo='-', cor='-', status='-', situ='-'):
    try:
        a = open(arq, 'at')  # 'at' = append
    except:
        print('Houve um erro na abertura do arquivo !')
    else:
        try:
            a.write(
                f'{data};{patrimônio};{marca};{modelo};{cor};{status};{situ}\n')
        except:
            print('Houve um erro na hora de escrever os dados !')
        else:
            print(f'Novo registro de {patrimônio} adicionado.')
            a.close()


def ProcurarPatrimonio(arq, patrimonio):
    try:
        a = open(arq, 'rt')
    except:
        print(f'Erro ao ler o arquivo {arq}!')
    else:
        # procurar patrimonios iguais e criar uma lista
        lista = []
        for linha in a:
            dado = linha.split(';')
            if dado[1] == patrimonio:
                lista.append(dado)
        cabecalho('Aparelhos encontrados')
        print(
            f'{"Data":^20}{"Patrimônio":^10}{"Marca":^10}{"Modelo":^10}{"Cor":>15}{"Status":^20}{"Situação":^20}')
        for dado in lista:
            dado[5] = dado[5].replace('\n', '')
            print(
                f'{dado[0]:<3}{dado[1]:^10}{dado[2]:^13}{azul}{dado[3]:<20}\033[m{dado[4]:<10}{amarelo}{dado[5]:<10}\033[m{dado[6]:^20}')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')  # rt = read text
    except:
        print(f'Erro ao ler o arquivo {nome}!')
    else:
        cabecalho('Aparelhos cadastrados')
        print(
            f'{"Data":^20}{"Patrimônio":^10}{"Marca":^10}{"Modelo":^10}{"Cor":>30}{"Status":^20}{"Situação":<20}')
        for linha in a:
            dado = linha.split(';')
            dado[5] = dado[5].replace('\n', '')
            print(
                f'{dado[0]:<3}{dado[1]:^10}{dado[2]:^13}{azul}{dado[3]:<20}\033[m{dado[4]:>18}{amarelo}{dado[5]:>13}\033[m{dado[6]:>13}')    
        a.close()


