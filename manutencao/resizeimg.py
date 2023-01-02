from PIL import Image
from controle import Ler_imagens
fotos = 'imagens'
### Para redimensionar as imagens para todas ficar em um tamanho padrão
arquivos = Ler_imagens(fotos)
tamanho = (77, 125)
for i in arquivos:
    img = Image.open(i)
    if img.size != tamanho:
        img = img.resize(tamanho, Image.Resampling.BILINEAR)
        img.save(i, format='png')
        