from PIL import Image
import os
import unidecode
import random, string
def Nome(tipo):
    ## gerador de nome aleatorio
    letras = string.ascii_letters
    nome = ''.join(random.choice(letras) for i in range(15)) + '.' + tipo
    return 'geradas/' + nome

def Ordenar(texto):
    # busca as imagens na pasta #
    pasta = 'imagens'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    imagens = [arq for arq in arquivos if arq.lower().endswith(".jpg") or arq.lower().endswith(".png")  or arq.lower().endswith(".jpeg")]
    # -- #
    # Busca os arquivos da letras e sorteia 1 dos arquivos #
    # retornando assim uma lista com os arquivos. #
    ordem = []
    texto = texto.upper()
    sorteio = []
    for l in texto:
        for i in imagens:
            if l in i:
                sorteio.append(i)
        ordem.append(random.choice(sorteio))
        sorteio = []
    return ordem
def Criar(texto):
    ## cria imagem e retona o objeto imagem
    texto = unidecode.unidecode(texto) ## remove acentos
    # Utiliza as outras funções para realizar todo
    # Separa o texto em uma lista
    separado = texto.split(' ') #separa as palavras
    maior = max(separado, key=len) #encontro a maior palavra
    lista = [] ## aqui é o processo de criar uma lista com a lista das imagens conforme as palavras
    for i in separado:
        palavra = Ordenar(i)
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
    return fundo
class gerador:
    def gif(quantas=5, texto='test'):
        frames = []
        conta = 0
        while conta <= quantas:
            frames.append(Criar(texto))
            conta += 1
        nome = Nome('gif')
        frames[0].save(nome, save_all=True, append_images=frames[1:], optimize=True, duration=450, loop=0)
        return nome
    def png(texto):
        img = Criar(texto)
        nome = Nome('png')
        img.save(nome, format='png')
        return nome


if __name__ == '__main__':
    texto = 'classe' #str(input("Digite um texto: "))
    imagem = gerador.png(texto=texto)
    gif = gerador.gif(5, texto) 
    print(f'Geradas {imagem} e {gif}')