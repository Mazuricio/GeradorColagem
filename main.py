from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from colagem import criar
from manutencao.controle import *

descricao = """Api para a geração de colagem apartir de um texto \n
EM CONSTRUÇÃO
"""
app = FastAPI(
    title="Gerador de Colagem",
    description=descricao,
    version='0.0.1'
)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500"
    ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def home():
    return {'Hello': "World"}

## criar uma pagina de status

@app.get('/colagem')
def criar_colagem(texto: Union[str, None] = None):
    #query_param_1 = str = Query(None, descriotion="Texto que será convertido em imagem")
    imagem = criar(texto) ## no colagem, tem q ver se testar retornar o objeto img sem ser o arquivo, assim fica tudo na ram
    ## se não funcionar dessa forma, tem q criar uma função que apague as imagens na pasta
    ## ver o negocio do io que tinha se caso a primeira tentativa não funcionar
    Somar() ## Controle de imagens geradas
    return FileResponse(imagem)

@app.get('/status')
def status():
    return Ler_dados()


@app.delete('/manutencao')
def limpar(senha: Union[str, None]= None):
    ## provisorio para facilitar minha vida8
    if senha == "minha12":
        Apagar()
        return {"apagar": "realizado"}