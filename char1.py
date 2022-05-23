import escolhapersonagem

import time
from termcolor import cprint
import pyfiglet

nome_personagem = 'char1'
lista_resp = ['1', '2']

def jogar1():

    explicacao_missao_char1()


def explicacao_missao_char1():
    time.sleep(1)
    print('Nullam gravida ut metus sit amet tincidunt...')
    time.sleep(1)
    print('Nullam gravida ut metus sit amet tincidunt.\n')
    time.sleep(1)

    print('SUA MISSÃO É:')
    time.sleep(1)
    print('xxxx\n')
    time.sleep(1)
    print('Você está na porta do castelo, {}, mas parece que a porta tem um enigme para abri-la.\n'.format(nome_personagem))
    time.sleep(1)
    print('Digite o número correspondente a ação que deseja:')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('1. Desistir e ir embora (nem combina com você)')
    time.sleep(1)
    print('2. Ver enigma!')
    cprint('-'* 80, 'red')
    resposta_abrir_porta_nao_entrou() # caminho a fazer

def resp_desistiu_entrar():
    condicao = True
    while condicao:
        resp_desistiu = input('Digite sua escolha [1 ou 2]:')
        if (resp_desistiu == '1') or (resp_desistiu == '2'):
            print('\nAo desistir de entrar, você não se deu conta de que o sol já estava nascendo...')
            time.sleep(2)
            print('Um dos espelhos de dentro da casa, acabou refletindo um raio de sol em você.\n')
            cprint('GAME OVER! Você morreu.', 'yellow', 'on_red', attrs=['bold'])
            time.sleep(1)
            jogar_novamente()
            condicao = False
        else:
            print('Resposta inválida!')


def jogar_novamente():
    resp_jogar_novamente = input('\nDeseja jogar novamente? [S/N]:')
    if (resp_jogar_novamente.upper().strip() == 'S'):
        escolhapersonagemm.escolha_personagem()
    elif (resp_jogar_novamente.upper().strip() == 'N'):
        print('Até a próxima!')
    else:
        print('Digite uma resposta válida!')
        jogar_novamente()


if __name__ == '__main__':
    jogar1()