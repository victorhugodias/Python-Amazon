import json
import boto3
dicionario = {}
lista = []
linhas = []

def chavesAmazon():
    AWS_SERVER_PUBLIC_KEY = "chaves amazon"
    AWS_SERVER_SECRET_KEY = "chaves amazon"
    session = boto3.Session(
        aws_access_key_id=AWS_SERVER_PUBLIC_KEY,
        aws_secret_access_key=AWS_SERVER_SECRET_KEY,
    )
    s3 = session.resource('s3')
    s3.Object('infnet-victor', 'dados4.json').upload_file('dados.json')

def criarArquivo():
    arquivo = open('listagem.txt', 'r')
    arquivo = arquivo.read().splitlines()
    return arquivo

def organizandoArquivo(arquivo):
    for i in arquivo:
        linhas.append(i.split(','))
    for x in range(0,len(linhas)):
        dicionario = dict(maquina=linhas[x][0], core=linhas[x][1], memoria=linhas[x][2], storage=linhas[x][3])
        lista.append(dicionario)
    return lista

def criandoArquivoNuvem(lista):
    with open('dados.json','w') as arquivo:
        arquivo.write(json.dumps(lista,indent=4))


arquivo = criarArquivo()
lista = organizandoArquivo(arquivo)
criandoArquivoNuvem(lista)
chavesAmazon()

