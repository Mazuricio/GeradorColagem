import json
import os

def Ler_imagens(pasta):
    #pasta = 'imagens'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    imagens = [arq for arq in arquivos if arq.lower().endswith(".jpg") or arq.lower().endswith(".png")  or arq.lower().endswith(".jpeg")]
    return imagens

def Ler_dados():
    with open("manutencao/dados.json", encoding="utf-8") as mjson:
        dados = json.load(mjson)
    return dados

def Gravar_dados(lista):
    with open("manutencao/dados.json", 'w') as arquivo:
        json.dump(lista, arquivo)

def Somar():
    dados = Ler_dados()
    dados['generatedImages'] += 1
    quantas = Ler_imagens("geradas")
    dados["img_cache"] = len(quantas)
    Gravar_dados(dados)


def Apagar():
    arquivos = Ler_imagens("geradas")
    for i in arquivos:
        os.remove(i)
    dados = Ler_dados()
    quantas = Ler_imagens("geradas")
    dados["img_cache"] = len(quantas)
    Gravar_dados(dados)
    return len(arquivos)