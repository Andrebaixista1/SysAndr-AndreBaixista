import os
import emoji
from time import sleep
from lib.interface import *
from lib.archive import *
from datetime import datetime as dt
os.system('cls')

arq = 'BancoDeDados.txt'
# Opções
marcaDB = ['Samsung', 'Apple', 'Motorola']
modeloDB = ['Galaxy A01 Core (A013)',
            'Galaxy A03s (A037)',
            'Galaxy A10s (A107)',
            'Galaxy J5 Prime (G570)',
            'Galaxy J5 Pro (J530)',
            'Galaxy J7 Metal (J710)',
            'Galaxy J7 Prime 2 (G611)',
            'Galaxy S10e (G970)',
            'Galaxy S20 (G980)',
            'Galaxy S6 (G920)',
            'Galaxy S7 (G930)',
            'Galaxy S8 (G950)',
            'Galaxy TAB A - 10.5" (T590)',
            'Galaxy Tab A 10.1" (T510)',
            'Galaxy TAB A 8" (T290)',
            'Galaxy Tab A 9.7" (P555)',
            'Galaxy Tab A6 7" (T280)',
            'Galaxy Tab Active 2 (T395)',
            'iPad Air - 9.7" Wi-fi (A1475)',
            'iPad Air 2 - 9.7" 4G (A1396)',
            'iPhone 8 (A1864)',
            'Moto E6 Plus (XT2025)',
            'Moto E7 Plus (XT2081)',
            'Moto G5S Plus (XT1802)',
            'Moto G6 Play (XT1922)',
            'Moto G8 Play (XT2015)']

coresDB = ['Ametista',
           'Azul',
           'Branco',
           'Cinza',
           'Cinza Metálico',
           'Dourado',
           'Indigo',
           'Marrom',
           'Prata',
           'Preto']

statusDB = ['Aguardando Análise',
            'Aguardando Chegada de Peças',
            'Aguardando Compra',
            'Aguardando Garantia',
            'Consertado',
            'Reparo Iniciado - Jhow',
            'Sucata',
            'Tratado']

EntSai = ['Entrada', 'Saída', 'Sem movimentação']


warranty = (f'''
    - Para identificar os possíveis reparos de garantia, seguir:

    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento não liga
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento não carrega
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento carrega, mas não reconhece USB
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento com display queimado (emite som, porém não gera imagem)
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento reiniciando (reboot)
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento com microfone ou alto falante danificado
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento com botões com mal funcionamento
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento com erro de câmera
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento não reconhece SIM card
    {emoji.emojize(':white_check_mark:', use_aliases=True)} Equipamento não reconhece cartão de memória

    - Casos não passíveis de garantia:

    {emoji.emojize(':x:', use_aliases=True)} Equipamento com display quebrado/trincado/com riscos
    {emoji.emojize(':x:', use_aliases=True)} Equipamento com carcaça avariada
    {emoji.emojize(':x:', use_aliases=True)} Equipamento com vidro da câmera avariado
    {emoji.emojize(':x:', use_aliases=True)} Equipamento com sinais de oxidação (molhado)
    {emoji.emojize(':x:', use_aliases=True)} Equipamento com bateria estufada

''')

if not arquivoExiste(arq):
    criar_arquivo(arq)


while True:
    resp = menu(['Abrir Banco de Dados', 'Adicionar Item',
                'Procurar Aparelho', 'Garantias', 'Sair'])

    if resp == 1:
        os.system('cls')
        lerArquivo(arq)
        os.system('pause')
        os.system('cls')
    elif resp == 2:
        os.system('cls')
        cabecalho('Cadastro de Aparelhos')
        data = dt.now().strftime('%d/%m/%Y %H:%M:%S')
        patrimônio = input('Digite o patrimônio do aparelho: ').upper()
        marca = marca(marcaDB)
        marca = marcaDB[marca - 1]

        modelo = modelo(modeloDB)
        modelo = modeloDB[modelo - 1]

        cor = cor(coresDB)
        cor = coresDB[cor - 1]

        status = status(statusDB)
        status = statusDB[status - 1]

        situ = situacao(EntSai)
        situ = EntSai[situ - 1]
        cadastrar(arq, data, patrimônio, marca, modelo, cor, status, situ)
    elif resp == 3:
        os.system('cls')
        cabecalho('Procurar Aparelho')
        patrimônio = input('Digite o patrimônio do aparelho: ').upper()
        ProcurarPatrimonio(arq, patrimônio)
        os.system('pause')
        os.system('cls')

    elif resp == 4:
        os.system('cls')
        print(warranty)
        os.system('pause')
        os.system('cls')
    elif resp == 5:
        print('Obrigado por utilizar... Volte Sempre!')
        sleep(1)
        BarCharge()

        os.system('cls')
        break
    else:
        print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
        # os.system('pause')
        os.system('cls')
