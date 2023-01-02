import json

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
    Gravar_dados(dados)

