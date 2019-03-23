def change_files(filename, crypto, block_size=16):
    '''
    este módulo é responsável por encriptar e desencriptar os arquivos
    de acordo com o valor de 'crypto'.
    :filename: é o nome do arquivo, de preferencia um caminho absoluto
    :crypto: é uma uma função de stream cifrada que recebe um valor
    em texto plano e retorna um texto cifrado de tamanho idêntico.
    :block_size: o tamanho dos blocos para ler e escrever
    :return: None
    '''
    with open(filename, 'r+b') as f:
        plaintext = f.read(block_size)
        while plaintext:
            ciphertext = crypto(plaintext)
            # Compara o tamanho dos blocos cifrado e plano
            if len(plaintext) != len(ciphertext):
                # lança um erro caso o ciphertext não seja um stream cifrado de plaintext
                raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}. Não é uma stream cifrada.'.format(
                    len(ciphertext), len(plaintext)))

            f.seek(-len(plaintext), 1)
            f.write(ciphertext)
            plaintext = f.read(block_size)
