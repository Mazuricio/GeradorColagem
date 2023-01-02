from PIL import Image
import os
import unidecode

def ler_imagens(pasta):
    ## informa a pasta com a imagem e retorna uma lista com os nomes dos arquivos
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    imagens = [arq for arq in arquivos if arq.lower().endswith(".jpg") or arq.lower().endswith(".png")  or arq.lower().endswith(".jpeg")]
    return imagens

def ordenar(texto, lista):
    ## pega uma palavra e retorna uma lista com os arquivos de cada letra
    ordem = []
    texto = texto.upper()
    for l in texto:
        for i in lista:
            if l == i[8]:
                ordem.append(i)
    return ordem


def criar(texto):
    texto = unidecode.unidecode(texto) ## remove acentos
    # Utiliza as outras funções para realizar todo
    # Separa o texto em uma lista
    letras = ler_imagens('imagens') # pegas as imagens
    separado = texto.split(' ') #separa as palavras
    maior = max(separado, key=len) #encontro a maior palavra
    lista = [] ## aqui é o processo de criar uma lista com a lista das imagens conforme as palavras
    for i in separado:
        palavra = ordenar(i, letras)
        lista.append(palavra)
    width = len(maior) * 70         # largura conforme a maior palavra
    height = 135 * len(separado)    # altura conforme a quantidade de palavras
    fundo = Image.new('RGBA', (width, height), color=(255, 255, 255, 0)) ## fundo transparente
    linha = 5 ## margem superior de 5px
    for p in lista:  ## pega cada palavra
        comeco = int(((len(maior) - len(p))/2) * 70)  ## calcula o começo da palavra conforme a maior (centralizar)
        for i in p:  # Desenha a linha
            le = Image.open(i)
            fundo.paste(le, (comeco, linha))
            comeco += 70
        linha += 135
        comeco = 0
    nome = 'geradas/' + separado[0] + '.png'  ## esse nome vai precisar ser mais aleatorio
    fundo.save(nome) ## Salva o arquivo
    return nome


if __name__ == '__main__':
    texto = str(input("Digite um texto: "))
    #letras = ler_imagens('imagens')
    #palavra = ordenar(texto, letras)
    arquivo = criar(texto) 
    print(f"Gerado {arquivo}")