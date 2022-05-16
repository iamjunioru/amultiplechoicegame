import time
from termcolor import cprint


def escolher_personagem():
    inicio()
    
def inicio():
    cprint('=-='* 50, 'blue')
    cprint('                           _   _     _             ', 'blue')
    cprint('  ___  ___  _ __ ___   ___| |_| |__ (_)_ __   __ _ ', 'blue')
    cprint(' / __|/ _ \|  _ ` _ \ / _ \ __|  _ \| |  _ \ / _` |', 'blue')
    cprint(' \__ \ (_) | | | | | |  __/ |_| | | | | | | | (_| |', 'blue')
    cprint(' |___/\___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, |', 'blue')
    cprint('                                             |___/ ', 'blue')
    cprint('=-='* 50, 'blue')
    time.sleep(1)
    time.sleep(1)
    apresentação()
    
def apresentação():
    print('\nSeja bem-vindo(a).\n')
    time.sleep(1)
    print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eu viverra ante')
    time.sleep(1)
    print('sagittis suscipit leo. Mauris tempus, ex ac mattis sodales, ipsum quam tincidunt magna')
    time.sleep(1)
    print('ac luctus est odio eu ligula. Curabitur augue')
    time.sleep(1)
    print('\nO que você quer ser?\n')
    time.sleep(1)
    cprint('=-='* 50, 'red')
    print('\n\t1. Mago\n\tVestibulum in ipsum et libero dapibus tincidunt.')
    time.sleep(1)
    print('\n\t2. Lutador\n\tNulla malesuada sem et ex laoreet euismod.')
    time.sleep(1)
    print('\n\t3. Suporte\n\tNullam gravida ut metus sit amet tincidunt.\n')
    cprint('=-='* 50, 'red')



if(__name__ == '__main__'):
    escolher_personagem()
    